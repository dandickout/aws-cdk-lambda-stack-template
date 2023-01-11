#!/usr/bin/env python3

import aws_cdk as cdk

from cdk_master_template.cdk_master_stack import CDKMasterStack
from aws_cdk import Environment


app = cdk.App()
CDKMasterStack(app, "cdk-master-stack", env=Environment(
        account="YOUR_ACCOUNT_ID",
        region="YOUR_REGION"
    ))

app.synth()
