#!/usr/bin/python3
def reverse_integer(num):
  result = 0
  while num !=0:
    num, rem = divmod(num, 10)
    result = result *10 + rem

  return result

print(reverse_integer(123))
