#!/usr/bin/python3
s= "samit"

def reverse_str(s):
    a = list()
    for i in range(len(s)):
        a.append(s[i])
    print(a)
    res=''
    while len(a) !=0:
        res+=a.pop()
    return res
    
print(reverse_str(s))