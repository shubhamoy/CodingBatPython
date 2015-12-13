def cat_dog(str):
		ccat = 0
		cdog = 0
		for i in range(len(str)):
			if str[i:i+3] == "cat":
				ccat += 1
			if str[i:i+3] == "dog":
				cdog += 1
		return True if ccat == cdog else False
