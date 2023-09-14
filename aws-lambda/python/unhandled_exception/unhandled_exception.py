import sentry_sdk
from sentry_sdk.integrations.aws_lambda import AwsLambdaIntegration

sentry_sdk.init(
    dsn="<your DSN>",
    integrations=[AwsLambdaIntegration()],
    traces_sample_rate=1.0
)

def lambda_handler(event, context):
    """Lambda function which does a division by zero operation

    Args:
        event (dict): Parameter to pass in event data to the handler.
        context (bootstrap.LambdaContext): Parameter to provide runtime information to the handler.

    Returns:
        json: A simple json object with two keys and corresponding values
    """
    try:
        division_by_zero = 4/0
    except Exception as e:
        sentry_sdk.capture_exception(e)
        return {
            'status_code': 500,
            'body': 'An error occurred'
        }
    return {
        'status_code': 200,
        'body': division_by_zero
    }