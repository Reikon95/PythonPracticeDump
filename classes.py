'''
Classes
'''

class ExampleClass:
  pass

'''
Methods are functions within classes
These are then callable 
'''
class Rules:
  def washing_brushes(self):
    return "Point bristles towards the basin while washing your brushes."

'''
Methods with arguments
'''
class Circle:
  pi = 3.14
  
  def area(self, radius):
    return Circle.pi * radius ** 2
  
circle = Circle()
pizza_area = circle.area(12 / 2)
teaching_table_area = circle.area(36 / 2)
round_room_area = circle.area(11460 / 2)
