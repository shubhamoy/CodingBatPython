def string_splosion(str):
	result = ""
	for i in range(0,len(str)+1):
		result += str[0:i]
	return result
