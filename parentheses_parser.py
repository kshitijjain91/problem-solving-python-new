# the program checks whether each opening parenthesis has a corresponding closing one 
# using stacks. 

from stacks import Stack 

def parentheses_parser(a_string):
	
	s = Stack()

	index = 0
	balanced = True

	while index < len(a_string) and balanced:
		symbol = a_string[index]

		if symbol == '(':
			s.push('(')
		else:
			if s.is_empty():
				balanced = False
			else:
				s.pop()

		index = index + 1

	if balanced and s.is_empty():
			return True
	else:
		return False, balanced

print(parentheses_parser('()))'))

