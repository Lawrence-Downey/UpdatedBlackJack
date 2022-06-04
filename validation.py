'''
This Module is used for validating information throughout the Black Jack game
'''
import re

firstName = input("First Name:\t")
middleName = input("Middle Name:\t")
lastName = input("Last Name:\t")


# Function to validate Name entries
def checkName(name):
    invalidName = True
    pattern = r"[0-9]+"
    if name == '':
        return invalidName
    match = re.findall(pattern, name)
    if len(match) >= 1:
        return invalidName
    





checkName(firstName)
checkName(middleName)
checkName(lastName)
print()
print(firstName)
print(middleName)
print(lastName)
