#initializing a binary tree with root element r
def binary_tree(r):
	return [r, [], []]

#insert a subtree to the left of a root list given by root = [r, [], []]
#if a list is already present as the left subtree, it should be made the child of the new subtree being added
def insert_left(root, new_branch):
	t = root.pop(1)
	if len(t) > 1:
		root.insert(1, [new_branch, t, []])
	else:
		root.insert(1, [new_branch, [], []])
	return root

#inserting a subtree to the right
def insert_right(root, new_branch):
	t = root.pop(2)
	if len(t) > 1:
		root.insert(2, [new_branch, [], t])
	else:
		root.insert(2, [new_branch, [], []])
	return root

def get_root_val(root):
	return root[0]

def set_root_val(root, new_val):
	root[0] = new_val

def get_left_child(root):
	return root[1]

def get_right_child(root):
	return root[2]



tree = binary_tree("root_one")
print(tree)

tree = insert_left(tree, "root two")
print(tree)

tree = insert_right(tree, "root three")
print(tree)