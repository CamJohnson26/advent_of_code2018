
def get_overlapped(claims):
	grid = {}
	for claim in claims:
		for r in range(claim[1], claim[1] + claim[3]):
			for c in range(claim[2], claim[2] + claim[4]):
				grid[(r, c)] = grid.get((r, c), 0) + 1

	for claim in claims:
		is_clean = True
		for r in range(claim[1], claim[1] + claim[3]):
			for c in range(claim[2], claim[2] + claim[4]):
				if grid[(r, c)] >= 2:
					is_clean = False
		if is_clean:
			print(claim)


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