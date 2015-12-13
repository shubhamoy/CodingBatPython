def love6(a, b):
	if a==6 or b==6:
		return True
	c = a+b
	d = a-b
	if c == 6 or abs(d) == 6:
		return True
	return False
