# program to create a HashTable (Map ADT)

class HashTable():
	def __init__(self):
		self.size = 11
		self.slots = [[None]]*self.size
		self.data = [[None]]*self.size

	def put(self, key, value):
		hash_key = hash(key)
		
		if key in self.slots[hash_key]:
			for index, val in enumerate(self.slots[hash_key]):
				if val == key:
					index_found = index
					self.slots[hash_key][index_found] = key
					self.data[hash_key][index_found] = value

		else:
			self.slots[hash_key].append(key)
			self.data[hash_key].append(value)


	def get(self, key):
		hash_key = hash(key)

		if key in self.slots[hash_key]:
			for index, val in enumerate(self.slots[hash_key]):
				if val == key:
					return key, self.data[hash_key][index]

		else:
			return None

	def delete(self, key):
		hash_key = hash(key)
		for index, val in enumerate(self.slots[hash_key]):
			if val == key:
				del(key)
				del(self.data[hash_key][index])





def hash(item):
		return item % 11

def rehash(item):
	return (item % 11) + 1

dict_1 = HashTable()
dict_1.put(45, 'dog')
dict_1.put(56, 'cat')
dict_1.put(4, 'alpha')

print(dict_1.get(45))
print(dict_1.get(56))
print(dict_1.get(46))

dict_1.delete(45)
