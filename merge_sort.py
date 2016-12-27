# program to implement a merge sort algorithm

def merge_sort(a_list):
	
	if len(a_list) == 1:
		return a_list

	while len(a_list) > 1:
		len_1 = len(a_list) // 2

		left_list = a_list[0:len_1]
		right_list = a_list[len_1:]

		return merge_lists(merge_sort(left_list), merge_sort(right_list))

def merge_lists(left_list, right_list):
	count_left = 0
	count_right = 0
	count_main = 0
	merged_list = [None]*(len(left_list) + len(right_list))

	while count_left < len(left_list) and count_right < len(right_list):
		if left_list[count_left] < right_list[count_right]:
			merged_list[count_main] = left_list[count_left]
			count_left = count_left + 1
			count_main = count_main + 1
		else:
			merged_list[count_main] = right_list[count_right]
			count_right = count_right + 1
			count_main = count_main + 1

		if count_left == len(left_list):
			merged_list[count_main:] = right_list[count_right:]
		if count_right == len(right_list):
			merged_list[count_main:] = left_list[count_left:]

	return merged_list

a_list = [54, 26, 93, 17, 77, 31, 44, 55, 20, 12, 3, 34, 23, 78, 17]
print(merge_sort(a_list))





