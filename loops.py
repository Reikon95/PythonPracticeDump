ages = [12, 38, 34, 26, 21, 19, 67, 41, 17]

for num in ages:
  if num < 21:
    continue
  print(num)
  
#this prints all ages in the list except for those under 21. The continue line means that it will skip over any value less than 21
