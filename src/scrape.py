#!/usr/bin/env python3

import seriouseats

def fetch_recipe(url):
	if 'seriouseats.com' in url:
		return seriouseats.fetch_recipe(url)

def main():
	pass

if __name__ == '__main__':
	main()
