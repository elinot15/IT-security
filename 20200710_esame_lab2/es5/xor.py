import string
import sys
import itertools
from langdetect import detect

try:
	# default params
	filename = 'encrypted.txt'
	keylen = 2
	lang = ''

	# input params
	try:
		filename = sys.argv[1]
		keylen = int(sys.argv[2])
		lang = sys.argv[3]
	except:
		print("Not all params are defined: using default ones where not specified!")	
	
	# setup 
	ciphertext = open(filename,"r").read()
	keyDomain = string.ascii_uppercase #+string.ascii_lowercase 
	ptDomain = string.ascii_letters+'.:,;!?\'\"\n\t ' #+string.whitespace #+string.punctuation #+string.printable #for more admissible output chars 
	allKeys = list(itertools.product(keyDomain,repeat=keylen))
	output = ""
	
	# progress animation setup
	keyNum = len(allKeys)
	i = 1
	loading = '|/-\\'
	speed = 7 # 0 is the highest
	
	# Xoring all keys
	for key in allKeys:
		# progress animation
		percent = 100*i/keyNum
		sys.stdout.write("\r{} Progress: {}% ".format(loading[i/pow(2,speed)%4],percent))
		sys.stdout.flush()
		
		# key & plaintext setup
		key="".join(key)
		fullkey=""
		plaintext=""
		
		# extending key to cyphertext length by repeating it
		while( len(fullkey) < len(ciphertext) ): 
			fullkey+=key
			
		# actual XOR
		for w, k in zip(ciphertext,fullkey):
			xored = chr(ord(w)^ord(k))
			# filter plaintexts to the ones in ptDomain
			if( xored in ptDomain ):
				plaintext+= xored
			else:
				break
		# filter plaintexts to defined language ones
		if(len(plaintext)==len(ciphertext)):
			l = detect(plaintext)
			if(l==lang or lang==''):
				print("\nLang: {}\t -\tKey: {} \nPlaintext:\n{}".format(l,key,plaintext))
		i+=1
	print
except KeyboardInterrupt:
	print('\n...interrupted')
