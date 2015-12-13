def near_ten(num):
	return True if num % 10 <= 2 or 10 - (num % 10) <= 2 else False
