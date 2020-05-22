#!/usr/bin/python3
def str_to_int(st):
  res = 0
  i = 0
  for i in st:
    res= res*10+(ord(i)-ord('0'))

  return res

print(str_to_int('123'))
print(type(str_to_int('123')))
