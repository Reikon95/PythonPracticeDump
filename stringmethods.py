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
