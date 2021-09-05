import json

from aws_lambda_powertools.utilities.batch import sqs_batch_processor


def record_handler(record):
    print(f"メッセージ毎の処理するよ！{json.dumps(record['body'])}")
    if int(record["body"].replace("hoge", "")) % 2:
        # 奇数なら例外を出す
        print(f"例外だ！！{json.dumps(record['body'])}")
        raise
    return


@sqs_batch_processor(record_handler=record_handler)
def handler(event, context):
    print(f"ハンドラーだよ!{json.dumps([x['body'] for x in event['Records']])}")
    return {"statusCode": 200}
