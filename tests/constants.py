import datetime

from dateutil.tz import tzlocal

REGION = 'us-east-1'
PROFILE = 'my-profile'
STACK = 'my-stack'
STACK_ID = 'my-stack-id'
TEMPLATE = 'MYTEMPLATE'
CHANGESETNAME = f'{STACK}-change-set'
CHANGE_SET_TYPE = 'WHATEVER'
CHANGE_SET_PARAMETERS = {'A': 'B', 'B': 'C'}
CHANGESETCHANGES = {'ChangeSetName': 'simpleteststack-change-set', 'ChangeSetId': 'arn:aws:cloudformation:eu-central-1:420759548424:changeSet/simpleteststack-change-set/979f29ac-40c9-4802-b496-0b3f38241bcd', 'StackId': 'arn:aws:cloudformation:eu-central-1:420759548424:stack/simpleteststack/a4f23770-e476-11e6-bfa4-500c44f62262', 'StackName': 'simpleteststack', 'CreationTime': datetime.datetime(2017, 1, 27, 9, 58, 3, 821000, tzinfo=tzlocal()), 'ExecutionStatus': 'AVAILABLE', 'Status': 'CREATE_COMPLETE', 'NotificationARNs': [], 'Capabilities': [], 'Changes': [{'Type': 'Resource', 'ResourceChange': {'Action': 'Remove', 'LogicalResourceId': 'DeploymentBucket', 'PhysicalResourceId': 'simpleteststack-deploymentbucket-1l7p61v6fxpry', 'ResourceType': 'AWS::S3::Bucket', 'Scope': [], 'Details': []}}, {'Type': 'Resource', 'ResourceChange': {'Action': 'Modify', 'LogicalResourceId': 'DeploymentBucket2', 'PhysicalResourceId': 'simpleteststack-deploymentbucket2-11ngaeftydtn7', 'ResourceType': 'AWS::S3::Bucket', 'Replacement': 'True', 'Scope': ['Properties', 'Tags'], 'Details': [{'Target': {'Attribute': 'Tags', 'RequiresRecreation': 'Never'}, 'Evaluation': 'Static', 'ChangeSource': 'DirectModification'}, {'Target': {'Attribute': 'Properties', 'Name': 'BucketName', 'RequiresRecreation': 'Always'}, 'Evaluation': 'Static', 'ChangeSource': 'DirectModification'}]}}, {'Type': 'Resource', 'ResourceChange': {'Action': 'Add', 'LogicalResourceId': 'DeploymentBucket3', 'ResourceType': 'AWS::S3::Bucket', 'Scope': [], 'Details': []}}], 'ResponseMetadata': {'RequestId': '2a95cc4f-e477-11e6-a696-5fdc4c9bb8c5', 'HTTPStatusCode': 200, 'HTTPHeaders': {'x-amzn-requestid': '2a95cc4f-e477-11e6-a696-5fdc4c9bb8c5', 'content-type': 'text/xml', 'content-length': '2816', 'vary': 'Accept-Encoding', 'date': 'Fri, 27 Jan 2017 09:58:33 GMT'}, 'RetryAttempts': 0}}  # noqa
DESCRIBE_STACKS = {'Stacks': [{'StackId': 'arn:aws:cloudformation:eu-central-1:420759548424:stack/teststack/a29eaa70-e7ab-11e6-aada-503f2ad2e536', 'StackName': 'teststack', 'ChangeSetId': 'arn:aws:cloudformation:eu-central-1:420759548424:changeSet/teststack-change-set/91eb2bd2-ffc1-4082-8ccb-4ca244b0f99c', 'CreationTime': datetime.datetime(2017, 1, 31, 11, 51, 43, 596000), 'LastUpdatedTime': datetime.datetime(2017, 1, 31, 13, 55, 20, 357000), 'StackStatus': 'UPDATE_COMPLETE', 'DisableRollback': False, 'NotificationARNs': [], 'Tags': []}], 'ResponseMetadata': {'RequestId': 'b35e44c7-e7c2-11e6-8d56-e7fe8c71bde8', 'HTTPStatusCode': 200, 'HTTPHeaders': {'x-amzn-requestid': 'b35e44c7-e7c2-11e6-8d56-e7fe8c71bde8', 'content-type': 'text/xml', 'content-length': '1979', 'date': 'Tue, 31 Jan 2017 14:36:49 GMT'}, 'RetryAttempts': 0}}  # noqa
MESSAGE = 'TESTMESSAGE'
EVENT_ID = 'SomeEventID'
STACK_EVENTS = {'StackEvents': [{'StackId': 'arn:aws:cloudformation:eu-central-1:420759548424:stack/teststack/a29eaa70-e7ab-11e6-aada-503f2ad2e536', 'EventId': '7e7e22e0-ec85-11e6-a72f-50a68a770ce6', 'StackName': 'teststack', 'LogicalResourceId': 'teststack', 'PhysicalResourceId': 'arn:aws:cloudformation:eu-central-1:420759548424:stack/teststack/a29eaa70-e7ab-11e6-aada-503f2ad2e536', 'ResourceType': 'AWS::CloudFormation::Stack', 'Timestamp': datetime.datetime(2017, 2, 6, 16, 1, 17, 611000, tzinfo=tzlocal()), 'ResourceStatus': 'UPDATE_COMPLETE', "ResourceStatusReason": "Resource creation Initiated"}, {'StackId': 'arn:aws:cloudformation:eu-central-1:420759548424:stack/teststack/a29eaa70-e7ab-11e6-aada-503f2ad2e536', 'EventId': 'DeploymentBucket14-bc35d70a-3df5-45d4-afaa-c06b536a50cd', 'StackName': 'teststack', 'LogicalResourceId': 'DeploymentBucket14', 'PhysicalResourceId': 'teststack-deploymentbucket14-1r1yxsi27kclv', 'ResourceType': 'AWS::S3::Bucket', 'Timestamp': datetime.datetime(2017, 2, 6, 16, 1, 16, 976000), 'ResourceStatus': 'DELETE_COMPLETE'}, {'StackId': 'arn:aws:cloudformation:eu-central-1:420759548424:stack/teststack/a29eaa70-e7ab-11e6-aada-503f2ad2e536', 'EventId': 'DeploymentBucket18-f9a5ef79-307a-4919-a293-b74be40e19b2', 'StackName': 'teststack', 'LogicalResourceId': 'DeploymentBucket18', 'PhysicalResourceId': 'teststack-deploymentbucket18-iy7lt61peqvp', 'ResourceType': 'AWS::S3::Bucket', 'Timestamp': datetime.datetime(2017, 2, 6, 16, 1, 16, 868000), 'ResourceStatus': 'DELETE_COMPLETE'}, {'StackId': 'arn:aws:cloudformation:eu-central-1:420759548424:stack/teststack/a29eaa70-e7ab-11e6-aada-503f2ad2e536', 'EventId': 'DeploymentBucket3-7c92066b-c2e7-427a-ab29-53b928925473', 'StackName': 'teststack', 'LogicalResourceId': 'DeploymentBucket3', 'PhysicalResourceId': 'teststack-deploymentbucket3-51e2v1veq7go', 'ResourceType': 'AWS::S3::Bucket', 'Timestamp': datetime.datetime(2017, 2, 6, 16, 1, 16, 852000), 'ResourceStatus': 'DELETE_COMPLETE'}, {'StackId': 'arn:aws:cloudformation:eu-central-1:420759548424:stack/teststack/a29eaa70-e7ab-11e6-aada-503f2ad2e536', 'EventId': 'DeploymentBucket15-4ce4845e-f072-4d69-9aae-d2e8105dc0a8', 'StackName': 'teststack', 'LogicalResourceId': 'DeploymentBucket15', 'PhysicalResourceId': 'teststack-deploymentbucket15-2tdubysims21', 'ResourceType': 'AWS::S3::Bucket', 'Timestamp': datetime.datetime(2017, 2, 6, 16, 1, 16, 712000), 'ResourceStatus': 'DELETE_COMPLETE'}]}  # noqa