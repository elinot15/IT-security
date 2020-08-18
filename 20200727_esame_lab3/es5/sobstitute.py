import sys
# sobtitute = 'SPQROTUVZABCDEFGHIStLMwxyN'
sobstitute = sys.argv[2]
alphabet =   'abcdefghijklmnopqrstuvwxyz'
ciphertext = open(sys.argv[1],"r").read()
for l,s in zip(alphabet,sobstitute):
	ciphertext=ciphertext.replace(l,s)
print(ciphertext)
