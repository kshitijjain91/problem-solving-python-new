# General parentheses parser: Parses expressions (strings) with [], {} and ()
# Uses three stacks, one for each parentheses type
# 1 is (), 2 is [],  3 is {}

from stacks import Stack

s1 = Stack()
s2 = Stack()
s3 = Stack()

def gen_parentheses_parser(a_string):

	index = 0
	balanced_1 = True
	balanced_2 = True
	balanced_3 = True
	all_balanced = balanced_1 and balanced_2 and balanced_3
	
	while index < len(a_string) and all_balanced:
		symbol = a_string[index]

		if symbol == '(':
			s1.push('(')
		elif symbol == ')':
			if s1.is_empty():
				balanced_1 = False
			else:
				s1.pop()

		if symbol == '[':
			s2.push('[')
		elif symbol == ']':
			if s2.is_empty():
				balanced_2 = False
			else:
				s2.pop()

		if symbol == '{':
			s3.push('{')
		elif symbol == '}':
			if s3.is_empty():
				balanced_3 = False
			else:
				s3.pop()

		all_balanced = balanced_1 and balanced_2 and balanced_3
		index = index + 1

	if s1.is_empty() and s2.is_empty() and s3.is_empty() and balanced_1 and balanced_2 and balanced_3:
		return True
	else:
		return False

		
print(gen_parentheses_parser('((()))[]'))	
