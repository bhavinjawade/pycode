class DisjointSet:

	_disjoint_set = list()

	def __init__(self, init_arr):
		self._disjoint_set = []
		if init_arr:
			for item in list(set(init_arr)):
				self._disjoint_set.append([item])

	def _find_index(self, elem):
		for item in self._disjoint_set:
			if elem in item:
				return self._disjoint_set.index(item)
		return None

	def find(self, elem):
		for item in self._disjoint_set:
			if elem in item:
				return self._disjoint_set[self._disjoint_set.index(item)]
		return None
	
	def union(self,elem1, elem2):
		index_elem1 = self._find_index(elem1)
		index_elem2 = self._find_index(elem2)
		if index_elem1 != index_elem2 and index_elem1 is not None and index_elem2 is not None:
			self._disjoint_set[index_elem2] = self._disjoint_set[index_elem2]+self._disjoint_set[index_elem1]
			del self._disjoint_set[index_elem1]
		return self._disjoint_set
		
	def get(self):
		return self._disjoint_set

if __name__=='__main__':
    test_set = DisjointSet([1,2,3,3,3,4,5,6,7,7,7,7])
	
	print test_set.get()
	
	print test_set.union(2,3)
	print test_set.union(6,7)
	
	print test_set.union(7,10)
	
	print test_set.union(2,6)