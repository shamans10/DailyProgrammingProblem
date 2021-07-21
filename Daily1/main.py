'''
Daily Coding Problem #1

This problem was recently asked by Google.
Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
Bonus: Can you do this in one pass?
'''

# O(N)
def addsTo(lst, k):
	nums = []
	for i in lst:
		if k - i in nums:
			return True
		nums.append(i)
	return False

print(addsTo([2,3,5,7], 10))

