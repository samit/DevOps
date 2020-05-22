#!/usr/bin/python3
s1 = "poor girl"
s2 = "roop lrig"

def is_anagram(s1, s2):
    ht = dict()
    for i in s1:
        if i in ht:
            ht[i]+=1
        else:
            ht[i]=1
    for i in s2:
        if i in ht:
            ht[i]-=1
        else:
            ht[i]=1
    for i in ht:
        if ht[i] !=0:
            return False
    return True

print(is_anagram(s1,s2))