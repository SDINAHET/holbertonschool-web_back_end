personal data




root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestr
e/holbertonschool-web_back_end/personal_data# cat main.sql | mysql -uroot -p
Enter password:
root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestr
e/holbertonschool-web_back_end/personal_data# echo "SELECT COUNT(*) FROM users;" | mysql -uroot -p my_db
Enter password:
COUNT(*)
2
root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestr
e/holbertonschool-web_back_end/personal_data# PERSONAL_DATA_DB_USERNAME=root PERSONAL_DATA_DB_PASSWORD=root PERSONAL_DATA_DB_HOST=localhost PERSONAL_DATA_DB_NAME=my_db ./filtered_logger.py
[HOLBERTON] user_data INFO 2025-07-23 20:05:33,887: name=***; email=***; phone=***; ssn=***; password=***; ip=60ed:c396:2ff:244:bbd0:9208:26f2:93ea; last_login=2019-11-14 06:14:24; user_agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36;
[HOLBERTON] user_data INFO 2025-07-23 20:05:33,887: name=***; email=***; phone=***; ssn=***; password=***; ip=f724:c5d1:a14d:c4c5:bae2:9457:3769:1969; last_login=2019-11-14 06:16:19; user_agent=Mozilla/5.0 (Linux; U; Android 4.1.2; de-de; GT-I9100 Build/JZO54K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30;
root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonschool-web_back_end/personal_data#
