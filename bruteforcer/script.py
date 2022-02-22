#flag{b1n42y_s3r2ch_f7w}

from pwn import *

io = process('./bruteforcer')

file = open('wordlist.txt', 'r')

words = file.readlines()

words.sort()
length = len(words)
start = 0
end = length
io.sendline(words[(start + end)//2])

receive = str(io.recvline())

while "WRONG" in receive:
    
    if "low" in receive:
        start = (start + end)//2
        io = process('./bruteforcer')
        io.sendline(words[(start + end)//2])
        receive = str(io.recvline())
    elif "high" in receive:
        end = (start+end)//2
        io = process('./bruteforcer')
        io.sendline(words[(start + end)//2])
        receive = str(io.recvline())


password = words[(start + end)//2]
print(password)

file.close()