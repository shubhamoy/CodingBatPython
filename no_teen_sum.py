def fix_teen(n):
	return n if n==15 or n==16 else 0

def no_teen_sum(a, b, c): 
	if a >=13 and a <= 19:
		a = fix_teen(a)	
	if b >=13 and b <= 19:
		b = fix_teen(b)	
	if c >=13 and c <= 19:
		c = fix_teen(c)	
	return a+b+c
