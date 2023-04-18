
def remove_comments(tokens):
	res = tokens[:]
	for t in range(len(res)):
		for c in range(len(res[t])):
			if res[t][c] == '#':
				res[t] = res[t][:c].strip()
				return res[:t + 1]
	return res
