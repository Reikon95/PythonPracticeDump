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
