# simple binary search program to find the index of a number in a sorted list
import random

num_list = [0]
l = 10000
for i in range(l):
	num_list.append(num_list[i] + random.randrange(1, 100))

def binary_search(num_list, item):
	found = False
	start = 0
	end = len(num_list)
	while (end - start) > 1 and not found:
		mid =  (start + end) // 2
		if item > num_list[mid]:
			start = mid
		elif item < num_list[mid]:
			end = mid
		else:
			found = True
			return mid

	return found

print(binary_search([1, 3, 5, 7, 12, 23, 56, 89], 80))
print(binary_search(num_list, 482801))