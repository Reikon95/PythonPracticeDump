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
