#! /usr/bin/python
from sys import argv
from numpy.linalg import norm
from numpy import array
from VecFile import VecFile

if __name__ != "__main__":
	quit("Misimport of main.")

if len(argv) < 2:
	quit(f"Syntax: {argv[0]} [filename]")

v = VecFile(argv[1])

if "Centroids" not in v:
	quit("No centroids.")
if "Vectors" not in v:
	quit("No vectors.")

k = len(v["Centroids"])
dim = len(v["Centroids"][0])

# k empty groups
keg = lambda k: [list() for _ in range(k)] 
kgroups = None

for _ in range(50):
	kgroups = keg(k)
	for i in v["Vectors"]:
		dist = list()
		for centroid in v["Centroids"]:
			dist.append(norm(v["Vectors"][i] - centroid))
		min_dist = min(range(len(dist)), key=lambda i:dist[i])
		kgroups[min_dist].append(i)
	for c in range(k):
		try:
			v["Centroids"][c] = (sum(v["Vectors"][i] for i in kgroups[c]) / len(kgroups[c]))
		except ZeroDivisionError:
			quit(f"Bad Centroid detected. Centroids:\n{str(v['Centroids'])}")

for i, item in enumerate(kgroups):
	tmp = "\n- ".join(item)
	print(f"Group {i + 1}:\n- {tmp}")
	print(f"{v['Centroids'][i]}\n")
