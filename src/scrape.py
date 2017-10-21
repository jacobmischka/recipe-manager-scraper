#!/usr/bin/env python3

import seriouseats, bonappetit, wellplated

def fetch_recipe(url):
	if 'seriouseats.com' in url:
		return seriouseats.fetch_recipe(url)
	elif 'bonappetit.com' in url:
		return bonappetit.fetch_recipe(url)
	elif 'wellplated.com' in url:
		return wellplated.fetch_recipe(url)

def main():
	pass

if __name__ == '__main__':
	main()
