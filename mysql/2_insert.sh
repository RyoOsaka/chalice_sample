mysql -uroot -ppassword --local-infile daily_report -e "LOAD DATA LOCAL INFILE '/docker-entrypoint-initdb.d/daily_report.csv' INTO TABLE daily_report FIELDS TERMINATED BY ',' ENCLOSED BY '' LINES TERMINATED BY '\n'"
mysql -uroot -ppassword --local-infile daily_report -e "LOAD DATA LOCAL INFILE '/docker-entrypoint-initdb.d/employee.csv' INTO TABLE employee FIELDS TERMINATED BY ',' ENCLOSED BY '' LINES TERMINATED BY '\n'"
mysql -uroot -ppassword --local-infile daily_report -e "LOAD DATA LOCAL INFILE '/docker-entrypoint-initdb.d/transportation_cost.csv' INTO TABLE transportation_cost FIELDS TERMINATED BY ',' ENCLOSED BY '' LINES TERMINATED BY '\n'"