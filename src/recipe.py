import sys

from utils import get_og_prop

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
			print(e, file=sys.stderr)

		try:
			return soup.find('h1').get_text(strip=True)
		except Exception as e:
			print(e, file=sys.stderr)

		return None

	@classmethod
	def get_description(cls, soup):
		try:
			return get_og_prop(soup, 'description')
		except Exception as e:
			print(e, file=sys.stderr)

		try:
			return soup.find('meta', attrs={'name': 'description'}).get('content')
		except Exception as e:
			print(e, file=sys.stderr)


		return None

	@classmethod
	def get_image(cls, soup):
		try:
			return get_og_prop(soup, 'image')
		except Exception as e:
			print(e, file=sys.stderr)

		return None

	@classmethod
	def get_info(cls, _):
		servings = None
		times = {}

		return {
			'servings': servings,
			'time': times
		}

	@classmethod
	def get_ingredients(cls, _):
		return None

	@classmethod
	def get_directions(cls, _):
		return None


	def to_dict(self):
		return {
			'title': self.title,
			'description': self.description,
			'image': self.image,
			'servings': self.servings,
			'ingredients': self.ingredients,
			'directions': self.directions,
			'active_time': self.time['active'] if 'active' in self.time else None,
			'total_time': self.time['total'] if 'total' in self.time else None,
			'additional_info': self.additional_info
		}
