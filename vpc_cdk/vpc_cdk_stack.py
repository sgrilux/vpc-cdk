from aws_cdk import (
    core,
    aws_ec2 as ec2)


class VpcCdkStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # The code that defines your stack goes here
        vpc = ec2.Vpc(self, "TheVPC",
            cidr="10.0.0.0/16"
        )