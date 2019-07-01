ages = [12, 38, 34, 26, 21, 19, 67, 41, 17]

for num in ages:
  if num < 21:
    continue
  print(num)
  
#this prints all ages in the list except for those under 21. The continue line means that it will skip over any value less than 21

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
