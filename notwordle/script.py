#flag{pr377y_5u23_7h15_15_n07_w0rd13}

import string
from pwn import *

allowed = str(string.printable.partition("Z")[0]) + "Z" + "_"

pwd_till_now = []
for i in range(0, 30):
    pwd_till_now.append("*")

    
io = process("./notwordle")

str_conv = "".join(pwd_till_now)

io.sendline(str_conv)
receive = int(str(str(io.recvline()).partition("/")[0]).partition(":")[2])
io.close()

counter = 0


while receive != 30:
    temp = receive
    counter = 0
    while temp == receive:
        io = process("./notwordle")
        pwd_till_now[temp] = allowed[counter]
        counter += 1
        str_conv = "".join(pwd_till_now)
        io.sendline(str_conv)
        receive = int(str(str(io.recvline()).partition("/")[0]).partition(":")[2])
        io.close()

print("".join(pwd_till_now))
