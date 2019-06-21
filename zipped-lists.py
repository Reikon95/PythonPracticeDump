first_names = ['Ainsley', 'Ben', 'Chani', 'Depak']
age = []

age.append(42)
#Adds 42 to the list
all_ages = age + [32, 41, 29]
#adds the two lists together into one new one
name_and_age = (zip(first_names, all_ages))
#this is a zipped lists, pairing the list values together according to their position
ids = range(0, 4)
#corresponding ID values (just range practice here)
print(list(name_and_age))

#prints the zipped values as a list in pairs - given example should print as [('Ainsley', 42), ('Ben', 32), ('Chani', 41), ('Depak', 29)]

