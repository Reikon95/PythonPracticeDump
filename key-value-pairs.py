sensors =  {"living room": 21, "kitchen": 23, "bedroom": 20, "pantry": 22}
num_cameras = {"backyard": 6,  "garage": 2, "driveway": 1}

print(sensors)


'''
simple structure, they go in pairs. First one is key, second one value.


Easy

'''
animals_in_zoo = {}

animals_in_zoo["zebras"] = 8
animals_in_zoo["monkeys"] = 12
animals_in_zoo["dinosaurs"] = 0
print(animals_in_zoo)



songs = ["Like a Rolling Stone", "Satisfaction", "Imagine", "What's Going On", "Respect", "Good Vibrations"]
playcounts = [78, 29, 44, 21, 89, 5]

plays = {key: value for key, value in zip(songs, playcounts)}

print(plays)

plays['Purple Haze'] = 1

plays['Respect'] = 94

library = {"The Best Songs": plays, "Sunday Feelings": {}}

print(library)






''''

GET A KEY

'''

zodiac_elements = {"water": ["Cancer", "Scorpio", "Pisces"], "fire": ["Aries", "Leo", "Sagittarius"], "earth": ["Taurus", "Virgo", "Capricorn"], "air":["Gemini", "Libra", "Aquarius"]}

print(zodiac_elements["earth"])

print(zodiac_elements["fire"])


'''

Try/Except 
Like if else except try is if it works and except is if it doesnt
'''

caffeine_level = {"espresso": 64, "chai": 40, "decaf": 0, "drip": 120}
caffeine_level['matcha'] = 30

try:
  print(caffeine_level['matcha'])
except:
  print('Unknown Caffeine Level')
  
  
  
'''
Default values
'''
  
user_ids = {"teraCoder": 100019, "pythonGuy": 182921, "samTheJavaMaam": 123112, "lyleLoop": 102931, "keysmithKeith": 129384}

tc_id = user_ids.get("teraCoder", 10000)

stack_id = user_ids.get("superStackSmash", 100000)
print(stack_id)

'''
.pop 

'''

available_items = {"health potion": 10, "cake of the cure": 5, "green elixir": 20, "strength sandwich": 25, "stamina grains": 15, "power stew": 30}
health_points = 20

health_points += available_items.pop("stamina grains", 0)
health_points += available_items.pop("power stew", 0)
health_points += available_items.pop("mystic bread", 0)

print(available_items)
print(health_points)
'''
Dict Keys

'''
user_ids = {"teraCoder": 100019, "pythonGuy": 182921, "samTheJavaMaam": 123112, "lyleLoop": 102931, "keysmithKeith": 129384}
num_exercises = {"functions": 10, "syntax": 13, "control flow": 15, "loops": 22, "lists": 19, "classes": 18, "dictionaries": 18}

users = user_ids.keys()

print(users)

lessons = num_exercises.keys()


print(lessons)


'''
Get all values

'''

num_exercises = {"functions": 10, "syntax": 13, "control flow": 15, "loops": 22, "lists": 19, "classes": 18, "dictionaries": 18}

total_exercises = 0

for val in num_exercises.values():
  total_exercises += val
  
print(total_exercises)

