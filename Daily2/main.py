'''
Daily Coding Problem #2

This problem was asked by Uber.
Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.
For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].
Follow-up: what if you can't use division?
'''

# With Division

# O(N)
def arrProduct(arr):
	product = 1
	for num in arr:
		product *= num

	return [product/x for x in arr]

print(arrProduct([1,2,3,4,5]))

# Without Division
# O(N^2)
def arrProduct(arr):
	result = []
	for i in range(len(arr)):
		tempList = arr[:i] + arr[i+1:]
		multiplier = 1
		for num in tempList: 
			multiplier *= num

		result.append(multiplier)

	return result

print(arrProduct([1,2,3,4,5]))