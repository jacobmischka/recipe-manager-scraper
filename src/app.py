#!/usr/bin/env python3

from sanic import Sanic
from sanic.response import json
from sanic_cors import CORS

from scrape import fetch_recipe

app = Sanic()
CORS(app)

@app.route('/fetch')
async def fetch(request):
	return json(fetch_recipe(request.args['url'][0]))

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=4000)
