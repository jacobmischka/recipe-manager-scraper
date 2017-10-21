def get_servings_from_str(servings_str):
	return [int(s) for s in servings_str.split() if s.isdigit()]

def get_og_prop(soup, prop):
	return soup.find('meta', property='og:{}'.format(prop)).get('content')
