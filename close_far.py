def close_far(a, b, c):
	r1 = a-b
	r2 = a-c
	r3 = b-c
	if abs(r1) == 1 and abs(r2) == 1:
		return False
	if abs(r1) <= 1 or abs(r2) <= 1:
		if abs(r1) <= 1:
			if abs(r3) >= 2:
				return True
			return False
		elif abs(r2) <= 1:
			if abs(r3) >= 2:
				return True
			return False
		return False
