"""
Sudoku is a number-placement puzzle. The objective is to fill a 9 × 9 grid with numbers in such a way that each column, 
each row, and each of the nine 3 × 3 sub-grids that compose the grid all contain all of the numbers from 1 to 9 one time.
Implement an algorithm that will check whether the given grid of numbers represents a valid Sudoku puzzle according to the layout rules described above. 
Note that the puzzle represented by grid does not have to be solvable.
"""

"""
APPROACH 

1. Write a function to check unique numbers using a set datastructure, return True if unique
otherwise return false

    Input : ["1", "2", "3", "4", "5", "6", "7", ","]
    Output: [True]

2. Check each line in the grid, if False, return False, otherwise proceed to 
next step

    Input : [["1", "2", "3", "4", "5", "6", "7", ","], 
            ["1", "2", "3", "4", "5", "6", "7", ","],
            ["1", "2", "3", "4", "5", "6", "7", ","]]

3. Check each column in the grid

    Input : [["1", "2", "3", "4", "5", "6", "7", ","], 
            ["1", "2", "3", "4", "5", "6", "7", ","],
            ["1", "2", "3", "4", "5", "6", "7", ","]]

4. Check squares within the grid.

     Input : [["1", "2", "3", "4", "5", "6", "7", ","], 
            ["1", "2", "3", "4", "5", "6", "7", ","],
            ["1", "2", "3", "4", "5", "6", "7", ","]]
"""


def check_unique(nums):
    s = set()
    for num in nums:
        if num == '.':
            continue    
        if num in s:
            return False
        s.add(num)
    return True

def solution(grid):
    for line in grid:
        if not check_unique(line):
            return False
            
    for i in range(9):
        if not check_unique([line[i] for line in grid]):
            return False
    
    for i in range(0,9,3):
        for j in range(0, 9, 3):
            if not check_unique(grid[i][j:j+3] + grid[i+1][j:j+3] + grid[i+2][j:j+3]):
                return False
                
    return True
