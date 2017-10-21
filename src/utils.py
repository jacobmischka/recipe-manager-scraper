def get_servings_from_str(servings_str):
	return [int(s) for s in servings_str.split() if s.isdigit()]

def get_og_prop(soup, prop):
	return soup.find('meta', property='og:{}'.format(prop)).get('content')

def format_timedelta(td):
	s = str(td).split(' ')[-1]
	[hours, minutes, _] = s.split(':')

	pieces = []
	if td.days:
		pieces.append('{} days'.format(td.days))
	if hours and int(hours):
		pieces.append('{} hours'.format(int(hours)))
	if minutes and int(minutes):
		pieces.append('{} minutes'.format(int(minutes)))

	return ', '.join(pieces)
