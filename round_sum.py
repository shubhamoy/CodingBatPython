def round10(num):
	r = num % 10
	if r >= 5:
		num += (10-r)
	elif r < 5:
		num -= r
	return num

def round_sum(a, b, c):
	return round10(a)+round10(b)+round10(c)
