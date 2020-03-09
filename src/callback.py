# -*- coding: utf-8 -*-
import json

from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.auth.credentials import StsTokenCredential
from aliyunsdkfnf.request.v20190315.ReportTaskSucceededRequest import ReportTaskSucceededRequest


def handler(environ, start_response):
    # Get request body
    try:
        request_body_size = int(environ.get('CONTENT_LENGTH', 0))
    except ValueError:
        request_body_size = 0
    request_body = environ['wsgi.input'].read(request_body_size)
    print('Request body: {}'.format(request_body))

    body = json.loads(request_body)
    message_body_str = body['Message']

    # Read MessageBody and TaskToken from message body
    message_body = json.loads(message_body_str)
    task_token = message_body['taskToken']
    ori_message_body = message_body['messageBody']
    print('Task token: {}\norigin message body: {}'.format(task_token, ori_message_body))

    # Init fnf client use sts token
    context = environ['fc.context']
    creds = context.credentials
    sts_creds = StsTokenCredential(creds.access_key_id, creds.access_key_secret, creds.security_token)
    fnf_client = AcsClient(credential=sts_creds, region_id=context.region)

    # Report task succeeded to serverless workflow
    req = ReportTaskSucceededRequest()
    req.set_TaskToken(task_token)
    req.set_Output('{"status": "success"}')
    resp = fnf_client.do_action_with_exception(req)
    print('Report task response: {}'.format(resp))

    # Response to http request
    status = '200 OK'
    response_headers = [('Content-type', 'text/plain')]
    start_response(status, response_headers)
    return [b'OK']
