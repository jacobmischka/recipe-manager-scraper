from isodate import parse_duration
import sys

from recipe import Recipe
from utils import get_servings_from_str, format_timedelta

class WellPlatedRecipe(Recipe):

	@classmethod
	def get_info(cls, soup):
		servings = None
		times = {}

		try:
			about = soup.find(id='recipe').find(class_='time')

			try:
				recipe_yield = about.find(itemprop='recipeYield').get_text(strip=True)
				servings = get_servings_from_str(recipe_yield)[0]
			except Exception as e:
				print(e, file=sys.stderr)

			for time_type in ['prep', 'cook', 'total']:
				try:
					tag = about.find(itemprop='{}Time'.format(time_type))
					duration = parse_duration(tag.get('content'))
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
			container = soup.find(id='recipe').find(class_='ingredients')
			return [li.get_text(strip=True) for li in container.find_all(class_='ingredient')]
		except Exception as e:
			print(e, file=sys.stderr)

		return None

	@classmethod
	def get_directions(cls, soup):
		try:
			container = soup.find(id='recipe').find(class_='instructions')
			return [item.get_text(strip=True) for item in container.find_all('li')]
		except Exception as e:
			print(e, file=sys.stderr)

		return None
