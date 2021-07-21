'''
Daily Coding Problem #3

This problem was asked by Google.
Given the root to a binary tree, implement serialize(root), which serializes the tree into a string, and deserialize(s), which deserializes the string back into the tree.
For example, given the following Node class

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

The following test should pass:

node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'
'''

class Node:
	def __init__(self, val, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right

def serialize(root):
	if not root:
		return "X"
	else:
		return "{} {} {}".format(root.val, serialize(root.left), serialize(root.right))

def deserialize(data):
	nodes = iter(data.split(" "))
	
	def dNode():
		currentNode = next(nodes)
		if currentNode == "X":
			return None
		else:
			return Node(int(currentNode), dNode(), dNode())

	return dNode()



node = Node(1, Node(2, Node(3)), Node(4))

print(serialize(deserialize(serialize(node))) == serialize(node))

# >> True