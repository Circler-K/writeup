nyam=[24,20,20,24,0,0,0,0,4,12,6,30,13]
hateRuby="Ruby_is_light"
str=""
for i in range(0,13):
	str+=chr(nyam[i]^ord(hateRuby[i]))
print(str)