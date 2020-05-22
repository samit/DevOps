#!/usr/bin/python

def generate_fibo(num):
  if num == 0:
    return 0
  if num ==1:
    return 1
  else:
    return generate_fibo(num -1)+ generate_fibo(num -2)


for i in range(0,10):
  print(generate_fibo(i))
