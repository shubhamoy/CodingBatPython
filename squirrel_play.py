def squirrel_play(temp, is_summer):
	if is_summer:
		return True if temp >=60 and temp <= 100 else False
	else:
		return True if temp >= 60 and temp <=90 else False
