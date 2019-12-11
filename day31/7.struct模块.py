import struct
ret = struct.pack('i',1023800976)
print(ret,len(ret))
num = struct.unpack('i',ret)
print(num[0])
