# algorithm to insert a number m in a sorted list of size n
def insert_num(sorted_list, m):
	start = 0
	end = len(sorted_list)
	mid = (start + end) // 2
	while (end - start) > 1:
		mid = (start + end) // 2
		if m > sorted_list[mid]:
			start = mid
		else:
			end = mid
	sorted_list.insert(end, m)

	return sorted_list

 
list1 = [2, 13, 14, 8, 37, 46, 12]

def insertion_sort_1(num_list):
	temp_list = [num_list[0]]
	for i in range(len(num_list) - 1):
		print(temp_list)
		temp_list = insert_num(temp_list, num_list[i+1])
		

	return temp_list

print(insert_num([2], 31))
print(insertion_sort_1(list1))
