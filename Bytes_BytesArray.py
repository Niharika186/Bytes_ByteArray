'''Bytes are immutable,modifications can't be done'''

# a=b'niharika'
# print(a,type(a)) # b'niharika' bytes
# a=B'niharika'
# print(a,type(a)) # b'niharika' bytes

'''converting bytes to list,tuple,set'''
# a=b'niharika'
# print(list(a)) # [110, 105, 104, 97, 114, 105, 107, 97]
# print(tuple(a)) # (110, 105, 104, 97, 114, 105, 107, 97)
# print(set(a)) # {97, 104, 105, 107, 110, 114}

'''it will take ASCII values'''
# a=b'sahi,th,ya'
# print(list(a)) # [115, 97, 104, 105, 44, 116, 104, 44, 121, 97]
# print(tuple(a)) # (115, 97, 104, 105, 44, 116, 104, 44, 121, 97)
# print(set(a)) # {97, 104, 105, 44, 115, 116, 121}

# print(chr(90)) # Z
# print(ord(',')) # 44
# print(ord('a')) # 97

'''Modification can't be done'''
# a=b'python'
# a[0]='n' # TypeError: 'bytes' object does not support item assignment


'''ByteArray is mutable,modifications are done'''
# a=bytearray(b'python')
# print(a,type(a)) # bytearray(b'python')  bytearray
# a[0]=90
# print(a) # Zython