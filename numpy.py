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
