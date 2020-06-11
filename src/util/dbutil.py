# -*- coding: utf-8 -*-
from typing import Dict
from datetime import date


def create_query_params(params: dict) -> Dict[str, dict]:
    """クエリパラメータを rds data api 用の形式に変換する

    :param params:
    :return: rds data api 用の dict e.g. {'name': hoge, {'value': {'stringValue': 'hoge'}}}
    """
    if not params:
        return None

    ret_params = {}
    for k, v in params.items():
        if v is None:
            ret_params.update({'name': k, 'value': {'isNull': True}})
        elif type(v) is str:
            ret_params.update({'name': k, 'value': {'stringValue': v}})
        elif type(v) is int:
            ret_params.update({'name': k, 'value': {'longValue': v}})
        elif type(v) is bool:
            ret_params.update({'name': k, 'value': {'booleanValue': v}})
        elif type(v) is date:
            ret_params.update({'name': k, 'typeHint': 'DATE',
                               'value': {'doubleValue': v}})
    return ret_params


def read_query(sql_file: str) -> str:
    sql_dir = f'src/models/queries/{sql_file}'
    with open(sql_dir) as f:
        sql = f.read()
    if not sql:
        raise Exception(f'Target SQL file dir is wrong... dir: {sql_dir}')
    return sql


def execute_statement(sql_file: str, db_name: str, **params: dict) -> dict:
    """SQLファイルを読み込み、aurora の data api を実行する

    :param sql_file: 実行するSQLのファイル名
    :param params: sql file にわたすパラメータ
    :return: 実行結果
    """
    sql = read_query(sql_file)
    sql_params = create_query_params(params)
    cli = boto3.client('rds-data')
    return cli.execute_statement(
        secretArn=os.getenv('secret-arn'),
        database=db_name,
        resourceArn=os.getenv('database-arn'),
        sql=sql,
        sql_parameters=sql_params
    )
