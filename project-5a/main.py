

with open('input.txt','r') as f:
	lines = f.readlines()
	polymer = lines[0]

	stack = []

	for c in polymer:
		if len(stack) > 0 and stack[-1] == (c.lower() if c.isupper() else c.upper()):
			stack.pop()
		else:
			stack.append(c)

	print(len(stack) - 1)
