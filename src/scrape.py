from bs4 import BeautifulSoup
from requests import get

from recipe import Recipe
from bonappetit import BonAppetitRecipe
from seriouseats import SeriousEatsRecipe
from wellplated import WellPlatedRecipe

def fetch_recipe(url):
	soup = BeautifulSoup(get(url).text, 'html.parser')

	if 'seriouseats.com' in url:
		return SeriousEatsRecipe.from_soup(soup)
	elif 'bonappetit.com' in url:
		return BonAppetitRecipe.from_soup(soup)
	elif 'wellplated.com' in url:
		return WellPlatedRecipe.from_soup(soup)
	else:
		return Recipe.from_soup(soup)
