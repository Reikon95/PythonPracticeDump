#ranges define a range for the script to work through
#you write them like this (number, number, number)
#this is how they work (start, end +1, interval)

range(1, 11, 2)

#this would return 1, 3, 5, 7, 9 because it is every second number starting from one

#as an example, this is how you would use it to iterate in a list


def odd_indices(lst):
  new_lst = []
  for num in range(1, len(lst), 2):
    new_lst.append(lst[num])
  return new_lst  
   

print(odd_indices([4, 3, 7, 10, 11, -2]))

#list is the paramater, you feed it a list of elements and the range returns starting from 1, ending at the length of the list skipping every other value
#this returns [3, 10, -2]. Remember to start counting from zero
