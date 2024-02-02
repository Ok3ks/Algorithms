"""Given a string s consisting of small English letters, find and return the first instance of a non-repeating character in it.
If there is no such character, return '_'."""

def solution(s):
    
    freq = {}
    for i in s:
        freq[i] = freq.get(i, 0) + 1
    
    for j in s:
        if freq[j] == 1:
            return j
  
    return '_'