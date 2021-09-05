#!/usr/bin/env python3

from aws_cdk import core

from cdk_lambda_powertools_sqs_batch.cdk_lambda_powertools_sqs_batch_stack import CdkLambdaPowertoolsSqsBatchStack

app = core.App()
CdkLambdaPowertoolsSqsBatchStack(app, "cdk-lambda-powertools-sqs-batch")

app.synth()
