import sys
frequency_analysis = {  "a" : 0,  "b" : 0,  "c" : 0,  "d" : 0,  "e" : 0 , "f" : 0,  "g" : 0,
    "h" : 0,  "i" : 0,  "j" : 0,  "k" : 0,  "l" : 0,  "m" : 0,  "n" : 0,  "o" : 0,
    "p" : 0,  "q" : 0,  "r" : 0,  "s" : 0,  "t" : 0,  "u" : 0,  "v" : 0,  "w" : 0,
    "x" : 0,  "y" : 0,  "z" : 0 }

occs = []
length = 0
alphabet = 'abcdefghijklmnopqrstuvwxyz'
ciphertext = open(sys.argv[1],"r").read()
#(ciphertext)
for letter in ciphertext:
	if letter in alphabet:
        	frequency_analysis[letter] += 1
		length += 1.0 	
for letter in alphabet:
	occs.append(100*frequency_analysis[letter]/length)

occs = zip(alphabet,occs)
freqs = sorted(occs, key = lambda x: x[1], reverse = True)
printable = ""
for l,f in freqs:
	print("{}\t{:.2f}%").format(l,f)

