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

'''

Writing a CSV File
This creates a csv file

'''

access_log = [{'time': '08:39:37', 'limit': 844404, 'address': '1.227.124.181'}, {'time': '13:13:35', 'limit': 543871, 'address': '198.51.139.193'}, {'time': '19:40:45', 'limit': 3021, 'address': '172.1.254.208'}, {'time': '18:57:16', 'limit': 67031769, 'address': '172.58.247.219'}, {'time': '21:17:13', 'limit': 9083, 'address': '124.144.20.113'}, {'time': '23:34:17', 'limit': 65913, 'address': '203.236.149.220'}, {'time': '13:58:05', 'limit': 1541474, 'address': '192.52.206.76'}, {'time': '10:52:00', 'limit': 11465607, 'address': '104.47.149.93'}, {'time': '14:56:12', 'limit': 109, 'address': '192.31.185.7'}, {'time': '18:56:35', 'limit': 6207, 'address': '2.228.164.197'}]
fields = ['time', 'address', 'limit']

import csv
with open('logger.csv', 'w') as logger_csv:
  log_writer = csv.DictWriter(logger_csv, fieldnames=fields )
  log_writer.writeheader()
  for item in access_log:
    log_writer.writerow(item)

'''
   JSON
   
'''

import json

with open('message.json') as message_json:
  message = json.load(message_json)
  print(message['text'])
