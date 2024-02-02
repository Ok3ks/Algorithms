""" Given an array a that contains only numbers in the range from 1 to a.length, find the first duplicate number 
for which the second occurrence has the minimal index. In other words, if there are more than 1 duplicated numbers, 
return the number for which the second occurrence has a smaller index than the second occurrence of the other number does.
If there are no such elements, return -1"""

def solution(a):
    duplicates = {}
    
    if not len(set(a)) == len(a):
        for _, i in enumerate(a):
            duplicates[i] = duplicates.get(i, 0) + 1
            if duplicates[i] > 1:
                return i    
                
    else:
        return -1

## APPROACH 2 
"""
1. For each letter in the string 


2. Find the index of this letter from the left and find the index of 
the same letter from the right.

2. Compare both, if index is the same, return the letter, otherwise return "_"
"""

def solution(s):
    for c in s:
        if s.index(c) == s.rindex(c):
            return c
    return '_'
