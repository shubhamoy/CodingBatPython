def make_chocolate(small, big, goal):
	if goal > big*5+small:
		return -1
	if goal % 5 > small:
		return -1
	r = goal - (big * 5)
	if r > 0:
		return r
	else:
		return goal%5
