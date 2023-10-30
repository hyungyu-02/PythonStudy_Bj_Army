import copy
arr = [[1,2],[2,3]]
copy = copy.deepcopy(arr)
copy[0][0] = 5

a = 5
b = a
print(a, b)
b = 4
print(a, b)