'''

Iterating through lines - prints each line ib a doc

'''

with open('how_many_lines.txt') as lines_doc:
  for line in lines_doc.readlines():
    print(line)
