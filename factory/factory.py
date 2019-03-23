'''
factory.py
'''
#####################################################

# Class Factory
class ShapeInterface:
	def draw(self):
		pass

# Class Circle -> Product from Class Factory
class Circle(ShapeInterface):
	def draw(self):
		print("Circle Drawed")

# Class Square -> Product from Class Factory
class Square(ShapeInterface):
	def draw(self):
		print("Square Drawed")

Class ShapeFactory:
	@staticmethod
	def getShape(type):
		if type == 'circle':
			return Circle()
		if type == 'square':
			return Square()
		assert 0, 'Could not find shape' + type


'''
main.py
'''
#####################################################
# import class ShapeFactory from factory file
from factory import ShapeFactory
f = ShapeFactory()
s = f.getShape('square')

print(s)
# <<factory.Square object at 0x000000>>

s.draw()
# Square Drawed

t = f.getShape('triangle')
# AssertError: Could not find shape triangle
