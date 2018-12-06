
def manhattan(p1, p2):
	d_x = abs(p1[0] - p2[0])
	d_y = abs(p1[1] - p2[1])
	return d_x + d_y

with open('input.txt','r') as f:
	lines = f.readlines()
	entries = []
	for line in lines:
		entries.append([int(i) for i in line.split(", ")][::-1])

	max_x = max([p[0] for p in entries]) + 1
	min_x = 0
	max_y = max([p[1] for p in entries]) + 1
	min_y = 0
	grid = [[(float("inf"), None) for c in range(min_x, max_x + 1)] for r in range(min_y, max_y + 1)]

	for x, r in enumerate(grid):
		for y, c in enumerate(r):
			closest = (float("inf"), None)
			for e in entries:
				m = manhattan(e, [x, y])
				if m < closest[0]:
					closest = (m, e)
				if m == closest[0] and not (e[0] == closest[1][0] and e[1] == closest[1][1]):
					closest = (m, [None, None])
			grid[x][y] = closest

	entries.append([None, None])
	counts = {}
	boundaries = [entries.index(c[1]) for c in grid[0]] + \
				 [entries.index(c[1]) for c in grid[-1]]+ \
				 [entries.index(r[-1][1]) for r in grid]+ \
				 [entries.index(r[-1][1]) for r in grid]
	for r in grid:
		print([c[0] for c in r])
	print("\n")
	for r in grid:
		print([entries.index(c[1]) for c in r])

	c_e = [entries.index(c[1]) for r in grid for c in r]

	for e in c_e:
		if not e in boundaries:
			v = counts.get(e, 0) + 1
			counts[e] = v

	print(counts)

