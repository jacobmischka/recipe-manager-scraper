from isodate import parse_duration
import sys

from utils import get_og_prop, get_servings_from_str, format_timedelta

class Recipe(object):

	def __init__(self,
		title=None,
		description=None,
		image=None,
		servings=None,
		ingredients=None,
		directions=None,
		time=None,
		**kwargs
	):
		self.title = title
		self.description = description
		self.image = image
		self.servings = servings
		self.ingredients = ingredients
		self.directions = directions
		self.time = time
		self.additional_info = kwargs

	@classmethod
	def from_soup(cls, soup):
		return cls(
			title=cls.get_title(soup),
			description=cls.get_description(soup),
			image=cls.get_image(soup),
			ingredients=cls.get_ingredients(soup),
			directions=cls.get_directions(soup),
			**cls.get_info(soup)
		)

	@classmethod
	def get_title(cls, soup):
		try:
			return get_og_prop(soup, 'title')
		except Exception as e:
			print('Failed to get title: {}'.format(e), file=sys.stderr)

		try:
			return soup.find('h1').get_text(strip=True)
		except Exception as e:
			print('Failed to get title: {}'.format(e), file=sys.stderr)

		return None

	@classmethod
	def get_description(cls, soup):
		try:
			return get_og_prop(soup, 'description')
		except Exception as e:
			print('Failed to get description: {}'.format(e), file=sys.stderr)

		try:
			return soup.find('meta', attrs={'name': 'description'}).get('content')
		except Exception as e:
			print('Failed to get description: {}'.format(e), file=sys.stderr)

		return None

	@classmethod
	def get_image(cls, soup):
		try:
			return get_og_prop(soup, 'image')
		except Exception as e:
			print('Failed to get image: {}'.format(e), file=sys.stderr)

		return None

	@classmethod
	def get_info(cls, soup):
		servings = None
		times = {}

		try:
			try:
				recipe_yield = soup.find(itemprop='recipeYield').get_text(strip=True)
				servings = get_servings_from_str(recipe_yield)[0]
			except Exception as e:
				print(e, file=sys.stderr)

			for time_type in ['prep', 'cook', 'total']:
				try:
					tag = soup.find(itemprop='{}Time'.format(time_type))
					value = tag.get('content')
					if not value:
						value = tag.get('datetime')
					if not value:
						value = tag.get_text(strip=True)
					duration = parse_duration(value)
					value = format_timedelta(duration)
					if value:
						times[time_type] = value
				except Exception as e:
					print(e, file=sys.stderr)

		except Exception as e:
			print(e, file=sys.stderr)

		return {
			'servings': servings,
			'time': times
		}


	@classmethod
	def get_ingredients(cls, soup):
		try:
			return [
				ingredient.get_text(strip=True)
				for ingredient in soup.find_all(itemprop='ingredients')
			]
		except Exception as e:
			print('Failed to get ingredients: {}'.format(e), file=sys.stderr)

		return None

	@classmethod
	def get_directions(cls, soup):
		try:
			return [
				sentence.strip() for sentence
				in soup.find(itemprop='recipeInstructions')\
					.get_text(strip=True).split('.')
				if sentence.strip()
			]
		except Exception as e:
			print('Failed to get directions: {}'.format(e), file=sys.stderr)

		return None
