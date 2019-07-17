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

'''
Constructors
'''
class Circle:
  pi = 3.14
  
  # Add constructor here:
  def __init__(self, diameter):
    print("New circle with diameter: {diameter}".format(diameter=diameter))
    
teaching_table = Circle(36)

'''
Instance variables
The below creates objects
'''
class Store:
  pass

alternative_rocks = Store()
isabelles_ices = Store()

alternative_rocks.store_name = "Alternative Rocks"
isabelles_ices.store_name = "Isabelle's Ices"

'''
Check if a method exists
'''

how_many_s = [{'s': False}, "sassafrass", 18, ["a", "c", "s", "d", "s"]]

for element in how_many_s:
  if hasattr(element, "count"):
    print(element.count("s"))
'''
Constructing additional methods
'''
class Circle:
  pi = 3.14
  def __init__(self, diameter):
    print("Creating circle with diameter {d}".format(d=diameter))
    # Add assignment for self.radius here:
    self.radius = (diameter / 2)
  def circumference(self):
    circumference = 2 * self.pi * self.radius
    return circumference

medium_pizza = Circle(12)
teaching_table = Circle(36)
round_room = Circle(11460)

print(medium_pizza.circumference())
print(teaching_table.circumference())
print(round_room.circumference())

'''
Dir gives out all the attributes of an object
'''
print(dir(5)) # Dir gives you all the attributes 


'''
Inheritance
Essentialy a copy with a difference.
Child is below, parent is above
'''
class Bin:
  pass

class RecyclingBin(Bin):
  pass


