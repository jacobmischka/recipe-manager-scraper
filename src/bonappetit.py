#!/usr/bin/env python3

from bs4 import BeautifulSoup
from requests import get
import json, sys

from recipe import Recipe
from utils import get_servings_from_str

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
	return soup.find('h1').get_text(strip=True)

def get_description(soup):
	return soup.find('meta', attrs={'property': 'og:description'}).get('content')

def get_image(soup):
	return soup.find('meta', attrs={'property': 'og:image'}).get('content')

def get_info(soup):
	container = soup.find(class_='post-dek-meta')

	servings = None
	try:
		servings = container.find(class_='recipe__header__servings').get_text(strip=True)
		servings = get_servings_from_str(servings)[0]
	except Exception as e:
		print(e, file=sys.stderr)

	times = {}
	for li in container.find_all(class_='recipe__header__times'):
		label = li.get_text(strip=True)
		try:
			[time_type, time_val] = label.split(':')
			time_type = time_type.lower().replace('time', '').strip()
			time_val = time_val.strip()
			times[time_type] = time_val

		except Exception as e:
			print(e, file=sys.stderr)

	return {
		'servings': servings,
		'time': times
	}


def get_ingredients(soup):
	container = soup.find(class_='ingredients')
	return [li.get_text(strip=True) for li in container.find_all(class_='ingredient')]

def get_directions(soup):
	container = soup.find(class_='steps')
	return [item.get_text(strip=True) for item in container.find_all(class_='step')]

def main():
	pass

if __name__ == '__main__':
	main()
