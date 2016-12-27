# program to compare running time of 4 methods to create a list 

# method 1: concatenate
def test1():
	l = []

	for i in range(1000):
		l = l + [i]
# append
def test2():
	l  = []

	for i in range(1000):
		l.append(i)

# list comprehension
def test3():
	l = [i for i in range(1000)]

# range
def test4():
	l = list(range(1000))

# code to measure run time
import timeit
from timeit import Timer

t1 = Timer("test1()", "from __main__ import test1")
print(t1.timeit(1000))

t2 = Timer("test2()", "from __main__ import test2")
print(t2.timeit(1000))

t3 = Timer("test3()", "from __main__ import test3")
print(t3.timeit(1000))

t4 = Timer("test4()", "from __main__ import test4")
print(t4.timeit(1000))

# Note: This (timeit module's Timer object) is a good way to experiment with running times of 
# functions. 


# Experiment 2: Indexing and popping of lists
# To show that popping from the end is O(1) and that from the beginning is O(n)

# Create Timer objects
pop_zero = Timer("x.pop(0)", "from __main__ import x")
pop_end = Timer("x.pop()", "from __main__ import x")

# for length in range(100000):
x = list(range(1000000))
print(pop_zero.timeit(1000), "zero")
print(pop_end.timeit(1000), "end")

# Experiment 3: To compare the contains (in) operation in lists and dictionaries
# Hypothesis: 'in' in a list is O(n); in a dict it is O(1)

import random

for i in range(100000, 1000001, 10000):
	timer_object = Timer("random.randrange({0}) in x".format(i), "from __main__ import random, x")

	# list
	x = list(range(i))
	lst_time = timer_object.timeit(1000)

	# dict
	x = {j:None for j in range(i)}
	dict_time = timer_object.timeit(1000)

	print(i, lst_time, dict_time)

















