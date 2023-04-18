from numpy import array

def Matrix(data):
	if type(data) == list:
		return ListMatrix(data)
	elif type(data) == dict:
		return IndexedMatrix(data)

class AbstractMatrix:
	def __init__(self):
		raise 1
	def __repr__(self):
		return repr(self.matrix)
	def __len__(self):
		return len(self.matrix)
	def __iter__(self):
		return iter(self.matrix)
	def __getitem__(self, arg):
		return self.matrix[arg]
	def __setitem__(self, idx, value):
		self.matrix[idx] = array(value)
	def row(self, idx):
		return self.raw[:, idx]
	def rows(self, *idx):
		return self.raw[:, idx]
	def setrow(self, idx, value):
		self.raw[:, idx] = value

class ListMatrix(AbstractMatrix):
	def __init__(self, data):
		self.raw = array(data)
		self.matrix = self.raw
	
	def indexed(self):
		return False
	
	def __str__(self):
		res = ""
		for vec in self.raw:
			res += ("\t".join([str(i) for i in vec]) + "\n")
		return res

class IndexedMatrix(AbstractMatrix):
	def __init__(self, data):
		tmpraw = list()
		keys = list()
		self.matrix = dict()
		for key in data:
			tmpraw.append(data[key])
			keys.append(key)
		self.raw = array(tmpraw)
		for i in range(len(keys)):
			self.matrix[keys[i]] = self.raw[i]
	
	def indexed(self):
		return True
	
	def __str__(self):
		res = ""
		for vec in self.matrix:
			res += (vec + "\t" + "\t".join([str(i) for i in self.matrix[vec]]) + "\n")
		return res
