# recipe-manager-scraper

Quick and simple recipe scraper. Intended to be used by [recipe-manager][recipe-manager], but can be used anywhere.

By default it attempts to fetch metadata from opengraph meta tags, and recipe information from [Recipe schema][recipe-schema] tags.

Any site that implements both of those should work, but a few sites are currently "officially" supported:

- seriouseats.com
- wellplated.com
- bonappetit.com
- allrecipes.com

## Usage

Pass the url of the page to scrape as `url` search param to `/fetch` route.

### Request

`recipe-manager-scraper.now.sh/fetch?url=http://www.seriouseats.com/recipes/2017/01/3-ingredient-stovetop-mac-and-cheese-recipe.html`

### Response

```json
{
  "additional_info": {},
  "description": "This macaroni and cheese—this pot of creamy, gooey, cheesy, glorious macaroni and cheese—was made with three ingredients in about 10 minutes. Seriously. That's one fewer ingredient than you need to add to the pot to make a box of Kraft macaroni and cheese. Not only that, but all three ingredients are staples, with shelf lives of weeks or months, which means that a simple lunch is always on hand.\\n\\nReady to see it?",
  "directions": [
    "Place macaroni in a medium saucepan or skillet and add just enough cold water to cover. Add a pinch of salt and bring to a boil over high heat, stirring frequently. Continue to cook, stirring, until water has been almost completely absorbed and macaroni is just shy of al dente, about 6 minutes.",
    "Immediately add evaporated milk and bring to a boil. Add cheese. Reduce heat to low and cook, stirring continuously, until cheese is melted and liquid has reduced to a creamy sauce, about 2 minutes longer. Season to taste with more salt and serve immediately."
  ],
  "image": "http://www.seriouseats.com/recipes/assets_c/2017/01/20170105-3-ingredient-macaroni-and-cheese-10-thumb-1500xauto-435890.jpg",
  "ingredients": [
    "6 ounces (170g) elbow macaroni",
    "Salt",
    "6 ounces (180ml) evaporated milk",
    "6 ounces (170g) grated mild or medium cheddar cheese, or any good melting cheese, such as Fontina, Gruyère, or Jack"
  ],
  "servings": 2,
  "time": {
    "active": "8 minutes",
    "total": "8 minutes"
  },
  "title": "3-Ingredient Stovetop Macaroni and Cheese Recipe"
}
```

[recipe-manager]: https://github.com/abstractcoder/recipe-manager
[recipe-schema]: http://schema.org/Recipe
