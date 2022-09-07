import sys
import re
import hashlib
f = open("log.txt", 'a')

# 0 filler
def fill_zeros(y, inpu):
    for i in range(12-len(inpu)-len(y)):
        y = "0" + y 
    return y
    
# gets and converts fc to be usable
inp = sys.argv[1]
if len(inp) >= 12:
    print("too long")
    sys.exit()
    
rangenum = 10**(12-len(inp)+1)-1
print(inp)

x = "0"

# test through all possible friend codes, print valid ones to log.txt 

for i in range(rangenum):
    
    fc = inp + fill_zeros(x, inp)
    fcint = int(fc)                      #blatantly stolen from https://gist.github.com/TobiX/0106edd801c6c9f276e1fa920d8b0fd8
    principal = fcint & 0xffffffff
    checksum = fcint >> 32

    sha1 = hashlib.sha1()
    sha1.update(principal.to_bytes(4, byteorder='little'))
    calcsum = sha1.digest()[0] >> 1

    # print(fc, fcint, principal, checksum, calcsum)
    if checksum == calcsum:
        f.write(fc)
        f.write("\n")
    x = str(int(x)+1)


