/* 社員関連：社員 */
CREATE TABLE IF NOT EXISTS employee (
  employee_id bigint(20) NOT NULL AUTO_INCREMENT COMMENT '社員ID',
  employee_name varchar(255) NOT NULL COMMENT '氏名',
  mail_address varchar(255) NOT NULL COMMENT 'メールアドレス',
  department varchar(255) NOT NULL COMMENT '部署',
  gender tinyint(1) NOT NULL COMMENT '性別',
  join_date date NOT NULL COMMENT '入社日',
  birthday date NOT NULL COMMENT '生年月日',
  PRIMARY KEY (employee_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='社員';

/* 日報関連：日報 */
CREATE TABLE IF NOT EXISTS daily_report (
  daily_report_id bigint(20) NOT NULL AUTO_INCREMENT COMMENT '日報ID',
  employee_id bigint(20) NOT NULL COMMENT '社員ID',
  mail_to varchar(255) NOT NULL COMMENT '宛先',
  daily_report_date date NOT NULL COMMENT '日付',
  today_task text NOT NULL COMMENT '今日のタスク',
  tomorrow_task text NOT NULL COMMENT '翌営業日のタスク',
  problem text NOT NULL COMMENT '問題・課題',
  thoughts text NOT NULL COMMENT '感想',
  others text NOT NULL COMMENT 'その他',
  PRIMARY KEY (daily_report_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='日報';

/* 日報関連：交通費 */
CREATE TABLE IF NOT EXISTS transportation_cost (
  transportation_cost_id bigint(20) NOT NULL AUTO_INCREMENT COMMENT '交通費ID',
  employee_id bigint(20) NOT NULL COMMENT '社員ID',
  daily_report_id bigint(20) NOT NULL COMMENT '日報ID',
  transportation_cost int(6) NOT NULL COMMENT '交通費',
  departure_place varchar(255) NOT NULL COMMENT '出発地',
  arrival_place varchar(255) NOT NULL COMMENT '目的地',
  transportation_type tinyint(1) NOT NULL COMMENT '交通種別',
  PRIMARY KEY (transportation_cost_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='交通費';