#!/usr/bin/python

import struct
from pwn import *
import re

# Level 1
conn = pwnlib.tubes.remote.remote("vortex.labs.overthewire.org", 5842)
s = 0
for i in range(4):
    rcv = conn.recv(4)
    i = struct.unpack("<I", rcv)
    s = s + i[0]
    # if s > 0xFFFFFFFF:
    #     s = s - 0xFFFFFFFF
    
snd = struct.pack("<I", s)

conn.send(str(snd) + "\n")
# resp: Username: vortex1 Password: xxxxxx
resp =  conn.recv()
conn.close()

print resp

# m = re.search('Username: (.*) Password: (.*)', resp)
# username, passwd =  m.group(1), m.group(2)

