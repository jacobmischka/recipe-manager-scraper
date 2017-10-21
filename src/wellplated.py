import sys

from recipe import Recipe

class WellPlatedRecipe(Recipe):

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
