#convert upper and lower case strings
import string

message = "uSiNg aPPrOpRiAtE cApiTaLISAtiOn iS iMpOrTaNt fOr yOuR rEaDerS' SANity"
lowercased =  message.lower()
sentencecased = lowercased[0].upper() + lowercased[1: ] 

print(message + '\n' + lowercased + '\n' + sentencecased)
#Prints = 
#uSiNg aPPrOpRiAtE cApiTaLISAtiOn iS iMpOrTaNt fOr yOuR rEaDerS' SANity
#using appropriate capitalisation is important for your readers' sanity
#Using appropriate capitalisation is important for your readers' sanity

#Password generator

first_name = "Reiko"
last_name = "Matsuki"

def password_generator(first_name, last_name):
  return (first_name[len(first_name) - 3: ]) + (last_name[len(last_name) - 3: ])

temp_password = password_generator(first_name, last_name)

print(temp_password)

#Making edits to immutable strings

first_name = "Bob"
last_name = "Daily"


fixed_first_name = "R" + first_name[1:]

