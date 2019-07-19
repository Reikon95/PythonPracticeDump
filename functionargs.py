'''
** means keyword arguments meaning you can just input some keywords and it'll work
'''

print("My name is {name} and I'm feeling {feeling}.".format(name = 'Cameron', feeling = 'happy'))

from products import create_product

def create_products(**products_dict):
  for name, price in products_dict.items():
    create_product(name, price)


create_products(Baseball=3, Shirt=14, Guitar=70)


