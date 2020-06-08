from typing import Dict
import sys
sys.path.append('../')
from util.dbutil import execute_statement
from datetime import date


def find_by_date(year: int, month: int, day: int) -> Dict:

    res = execute_statement(sql_file='daily_report/find_by_date.sql',
                            db_name='daily_report',
                            report_date=date(year, month, day))
    return res


if __name__ == "__main__":
    print(find_by_date(2020, 10, 1))

