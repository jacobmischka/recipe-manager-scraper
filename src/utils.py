def get_servings_from_str(servings_str):
	return [int(s) for s in servings_str.split() if s.isdigit()]
