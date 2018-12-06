
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
			sum = 0
			for e in entries:
				m = manhattan(e, [x, y])
				sum += m
			grid[x][y] = sum

	for r in grid:
		print([c for c in r])

	counts = [c for r in grid for c in r]
	print(len([i for i in counts if i < 10000]))

