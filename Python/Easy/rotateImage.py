def solution(a):
    """
    You are given an n x n 2D matrix that represents an image. 
    Rotate the image by 90 degrees (clockwise)
    """

    """
    APPROACH 1

    1. Find the length of the matrix, n,
    2. Use a list comprehension with two for loops - one for the rows, another for the columns
    3. Within these for loops 
        a[i][j] = a[n-1-j][i]
    """

    n = len(a)
    a = [[a[n-1-j][i] for j in range(n)] for i in range(n)]
    return a

"""APPROACH 2

1. First reverse the matrix
2. Find the length of the matrix, create a for loop for each row.
3. Inside this for loop, create another for loop which iterates over each element.
4. Within this loop, each element is modified in place 
    a[i][j], a[j][i] = a[j][i], a[i][j]
5 Return the modified matrix

"""


