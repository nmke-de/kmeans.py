from numpy import array
from Matrix import *
from remove_comments import remove_comments

class VecFile:
	def __init__(self, filename):
		self.filename = filename
		self._matrices = dict()
		self.read()
	def __enter__(self):
		return self
	def __getitem__(self, arg):
		return (self._matrices[arg])
	def __iter__(self):
		return iter(self._matrices)
	def matrices(self):
		return [matrixname for matrixname in self._matrices]
	def read(self):
		file = open(self.filename)
		matrixname = None
		tmpmatrix = None
		for line in file:
			tokens = remove_comments(line.split('\t'))
			tokens[0] = tokens[0].strip()
			if tokens == [""]:
				continue
			if len(tokens) == 1 and tokens[0][-1] == ':':
				# Store read in matrix before proceeding
				if matrixname and tmpmatrix:
					self._matrices[matrixname] = Matrix(tmpmatrix)
				# Create new matrixname and tmpmatrix
				indexed = False
				if tokens[0][-2] == '*':
					matrixname = tokens[0][:-2]
					indexed = True
				else:
					matrixname = tokens[0][:-1]
				if indexed:
					tmpmatrix = dict()
				else:
					tmpmatrix = list()
				continue
			if indexed:
				li = list()
				for i in tokens[1:]:
					li.append(float(i))
				tmpmatrix[tokens[0]] = li
			else:
				li = list()
				for i in tokens:
					li.append(float(i))
				tmpmatrix.append(li)
		# Store last matrix
		if matrixname and tmpmatrix:
			self._matrices[matrixname] = Matrix(tmpmatrix)
		file.close()
	def write(self, filename):
		file = open(filename, "w")
		file.write(f"# Generated VecFile {filename}")
		for mat in self._matrices:
			file.write("\n")
			if self._matrices[mat].indexed():
				file.write(mat + "*:\n")
			else:
				file.write(mat + ":\n")
			file.write(str(self._matrices[mat]))
		file.close()
