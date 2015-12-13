def cigar_party(cigars, is_weekend):
	if cigars >= 40:
		if is_weekend == True:
			return True
		elif cigars <= 60:
			return True
		else:
			return False
	else:
		return False
