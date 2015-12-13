def end_other(a, b):
		a = a.lower()
		b = b.lower()
		if len(a) > len(b):
			for i in range(len(a)):
				if a[-len(b):] == b:
					return True
				return False
		return True if b[-len(a):] == a else False
