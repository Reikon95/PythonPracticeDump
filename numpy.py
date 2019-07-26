import numpy as np
import csv
# with open('books.csv') as books_csv:
test_1 = np.array([92, 94, 88, 91, 87])

test_2 = np.genfromtxt('test_2.csv', delimiter=',')

print(test_2)

test_3_fixed = []
for i in range(len(test_3)):
  test_3_fixed.append(test_3[i] + 2)


print(test_3)
print(test_3_fixed)

  '''
  Calc average
  '''

test_1 = np.array([92, 94, 88, 91, 87])
test_2 = np.array([79, 100, 86, 93, 91])
test_3 = np.array([87, 85, 72, 90, 92])
test_3_fixed = test_3 + 2

total_grade = (test_1 + test_2 + test_3_fixed) 

print(total_grade)

final_grade = (total_grade / 3)

print(final_grade)


  '''
  Coin toss example - 2 dimensional array
  '''
coin_toss = np.array([1, 0, 0, 1, 0])

coin_toss_again = np.array([[1, 0, 0, 1, 0], [0, 0, 1, 1, 1]])

  '''
  Select data from array
  '''
jeremy_test_2 = test_2[3]

manual_adwoa_test_1 = test_1[1:3]

student_scores = np.array([[92, 94, 88, 91, 87],
                           [79, 100, 86, 93, 91],
                           [87, 85, 72, 90, 92]])

tanya_test_3 = student_scores[2, 0]

print(tanya_test_3)

cody_test_scores = student_scores[0:3, 4]

print(cody_test_scores)

  '''
  Logical operators
  '''
porridge = np.array([79, 65, 50, 63, 56, 90, 85, 98, 79, 51])

cold = porridge[porridge < 60]

hot = porridge[porridge > 80]

just_right = porridge[(porridge > 60) & (porridge < 80)]

print(cold)
print(hot)
print(just_right)
