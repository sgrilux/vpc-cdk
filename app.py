#!/usr/bin/env python3

from aws_cdk import core

from vpc_cdk.vpc_cdk_stack import VpcCdkStack


app = core.App()
VpcCdkStack(app, "vpc-cdk")

app.synth()
