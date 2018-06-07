#Recursive flatten function
This function provides a way of flattening an array/list for n-dimensions

This is my way of approaching this problem, so it may not be the most efficient or best approach!

How the flatten function works:
a = [0, [1, [2]], 3] ---> needs to be: [0, 1, 2, 3]
base case: let x = the array segment, if x is not a list, return [x]
Recursive statement: flatten(a[0]) + flatten(a[1:])
flatten(a) = flatten(0) + flatten([[1, [2]], 3])
flatten([0]) = [0]
flatten(a) = [0] + flatten([[1, [2]], 3])
flatten([[1, [2]], 3]) = flatten([[1, [2]]) + flatten([3])
flatten([3]) = flatten(3) + (nothing)
flatten(3) = [3]
flatten([[1, [2]], 3]) = flatten([[1, [2]]) + [3]
flatten([[1, [2]]) = flatten([1, [2]]) (+ flatten([]) =   )
flatten([]) =    (nothing)
flatten([[1, [2]]) = flatten([1, [2]])
flatten([1, [2]]) = flatten(1) + flatten([2])
flatten(1) = [1]
flatten([2]) = flatten(2)
flatten(2) = [2]
- Working back up (subbing in)
flatten([1, [2]]) = [1] + [2] = [1, 2]
flatten([[1, [2]]) = [1, 2]
flatten([[1, [2]], 3]) = [1, 2] + [3] = [1, 2, 3]
flatten([0, [1, [2]], 3]) = [0] + [1, 2, 3] = [0, 1, 2, 3, 4]
