# program to build a parentheses parser tree for parsing mathematical expressions (fully parenthesised)
# Uses stacks to store intermediate trees and BinaryTree objects to create the tree

from stacks import Stack
from BinaryTree import BinaryTree

def build_parse_tree(p_exression):
	char_list = p_expression.split()
	s = Stack()
	current_node = BinaryTree('')
	s.push(current_node)

	for char in char_list:
		if char == '(':
			current_node.insert_left('')
			s.push(current_node)
			current_node = current_node.get_left_child()
		
		# for numeric values
		elif char not in "()+-*/%":
			current_node.set_root_val(int(char))
			current_node = s.pop()

		# for operators
		elif char in "+-*/%":
			current_node.set_root_val(char)
			current_node.insert_right('')
			s.push(current_node)
			current_node = current_node.get_right_child()

		# if ')', then make the parent te current node (till there's no parent and the tree is thus complete)
		elif char == ')':
			current_node = s.pop()

		else: 
			raise ValueError

		return current_node

pt = build_parse_tree(" ( 10 + 2 ) * ( 5 - 3 ) ")






			
