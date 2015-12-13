def not_string(str):
	return str if str.strip()[:3]=='not' else 'not '+str
