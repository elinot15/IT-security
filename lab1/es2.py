encrypted= open('crypt.txt' , 'r').read()
key= open('key.txt' , 'r').read()

key=key.encode()
encrypted=encrypted.encode()
decrypted=bytearray()

for (k,val) in zip (key, encrypted):
	decrypted.append(k^val)
	
decrypted.decode()
