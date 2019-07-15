'''

Iterating through lines - prints each line ib a doc

'''

with open('how_many_lines.txt') as lines_doc:
  for line in lines_doc.readlines():
    print(line)

'''

Only reading one line of doc


'''

with open('just_the_first.txt') as first_line_doc:
  first_line = first_line_doc.readline()
  print(first_line)


'''

Writing to a document (w means write in this case, after the file name)
This example opens a document filled with bad bands in writeable mode
Then we just add BrokeNCYDE because they sucked.
'''

with open('bad_bands.txt', 'w') as bad_bands_doc:
  bad_bands_doc.write('BrokeNCYDE')
  
''' 

Appending a document means you aren't totally rewriting it like the above
It adds to it rather than overwrites. Note the a in the place of w
'''

with open('cool_dogs.txt', 'a') as cool_dogs_file:
  cool_dogs_file.write('Air Bud')

'''
Open CSV files is easy as they are basically just plain text

See below 

'''

with open('logger.csv') as log_csv_file:
  stre = log_csv_file.read()
  print(stre)

'''

That being said, not always best to open as plain text
You can import a CSV module which basically makes it easier to handle.
You can save it as a dictionary which again makes it easier
Line is the key, so we are asking for it to print the value.

'''
import csv

with open('cool_csv.csv') as cool_csv_file:
  cool_csv_dict = csv.DictReader(cool_csv_file)
  for line in cool_csv_dict:
    print(line['Cool Fact'])
'''

And with a delimiter...

'''

import csv
with open('books.csv') as books_csv:
  books_reader = csv.DictReader(books_csv, delimiter='@')
  isbn_list = []
  for row in books_reader:
    isbn_list.append(row['ISBN'])
print(isbn_list)
