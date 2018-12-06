
def get_length(polymer):
	stack = []

	for c in polymer:
		if len(stack) > 0 and stack[-1] == (c.lower() if c.isupper() else c.upper()):
			stack.pop()
		else:
			stack.append(c)

	return len(stack) - 1


with open('input.txt','r') as f:
	lines = f.readlines()
	polymer = lines[0]
	for i in range(0, 26):
		c = str(chr(i + 65))
		print(c + ": " + str(get_length([p for p in polymer if not p in [c, c.lower()]])))
