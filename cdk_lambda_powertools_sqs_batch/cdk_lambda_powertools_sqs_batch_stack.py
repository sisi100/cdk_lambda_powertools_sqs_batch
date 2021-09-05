from aws_cdk import core
from aws_cdk.aws_lambda import Runtime
from aws_cdk.aws_lambda_event_sources import SqsEventSource
from aws_cdk.aws_lambda_python import PythonFunction
from aws_cdk.aws_sqs import Queue

APP_NAME = "CdkLambdaPowertoolsSqsBatch"


class CdkLambdaPowertoolsSqsBatchStack(core.Stack):
    def __init__(self, scope: core.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        queue = Queue(self, f"{APP_NAME}Queue", visibility_timeout=core.Duration.seconds(60),)

        lambda_ = PythonFunction(
            self, f"{APP_NAME}Lambda", entry="lambda_app", runtime=Runtime.PYTHON_3_8, reserved_concurrent_executions=1
        )

        lambda_.add_event_source(SqsEventSource(queue, max_batching_window=core.Duration.seconds(10)))
