from typing import Dict
from datetime import date
from ..util.dbutil import execute_statement


def find_by_date(year: int, month: int, day: int) -> Dict:

    res = execute_statement(sql_file='daily_report/find_by_date.sql',
                            db_name='daily_report',
                            )
    return res


if __name__ == "__main__":
    print(find_by_date(2020, 10, 1))
