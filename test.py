# coding=utf-8
from Xlib.ext.xinput import *


def print_bytes(bytes):
    print(", ".join(hex(v) for v in bytes))


for l in range(6):
    print_bytes(AddMasterInfo.to_binary(name="t"*l))

print()

print_bytes(RemoveMasterInfo.to_binary(deviceid=22))
print_bytes(AttachSlaveInfo.to_binary(deviceid=9, new_master=2))
print_bytes(DetachSlaveInfo.to_binary(deviceid=9))


class a(object):
    def __init__(self):
        print("init a")

class b(a):
    pass

obj = b()