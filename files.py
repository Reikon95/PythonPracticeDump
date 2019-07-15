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
