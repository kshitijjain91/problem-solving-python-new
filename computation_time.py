import time, random
time_list = []

for iter in range(50):
	rand = random.randint(1, 10)
	t1 = time.time()
	for i in range(1000000):
		i + rand
	t_end = time.time()
	time_list.append(t_end - t1)


print(time_list)
time_list = [x/1000000 for x in time_list]
print(time_list)

s = 0
for i in range(len(time_list)):
	s = s + time_list[i]

print(s/len(time_list))
