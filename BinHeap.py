# defining a binary heap class as a list
# each left child is at 2p, right child at 2p+1
# priority implies that the key of parents is less than or equal to the children's key

class BinHeap():
	def __init__(self):
		self.heap_list = [0]
		self.current_size = 0

	# insert method inserts a new item to the heap at its correct position
	def insert_heap(self, item):
		self.heap_list.append(item)
		posn = len(self.heap_list) - 1
		parent_posn = posn // 2
		while self.heap_list[parent_posn] <= item and parent_posn > 0:
			temp = self.heap_list[parent_posn]
			self.heap_list[parent_posn] = item
			self.heap_list[posn] = temp
			posn = parent_posn
			parent_posn = posn // 2

	# function to percolate an element down the tree
	def perc_down(self, item):
		index = 1
		child = 2*index
		while 2*index + 1 < len(self.heap_list):
			if self.heap_list[child] < self.heap_list[index]:
				temp = self.heap_list[index]
				self.heap_list[index] = self.heap_list[child]
				self.heap_list[child] = temp
				index = child
				child = 2*index 
				
			child = child + 1

	# function to delete the min item from a heap 
	def del_min(self):
		self.heap_list[1] = self.heap_list[-1]
		self.heap_list.pop()
		perc_down(self.heap_list[1])

	

			













	# deleting the minimum element in the list


heap = BinHeap()
heap.insert_heap(4)
heap.insert_heap(15)
heap.insert_heap(5)

