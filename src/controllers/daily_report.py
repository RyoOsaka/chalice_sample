# -*- coding: utf-8 -*-
from ..services import daily_report_service
from chalice import Chalice

app = Chalice(app_name='daily_report')


@app.route("/clockin", methods=['POST'])
def clockin():
    req_json = app.current_request.json_body
    req_json['clockin_time']

    return
