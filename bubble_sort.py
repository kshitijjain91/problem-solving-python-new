# simple bubble sort algorithm

import time, random, turtle, matplotlib.pyplot as plt 

l_list = []
time_list = []

def bubble_sort(num_list):
	t1 = time.time()
	for num_pass in range(len(num_list) - 1, 0, -1):
		for i in range(num_pass):
			if num_list[i+1] < num_list[i]:
				temp = num_list[i+1]
				num_list[i+1] = num_list[i]
				num_list[i] = temp
	t2 = time.time()
	return num_list, t2-t1



num_list = [0]
l = 10
for i in range(l):
	num_list.append(num_list[i] + random.randrange(1, 100))

sorted = bubble_sort(num_list)
print(bubble_sort(num_list))
time_list.append(sorted[1])
l_list.append(l)

plt.plot(l_list, time_list)
