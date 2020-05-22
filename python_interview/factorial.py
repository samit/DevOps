#!/usr/bin/python3
def get_fact(num):
  if num <=1:
    return 1
  else:
   return num * get_fact(num-1)

print(get_fact(5))
