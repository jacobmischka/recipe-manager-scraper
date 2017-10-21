#!/usr/bin/env python3

from bs4 import BeautifulSoup
from requests import get
import sys

from recipe import Recipe
from utils import get_servings_from_str, get_og_prop

def fetch_recipe(url):
	page = get(url).text
	soup = BeautifulSoup(page, 'html.parser')

	return Recipe(
		title=get_title(soup),
		description=get_description(soup),
		image=get_image(soup),
		ingredients=get_ingredients(soup),
		directions=get_directions(soup),
		**get_info(soup)
	)

def get_title(soup):
	try:
		return get_og_prop(soup, 'title')
	except Exception as e:
		print(e, file=sys.stderr)

	try:
		return soup.find(id='recipe').find(itemprop='name').get_text(strip=True)
	except Exception as e:
		print(e, file=sys.stderr)

	return None

def get_description(soup):
	try:
		return get_og_prop(soup, 'description')
	except Exception as e:
		print(e, file=sys.stderr)

	try:
		return soup.find('meta', attrs={'name': 'description'}).get('content')
	except Exception as e:
		print(e, file=sys.stderr)

	return None

def get_image(soup):
	try:
		return get_og_prop(soup, 'image')
	except Exception as e:
		print(e, file=sys.stderr)

	return None

def get_info(soup):
	servings = None
	times = {}

	recipe = soup.find(id='recipe')

	try:
		recipe_yield = recipe.find(itemprop='recipeYield').get_text(strip=True)
		servings = get_servings_from_str(recipe_yield)[0]
	except Exception as e:
		print(e, file=sys.stderr)

	# No times :(

	return {
		'servings': servings,
		'time': times
	}


def get_ingredients(soup):
	try:
		recipe = soup.find(id='recipe')
		return [
			ingredient.get_text(strip=True)
			for ingredient in recipe.find_all(itemprop='ingredients')
		]
	except Exception as e:
		print(e, file=sys.stderr)

	return None

def get_directions(soup):
	directions = []
	try:
		recipe = soup.find(id='recipe')
		for child in recipe.children:
			try:
				if child.name == 'p' and not child.get('class'):
					directions.append(child.get_text(strip=True))
			except Exception as e:
				print(e, file=sys.stderr)
	except Exception as e:
		print(e, file=sys.stderr)

	return directions

def main():
	pass

if __name__ == '__main__':
	main()
