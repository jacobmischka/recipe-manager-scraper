import sys

from recipe import Recipe
from utils import get_servings_from_str

class BonAppetitRecipe(Recipe):

	@classmethod
	def get_info(cls, soup):
		servings = None
		times = {}

		try:
			container = soup.find(class_='post-dek-meta')
			try:
				servings = container.find(class_='recipe__header__servings').get_text(strip=True)
				servings = get_servings_from_str(servings)[0]
			except Exception as e:
				print(e, file=sys.stderr)

			for li in container.find_all(class_='recipe__header__times'):
				label = li.get_text(strip=True)
				try:
					[time_type, time_val] = label.split(':')
					time_type = time_type.lower().replace('time', '').strip()
					time_val = time_val.strip()
					times[time_type] = time_val

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
			container = soup.find(class_='ingredients')
			return [li.get_text(strip=True) for li in container.find_all(class_='ingredient')]
		except Exception as e:
			print(e, file=sys.stderr)

	@classmethod
	def get_directions(cls, soup):
		try:
			container = soup.find(class_='steps')
			return [item.get_text(strip=True) for item in container.find_all(class_='step')]
		except Exception as e:
			print(e, file=sys.stderr)
