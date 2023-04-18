#!/usr/bin/python
from sys import argv
from numpy.linalg import norm
from numpy import array
from VecFile import VecFile

if __name__ != "__main__":
	quit("Misimport of main.")

if len(argv) < 3:
	quit(f"Syntax: {argv[0]} [input file] [output file]")

v = VecFile(argv[1])

if "Vectors" not in v:
	quit("No vectors to normalize.")

dim = len(v["Vectors"].raw[0])

for i in range(dim):
	row = v["Vectors"].row(i)
	avg = row.mean()
	dev = row.std()
	v["Vectors"].raw[:, i] = ((row - avg) / dev)

v.write(argv[2])
