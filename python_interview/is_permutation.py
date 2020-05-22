#!/usr/bin/python3
import string
p1='madam'
p2='race car!'

def is_perm_1(p):
    p = ''.join([x for x in p if x.isalpha()]).replace(" ", "").lower()
    return p == p[::-1]

print(is_perm_1(p1))
print(is_perm_1(p2))

def is_perm_2(p):
    i = 0
    j = len(p) -1
    while i < j:
        while not p[i].isalnum() and i <j:
            i+=1
        while not p[j].isalnum() and i <j:
            j-=1
        if p[i].lower() != p[j].lower():
            return False
        i +=1
        j -=1
    return True

print(is_perm_2(p1))
print(is_perm_2(p2))