class Recipe(object):

	def __init__(self,
		title=None,
		description=None,
		image=None,
		servings=None,
		ingredients=None,
		directions=None,
		time=None,
		**kwargs
	):
		self.title = title
		self.description = description
		self.image = image
		self.servings = servings
		self.ingredients = ingredients
		self.directions = directions
		self.time = time
		self.additional_info = kwargs

	def to_dict(self):
		return {
			'title': self.title,
			'description': self.description,
			'image': self.image,
			'servings': self.servings,
			'ingredients': self.ingredients,
			'directions': self.directions,
			'active_time': self.time['active'] if 'active' in self.time else None,
			'total_time': self.time['total'] if 'total' in self.time else None,
			'additional_info': self.additional_info
		}
