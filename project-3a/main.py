
def get_overlapped(claims):
	grid = {}
	for claim in claims:
		for r in range(claim[1], claim[1] + claim[3]):
			for c in range(claim[2], claim[2] + claim[4]):
				grid[(r, c)] = grid.get((r, c), 0) + 1
	print(len([v for v in grid.values() if v >= 2]))

with open('input.txt','r') as f:
	lines = f.readlines()
	claims = []
	for line in lines:
		claimId = line[1:line.index(" ")]
		claimX = int(line[line.index("@") + 2: line.index(",")])
		claimY = int(line[line.index(",") + 1: line.index(":")])
		claimWidth = int(line[line.index(":") + 2: line.index("x")])
		claimHeight = int(line[line.index("x")+1: -1])
		claims.append((claimId, claimX, claimY, claimWidth, claimHeight))
	get_overlapped(claims)

# 9271