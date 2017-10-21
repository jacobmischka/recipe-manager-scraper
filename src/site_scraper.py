#!/usr/bin/env python3

from bs4 import BeautifulSoup
from requests import get
import sys

from recipe import Recipe
from utils import get_og_prop

class SiteScraper(object):

	@classmethod
	def fetch_recipe(cls, url):
		page = get(url).text
		soup = BeautifulSoup(page, 'html.parser')

		return Recipe(
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
