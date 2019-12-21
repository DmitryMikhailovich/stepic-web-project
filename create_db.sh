mysql -uroot -e "create user stepic identified by 'stepic';"
mysql -uroot -e "create database stepic_web;"
mysql -uroot -e "grant all on stepic_web.* to stepic;"
