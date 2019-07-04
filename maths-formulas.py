
#circle calculations
radius = 5.
circle_perimeter = (2 * 3.14 * radius) 
circle_area = (3.14 * (radius ** 2)) 
print('A circle of radius ' + str(radius) + ' has a perimeter of ' +
   str(circle_perimeter) + ' and an area of ' + str(circle_area))

#Standard deviation. Need to simplify this

from math import sqrt
x1 = float(input('Enter the first number: '))
x2 = float(input('Enter the second number: '))
x3 = float(input('Enter the third number: '))

def simple_stdev(x1, x2, x3):
    simpmean = (x1 + x2 + x3) / 3
    print(simpmean)
    difa = ((x1 - simpmean) ** 2)
    print(difa)
    difb = ((x2 - simpmean) ** 2)
    print(difb)
    difc = ((x3 - simpmean) ** 2)
    print(difc)
    sum_of_difs = difa + difb + difc
    print(sum_of_difs)
    varience = (sum_of_difs / 3)
    print(varience)
    print(sqrt(varience))
    
   

simple_stdev(x1, x2, x3)
