# -*- coding: utf-8 -*-
from ..services import daily_report_service
from chalice import Chalice

import logging
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

app = Chalice(app_name='daily_report')


@app.route("/clockin", methods=['POST'])
def clockin():
    request = app.current_request

    # EventAPIのRedirectURLの認証のためchallengeフィールドの値をそのまま返す
    if "challenge" in request.json_body:
        return request.json_body["challenge"]

    slack_event = request.json_body['event']

    
    return "200 OK"

    req_json['clockin_time']
    return daily_report_service.find_by_date
    