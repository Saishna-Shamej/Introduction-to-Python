import re

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt) #returns start and end position of the first match occurance
print(x.span())
print()

import re

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)  #returns the search string
print(x.string)
print()

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)  #search for an upperstring character S in the beginning of the word and print the word
print(x.group())
print()



