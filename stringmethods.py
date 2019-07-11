# .upper(), .title(), and .lower() adjust the casing of your string.
# .split() takes a string and creates a list of substrings.
# .join() takes a list of strings and creates a string.
# .strip() cleans off whitespace, or other noise from the beginning and end of a string.
# .replace() replaces all instances of a character/string in a string with another character/string.
# .find() searches a string for a character/string and returns the index value that character/string is found at.
# .format() and f-strings allow you to interpolate a string with variables.
#.format()
def poem_title_card(poet, title):
  return "The poem \"{}\" is written by {}.".format(title, poet)
print(poem_title_card("Walt Whitman", "I Hear America Singing"))

def count_char_x(word, x):
  return word.count(x)
#returns the number of occurances of x in word


#EXAMPLE - my solution to reverse a string

def reverse_string(word):
  solution = [] #empty list for solution
  strlst = list(word) #convert word to list
  jj = len(strlst) #new variable which is length of the word basically
  while len(solution) < jj: #conditional loop
    letter = strlst.pop() #var is last elem in list
    solution.append(letter) #moves to the solution list
  result = ''.join(solution) #new variable which is a string, the joined solution list
  return result


def make_spoonerism(word1, word2):
  a = word2[0] + word1[1 :]
  b = word1[0] + word2[1 :]
  print(a + b)
  str = a + ' ' + b
  return str
  
