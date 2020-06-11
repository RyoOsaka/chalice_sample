CREATE TABLE employee(
    employee_id NOT NULL BIGINT(20) COMMENT '社員ID',
    first_name NOT VARCHAR(20) COMMENT '名字',
    last_name NOT VARCHAR(20) COMMENT '名前',
    mail NOT NULL VARCHAR(50) COMMENT 'メールアドレス',
    PRIMARY KEY(employee_id)
) ENGINE = InnoDB DEFAULT CHARSET = utf8 COMMENT = '社員'
