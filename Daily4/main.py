'''
Daily Coding Problem #4

This problem was asked by Stripe.

Given an array of integers, find the first missing positive integer in linear time and constant space. In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.
For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.
You can modify the input array in-place.
'''

# O(N)
def lowestInt(arr):
	lowest = min(arr)
	highest = max(arr)

	for i in range(lowest, highest):
		if i not in arr and i > 0:
			return i

	return highest+1 if highest+1 > 0 else 1

print(lowestInt([3, 4, -1, 1]))
# >> 2
print(lowestInt([1, 2, 0]))
# >> 3