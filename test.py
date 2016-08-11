# coding=utf-8
from Xlib.ext.xinput import *


class MockDisplay(object):
    def __init__(self, major_ext):
        self.display = self
        self.major_ext = major_ext

    def get_extension_major(self, extname):
        return self.major_ext

    def send_request(self, request, onerror):
        print_bytes(request._binary)


def print_bytes(bytes):
    print(", ".join(hex(v) for v in bytes))


for l in range(6):
    print_bytes(AddMasterInfo.to_binary(name="t" * l))

print()

print_bytes(RemoveMasterInfo.to_binary(deviceid=22))
print_bytes(AttachSlaveInfo.to_binary(deviceid=9, new_master=2))
print_bytes(DetachSlaveInfo.to_binary(deviceid=9))

change_hierarchy(MockDisplay(15), {'type': RemoveMaster, 'deviceid': 22})

