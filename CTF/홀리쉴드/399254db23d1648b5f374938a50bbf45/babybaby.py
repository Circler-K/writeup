import random

def encrypt(c):
	r=random.randrange(1, 16)
	return hex(r)[2:] + hex(ord(c)//r)[2:].rjust(2, '0') + hex(ord(c)%r)[2:]
	
f=open("flag.enc","rb")
string=f.read()
f.close()

buf = ''.join([encrypt(x) for x in string])

out=open("flag.enc", "wb")
out.write(buf.decode('hex'))
out.close()