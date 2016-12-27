# program to solve the tower of hanoi problem
# a pole of 64 disks needs to be transferred to another pole
# total 3 poles are given, two are initially empty
# each pole is a stack

from stacks import Stack

# populating p1 with numbers 1-64; each number represents the 'size' of the disk
# the task is to arrange the 64 disks, with 1 at the top and 64 at the bottom, to another pole (p2 or p3)


# Algorithm: If I know how to transfer 63 disks to another pole, I can transfer the 64th to the other one
# and arrange the 63 on top of it. To transfer 63 disks, I can do the same with 62 disks and so on. 
# The base case is transferring 1 disk to another pole

def arrange_hanoi(p1, p2, p3, disks):
	if disks == 1:
		print disks
		return(p1, p2, p3, disks)
	else:
		if disks % 2 == 0: # even number of disks implies a recursive call and then pop from p1 and push into p3
			print disks
			p2.push(arrange_hanoi(p1, p2, p3, disks - 1))
			p3.push(p1.pop())
			return(p1, p2, p3, disks)
		else: # odd number of disks
			print disks
			p1.push(arrange_hanoi(p1, p2, p3, disks - 1))
			p3.push(p2.pop())
			return(p1, p2, p3, disks)

def main():
	p1 = Stack() 
	p2 = Stack()
	p3 = Stack()
	num_disks = 6

	for disk in range(num_disks):
		p1.push(num_disks - disk)

	arrange_hanoi(p1, p2, p3, num_disks)
	print(p1.length(), p2.length(), p3.length())

main()


