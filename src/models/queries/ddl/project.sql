CREATE TABLE project(
    project_id NOT NULL BIGINT(20) COMMENT 'プロジェクトID',
    employee_id NOT NULL BIGINT(20) COMMENT '社員ID',
    project_name NOT NULL BIGINT(20) COMMENT 'プロジェクト名',
    PRIMARY KEY(project_id, employee_id)
) ENGINE = InnoDB DEFAULT CHARSET = utf8 COMMENT = 'プロジェクト'
