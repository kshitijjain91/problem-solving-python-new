import random


def selection_sort(num_list):
	for num_pass in range(len(num_list) - 1, 0, -1):
		largest = num_list[0]
		for i in range(num_pass):
			if num_list[i+1] > largest:
				largest = num_list[i+1]
		num_list[num_pass] = largest
	return num_list





num_list = [0]
l = 10
for i in range(l):
	num_list.append(random.randrange(1, 100))

print(selection_sort(num_list))