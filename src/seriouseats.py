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
	return soup.find('meta', attrs={'name': 'description'}).get('content')

def get_image(soup):
	return soup.find(class_='recipe-main-photo').find('img').get('src')

def get_info(soup):
	about = soup.find(class_='recipe-about')

	servings = None
	try:
		recipe_yield = about.find(class_='yield').get_text(strip=True)
		servings = get_servings_from_str(recipe_yield)[0]
	except Exception as e:
		print(e, file=sys.stderr)

	times = {}
	for li in about.find_all('li'):
		label = li.find(class_='label').get_text(strip=True)
		if 'time' in label:
			try:
				time_type = label.replace('time:', '').strip().lower()
				info = li.find(class_='info').get_text(strip=True)
				times[time_type] = info

			except Exception as e:
				print(e, file=sys.stderr)

	return {
		'servings': servings,
		'time': times
	}


def get_ingredients(soup):
	container = soup.find(class_='recipe-ingredients')
	return [li.get_text(strip=True) for li in container.find_all(class_='ingredient')]

def get_directions(soup):
	container = soup.find(class_='recipe-procedures')
	return [item.get_text(strip=True) for item in container.find_all(class_='recipe-procedure-text')]

def main():
	pass

if __name__ == '__main__':
	main()
