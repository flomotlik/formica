import json
import sys

import logging
from formica.s3 import temporary_bucket
from botocore.exceptions import ClientError, WaiterError
from texttable import Texttable
import boto3

from formica import CHANGE_SET_FORMAT

CHANGE_SET_HEADER = ["Action", "LogicalId", "PhysicalId", "Type", "Replacement", "Changed"]

logger = logging.getLogger(__name__)

cf = boto3.client("cloudformation")


class ChangeSet:
    def create(
        self,
        template="",
        change_set_type="",
        parameters=None,
        tags=None,
        capabilities=None,
        role_arn=None,
        s3=False,
        resource_types=False,
        use_previous_template=False,
        use_previous_parameters=False,
    ):
        optional_arguments = {}
        parameters_set = []
        if use_previous_parameters:
            stacks = cf.describe_stacks(StackName=self.stack)
            parameters_set = [
                {"ParameterKey": p["ParameterKey"], "UsePreviousValue": True}
                for p in stacks["Stacks"][0]["Parameters"]
            ]
        if parameters:
            for (key, value) in parameters.items():
                item = next((x for x in parameters_set if x["ParameterKey"] == key), None)
                values = {"ParameterKey": key, "ParameterValue": str(value), "UsePreviousValue": False}
                if item:
                    item.update(values)
                else:
                    parameters_set.append(values)

        if parameters_set:
            optional_arguments["Parameters"] = parameters_set

        if tags:
            optional_arguments["Tags"] = [{"Key": key, "Value": str(value)} for (key, value) in tags.items()]
        if role_arn:
            optional_arguments["RoleARN"] = role_arn
        if capabilities:
            optional_arguments["Capabilities"] = capabilities
        if change_set_type == "UPDATE":
            self.remove_existing_changeset()
        if resource_types:
            optional_arguments["ResourceTypes"] = list(
                set([resource["Type"] for key, resource in json.loads(template)["Resources"].items()])
            )

        if use_previous_template:
            optional_arguments["UsePreviousTemplate"] = True
            self.__change_and_wait(change_set_type, optional_arguments)
        else:
            if s3:
                with temporary_bucket() as t:
                    bucket_name = t.name
                    logger.info("Uploading to Bucket {}".format(bucket_name))
                    file_name = t.upload(template)
                    template_url = "https://{}.s3.amazonaws.com/{}".format(bucket_name, file_name)
                    self.__change_and_wait(change_set_type, {"TemplateURL": template_url, **optional_arguments})
            else:
                self.__change_and_wait(change_set_type, {"TemplateBody": template, **optional_arguments})

    def __change_and_wait(self, change_set_type, optional_arguments):
        try:
            cf.create_change_set(
                StackName=self.stack, ChangeSetName=self.name, ChangeSetType=change_set_type, **optional_arguments
            )
            logger.info("Change set submitted, waiting for CloudFormation to calculate changes ...")
            waiter = cf.get_waiter("change_set_create_complete")
            waiter.wait(ChangeSetName=self.name, StackName=self.stack)
            logger.info("Change set created successfully")
        except WaiterError as e:
            status_reason = e.last_response.get("StatusReason", "")
            logger.info(status_reason)
            if "didn't contain changes" not in status_reason:
                sys.exit(1)

    def __init__(self, stack):
        self.name = CHANGE_SET_FORMAT.format(stack=stack)
        self.stack = stack

    def describe(self):
        change_set = cf.describe_change_set(StackName=self.stack, ChangeSetName=self.name)
        table = Texttable(max_width=150)

        logger.info("Deployment metadata:")
        parameters = ", ".join(
            [
                parameter["ParameterKey"] + "=" + parameter["ParameterValue"]
                for parameter in change_set.get("Parameters", [])
            ]
        )
        table.add_row(["Parameters", parameters])
        tags = [tag["Key"] + "=" + tag["Value"] for tag in change_set.get("Tags", [])]
        table.add_row(["Tags ", ", ".join(tags)])
        table.add_row(["Capabilities ", ", ".join(change_set.get("Capabilities", []))])
        logger.info(table.draw() + "\n")

        table.reset()
        table = Texttable(max_width=150)
        table.add_rows([CHANGE_SET_HEADER])

        def __change_detail(change):
            target_ = change["Target"]
            attribute = target_["Attribute"]
            if attribute == "Properties":
                return target_["Name"]
            else:
                return attribute

        for change in change_set["Changes"]:
            resource_change = change["ResourceChange"]
            table.add_row(
                [
                    resource_change["Action"],
                    resource_change["LogicalResourceId"],
                    resource_change.get("PhysicalResourceId", ""),
                    resource_change["ResourceType"],
                    resource_change.get("Replacement", ""),
                    ", ".join(sorted(set([__change_detail(c) for c in resource_change["Details"]]))),
                ]
            )

        logger.info("Resource Changes:")
        logger.info(table.draw())

    def remove_existing_changeset(self):
        try:
            cf.describe_change_set(StackName=self.stack, ChangeSetName=self.name)
            logger.info("Removing existing change set")
            cf.delete_change_set(StackName=self.stack, ChangeSetName=self.name)
        except ClientError as e:
            if e.response["Error"]["Code"] != "ChangeSetNotFound":
                raise e
