# program to compare sort times of various sort functions
from bubble_sort import bubble_sort
from selection_sort import selection_sort
from insertion_sort_1 import insertion_sort_1
from insertion_sort import insertion_sort
from merge_sort import merge_sort, merge_lists
import random, time

num_list = [0]
l = 1000
for i in range(l):
	num_list.append(random.randrange(1, 100))

t0 = time.time()
bubble_sort(num_list)
t_bubble = time.time() 
selection_sort(num_list)
t_selection = time.time()
insertion_sort_1(num_list)
t_insertion_1 = time.time() 
insertion_sort(num_list)
t_insertion = time.time() 
merge_sort(num_list)
t_merge = time.time()

print("bubble", t_bubble - t0, "selection", t_selection - t_bubble, 
	"insertion_1", t_insertion_1 - t_selection, "insertion", t_insertion - t_insertion_1, "merge", t_merge - t_insertion)


