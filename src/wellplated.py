#!/usr/bin/env python3

from bs4 import BeautifulSoup
from requests import get
from isodate import parse_duration
from datetime import datetime
import sys

from recipe import Recipe
from utils import get_servings_from_str, get_og_prop, format_timedelta

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

	try:
		return soup.find(id='recipe').find(class_='summary').get_text(strip=True)
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


def get_ingredients(soup):
	try:
		container = soup.find(id='recipe').find(class_='ingredients')
		return [li.get_text(strip=True) for li in container.find_all(class_='ingredient')]
	except Exception as e:
		print(e, file=sys.stderr)

	return None

def get_directions(soup):
	try:
		container = soup.find(id='recipe').find(class_='instructions')
		return [item.get_text(strip=True) for item in container.find_all('li')]
	except Exception as e:
		print(e, file=sys.stderr)

	return None

def main():
	pass

if __name__ == '__main__':
	main()
