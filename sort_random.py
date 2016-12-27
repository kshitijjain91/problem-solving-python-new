#insertion sort algorithm

def insertion(num_list):
	for index in range(1, len(num_list)):
		position = index
		temp = num_list[index]
		while position > 0 and temp < num_list[position - 1]:
			num_list[position] = num_list[position - 1]
			position = position - 1
		num_list[position] = temp

	return num_list

l = [5, 67, 23, 41, 2, 4, 9, 34, 35, 123]
print(insertion(l))

