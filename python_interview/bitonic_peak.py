#!/usr/bin/python3
item = [1,2,3,4,5,6,7,4,3,2,1]

def find_bitonic_peak(item):
    low = 0
    high = len(item) -1
    while low <= high:
        mid = (low+high)//2
        mid_left = item[mid -1] if mid -1 > 0 else float("inf")
        mid_right = item[mid+1] if mid+1 < len(item) else float("inf")
        if mid_left < item[mid] and mid_right > item[mid]:
            low= mid+1 
        elif mid_left > item[mid] and mid_right < item[mid]:
            high = mid -1
            
        elif mid_left < item[mid] and mid_right < item[mid]:
            return item[mid]
        else:
            return None

print(find_bitonic_peak(item))
