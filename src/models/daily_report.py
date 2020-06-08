# -*- coding: utf-8 -*-


CREATE TABLE daily_report(
    daily_report_id  NOT NULL BIGINT(20) COMMENT '日報ID',
    report_date NOT NULL DATE COMMENT '日付',
    title NOT NULL VARCHAR(20) COMMENT 'タイトル',
    start_work_time NOT NULL TIME COMMENT '作業開始時刻',
    end_work_time NOT NULL TIME COMMENT '作業終了時刻',
    today_task NOT NULL TEXT COMMENT '本日のタスク',
    tommorow_task  TEXT COMMENT '翌営業日のタスク',
    problem TEXT COMMENT '課題',
    thinking TEXT COMMENT '感想',
    PRIMARY KEY(daily_report_id)
) ENGINE = InnoDB DEFAULT CHARSET = utf8 COMMENT = '日報'
