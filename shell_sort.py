# program to do shell sort
# Idea: Divide the list into several parts, keep sorting each part using insertion sort (since that is the fastest you've got till now) 
# till there is only one list left, which is again sorted using insertion sort

# Algo: Take a_list, divide it by 2 to get count = n//2 lists to be sorted; 
# pass all n//2 lists to an insertion sort function and do count = count//2 till count is 1
# only one list is finally left

def shell_sort(a_list):
	count = len(a_list) // 2
	while count > 0:
		for start_position in range(0, count):
			gap_insertion_sort(a_list, start_position, count)

		print("The list after {0} counts is {1}".format(count, a_list))
		count = count // 2


def gap_insertion_sort(a_list, start, gap):
	for index in range(start + gap, len(a_list), gap):
		position = index
		current_val = a_list[index]

		while position > 0 and a_list[position - gap] > current_val:
			a_list[position] = a_list[position -  gap]
			position = position - gap
		a_list[position] = current_val

a_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
shell_sort(a_list)

