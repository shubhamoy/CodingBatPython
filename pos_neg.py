def pos_neg(a, b, negative):
	return True if (a<0 and b<0 and negative==True) or (a<0 and b>0 and negative==False) or (a>0 and b<0 and negative==False) else False
