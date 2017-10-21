import sys

from recipe import Recipe
from utils import get_servings_from_str

class SeriousEatsRecipe(Recipe):

	@classmethod
	def get_info(cls, soup):
		servings = None
		times = {}

		try:
			about = soup.find(class_='recipe-about')

			try:
				recipe_yield = about.find(class_='yield').get_text(strip=True)
				servings = get_servings_from_str(recipe_yield)[0]
			except Exception as e:
				print(e, file=sys.stderr)

			for li in about.find_all('li'):
				label = li.find(class_='label').get_text(strip=True)
				if 'time' in label:
					try:
						time_type = label.replace('time:', '').strip().lower()
						info = li.find(class_='info').get_text(strip=True)
						times[time_type] = info

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
			container = soup.find(class_='recipe-ingredients')
			return [li.get_text(strip=True) for li in container.find_all(class_='ingredient')]
		except Exception as e:
			print('Failed to get ingredients: {}'.format(e), file=sys.stderr)

		return None

	@classmethod
	def get_directions(cls, soup):
		try:
			container = soup.find(class_='recipe-procedures')
			return [item.get_text(strip=True) for item in container.find_all(class_='recipe-procedure-text')]
		except Exception as e:
			print('Failed to get directions: {}'.format(e), file=sys.stderr)

		return None
