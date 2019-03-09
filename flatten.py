'''
    File: Recursive flatten function
    Author: N. Parsons
    Copyright: N. Parsons (C) 2019
'''
def flatten(arr): # flattnes an n-dimensional list
    if type(arr) is not list:
       return [arr]
    else:
        if(len(arr) > 1):
            return flatten(arr[0]) + flatten(arr[1:])
        else:
            return flatten(arr[0])

a = [[1, 2, [3, 4]], [5, 6], 7, [8, [9, [10, [11, [12, [13, 14, [[[15], 16]]]]]]]]]
print(flatten(a)) # output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 13, 14, 15, 16]
