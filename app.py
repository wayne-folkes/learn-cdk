#!/usr/bin/env python3

from aws_cdk import core

from dynamo_cdk.dynamo_cdk_stack import DynamoCdkStack


app = core.App()
DynamoCdkStack(app, "dynamo-cdk")

app.synth()
