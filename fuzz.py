class Fuzzy_range:
	"""
	Defines a range over which membership can be fuzzy.
	
	Takes at least 3 arguments, each a tuple of the form
	(turning_point, membership)
	where membership is a value between 0 inclusive and 1 inclusive.
	
	Think of turning points as being plotted on a graph, where the
	x-axis is the value of the turning point, and the y-axis is the
	membership value.
	"""
	def __init__(self, *points):
		self.points = sorted(points)
		self.defined_discont = list()
		# List of "discontinuous points" where the values are defined by appearing twice
		for i in range(len(self.points)):
			if self.points[i] == self.points[i-1]:
				if self.points[i] in self.defined_discont:
					print("Warning: discontinous point already defined")
				self.defined_discont.append(self.points[i])
	def has(self, testnum):
		"""
		Calculates membership for testnum in this Fuzzy_range object.
		Arguments: testnum
		Returns: a real number between 0 inclusive and 1 inclusive.
		(Defuzzification is left to the caller.)
		"""
		# Out of defined range.
		if testnum < min(self.points)[0] or testnum > max(self.points)[0]:
			return 0
		# Not enough known turning points.
		if len(self.points) <= 2:
			return 0
		# Main test loops
		## Uses the lower membership value for a defined discontinuous point
		for i in self.defined_discont:
			if testnum == i[0]:
				return i[1]
		for i in range(len(self.points)):
			if testnum == self.points[i][0]:
				return self.points[i][1]
			if testnum > self.points[i][0]:
				continue
			else:
				# Simple linear interpolation
				#                  points[i]
				#                 /   |
				#                /    |
				#               /     |
				#              /      |
				#            testnum  |
				#           /   |     |
				# points[i-1]----------
				return ((testnum-self.points[i-1][0]) / (self.points[i][0]-self.points[i-1][0])) * (self.points[i][1]-self.points[i-1][1]) + self.points[i-1][1]
		return None # Something went wrong!

# (((j - uold) / (u - uold)) * (v - vold)) + vold == w