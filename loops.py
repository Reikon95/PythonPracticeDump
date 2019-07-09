#general for loop structure:
for <temporary variable> in <list variable>:
    <action>
#standard

#Using basic range

str = "Hello World"

for temporary_var in range(5):
  print(str)

#This prints out the string 5 times

#Transfering from one list to another
students_period_A = ["Alex", "Briana", "Cheri", "Daniele"]
students_period_B = ["Dora", "Minerva", "Alexa", "Obie"]

for student in students_period_A:
  students_period_B.append(student)
  print(student)
#this will move each student from a to B and then print out their name for each iteration of the loop. very simple. 

#Using break keyword stops the loop in its tracks, useful for if you're trying to find something

dog_breeds_available_for_adoption = ['french_bulldog', 'dalmation', 'shihtzu', 'poodle', 'collie']
dog_breed_I_want = 'dalmation'

for dog in dog_breeds_available_for_adoption:
  print(dog)
  if dog == dog_breed_I_want:
    print('They have the dog I want!')
    break  

#This example would iterate through the list of dogs and print each one until it reaches dalmation (the dog wanted). 
#The break keyword tells it to stop running if it reaches a certain point (in this case, dealmation)

#Continue keyword - this 'skips' the element in the list and just keeps running the loop with no action.
ages = [12, 38, 34, 26, 21, 19, 67, 41, 17]

for num in ages:
  if num < 21:
    continue
  print(num)
  
#this prints all ages in the list except for those under 21. The continue line means that it will skip over any value less than 21

#While loops
#This is a loop that executues as long as a condition remains the one described in the initalising process

all_students = ["Alex", "Briana", "Cheri", "Daniele", "Dora", "Minerva", "Alexa", "Obie", "Arius", "Loki"]
students_in_poetry = []

while len(students_in_poetry) < 6:
  student = all_students.pop()
  students_in_poetry.append(student)
  
print(students_in_poetry)

#This example will cap off at 6 iterations (while length is less than 6 + the final one), pop a student off first list and add them to second one
#Important to remember to create a temporary variable (in this case, student)

#Nested Loops 
#A loop that executes inside a loop.
sales_data = [[12, 17, 22], [2, 10, 3], [5, 12, 13]]

scoops_sold = 0

for location in sales_data:
  print(location)
  for sale in location:
    scoops_sold += sale
    print(scoops_sold)
#this iterates through sales data firstly and then prints the parent list. (Location). Then, the second loop adds the numbers up into the variable scoops sold





















#sum all numbers in range

def larger_sum(lst1, lst2):
  sum1 = 0
  for num in lst1:
    sum1 = sum1+num
  sum2 = 0
  for num in lst2:
    sum2 = sum2+num
  if sum1 >= sum2:
    return lst1
  else:
    return lst2
print(larger_sum([1, 9, 5], [2, 3, 7]))

#returns list with higher sum

#finding largest number in range
def max_num(nums):
  big = nums[0]
  for i in nums:
    
    print(big)
    if (i > big):
      big = i
    print(big)
  return big
    
  

print(max_num([50, -10, 0, 75, 20]))


#nested loop to return values that are the same in two lists
def same_values(lst1, lst2):
  newlst = []
  for val in range(len(lst1)):
    print(val)
    if (lst1[val] == lst2[val]):
      print('yes')
      newlst.append(val)
      print(newlst)
  return newlst  
    
      

print(same_values([5, 1, -10, 3, 3], [5, 10, -10, 3, 5]))
