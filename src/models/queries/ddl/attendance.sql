CREATE TABLE attendance(
    attendance_id NOT NULL BIGINT(20) COMMENT '出退勤ID',
    employee_id NOT NULL BIGINT(20) COMMENT '社員ID',
    clockin_time DATETIME COMMENT '出勤時刻',
    clockout_time DATETIME COMMENT '退勤時刻',
    PRIMARY KEY(attendance_id)
) ENGINE = InnoDB DEFAULT CHARSET = utf8 COMMENT = '出退勤'
