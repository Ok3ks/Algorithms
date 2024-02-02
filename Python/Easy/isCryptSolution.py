"""
A cryptarithm is a mathematical puzzle for which the goal is to find the correspondence between letters and digits, 
such that the given arithmetic equation consisting of letters holds true when the letters are converted to digits.

You have an array of strings crypt, the cryptarithm, and an an array containing the mapping of letters and digits, solution.
The array crypt will contain three non-empty strings that follow the structure: [word1, word2, word3], which should be interpreted as the word1 + word2 = word3 cryptarithm.

If crypt, when it is decoded by replacing all of the letters in the cryptarithm with digits using the mapping in solution, becomes a valid arithmetic equation containing no numbers with leading zeroes, 
the answer is true.If it does not become a valid arithmetic solution, the answer is false.

"""

def solution(crypt, solution):
    
    lookup = {}
    for a in solution:
        lookup[a[0]] = a[-1]
        
    crypt = ["".join([str(lookup[i]) for i in word]) for word in crypt]
    int_crypt = [int(word) for word in crypt]
    
    if crypt[-1][0] =='0':
        if len(crypt[-1]) == 1:
            return True
        
    elif int_crypt[-1] == sum(int_crypt[:-1]) and (crypt[0][0] and crypt[1][0]) != '0' and crypt[-1] !='0':
        return True
        
    return False

"""
APPROACH

1. Create a lookup table, with a dictionary to map letter to respective integers
    
    Input : [(b,"1"), (a,"2"), (c, "3"), (d,"4"), (e,"5")]
    Output: {a:2, c:3, b:1, d:4}

2. Use the lookup table to convert each word in crypt to a list of integers

    Input: ["maze", "base", "cat"]
    Output: ["1040", "1050", "1089"]

3. Converts the list of strings to list of integers.

    Input: ["1040", "1050", "1089"]
    Output: [1040, 1050, 1089]

4. Checks if this conversion is a valid solution based on certain conditions

    Input: [1040, 050, 8809]
    Output: True
"""