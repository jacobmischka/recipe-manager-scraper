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
		return soup.find('h1').get_text(strip=True)
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

	try:
		return soup.find(class_='recipe-main-photo').find('img').get('src')
	except Exception as e:
		print(e, file=sys.stderr)

	return None

def get_info(soup):
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


def get_ingredients(soup):
	try:
		container = soup.find(class_='recipe-ingredients')
		return [li.get_text(strip=True) for li in container.find_all(class_='ingredient')]
	except Exception as e:
		print(e, file=sys.stderr)

	return None

def get_directions(soup):
	try:
		container = soup.find(class_='recipe-procedures')
		return [item.get_text(strip=True) for item in container.find_all(class_='recipe-procedure-text')]
	except Exception as e:
		print(e, file=sys.stderr)

	return None

def main():
	pass

if __name__ == '__main__':
	main()
