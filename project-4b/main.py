from dateutil import parser
def get_overlapped(entries):
	guards = {}

	sleep_minute = 0
	is_sleeping = False
	cur_id = ""
	while len(entries) > 0:
		entry = entries.pop()
		if entry[2] == 0:
			sleep_minute = 0
			cur_id = entry[1]
		elif entry[2] == 1:  # Fall Asleep
			is_sleeping = True
			sleep_minute = entry[0]
		elif entry[2] == 2:  # Wake Up
			is_sleeping = False
			guard_stats = guards.get(cur_id, [0]*60)
			for m in range(sleep_minute, entry[0]):
				guard_stats[m] += 1
			guards[cur_id] = guard_stats
			sleep_minute = 0
	sleepiest = 0
	for guard in guards.keys():
		sleep = sum(guards[guard])
		if sleep > sleepiest:
			print(guard)
			print(sum(guards[guard]))
			print(guards[guard].index(max(guards[guard])))
			sleepiest = sleep


with open('input.txt','r') as f:
	lines = f.readlines()
	entries = []
	for line in lines:
		a = int(line[line.index(":")+1:line.index("]")])
		temp = line[line.index("#") + 1:] if "#" in line else ""
		b = temp[:temp.index(" ")] if "#" in line else ""
		c = 0 if "begins shift" in line else 1 if "falls asleep" in line else 2
		d = parser.parse(line[line.index("[") + 1 : line.index("]")])
		entries.append((a, b, c, d))
	entries = sorted(entries, key=lambda x: x[3])[::-1]
	get_overlapped(entries)

# 9271