#!/usr/bin/python3

def intto_str(num):
  res = ''
  while num !=0:
    num, rem = divmod(num, 10)
    res = res+ chr(ord('0')+ rem)
  return res[::-1]

print(intto_str(123))
print(type(intto_str(123)))
