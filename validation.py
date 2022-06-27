"""
This Module is used for validating information throughout the Black Jack game
"""
import re


# Function to validate Name entries
def checkName(name):
    invalidName = "Invalid Entry"
    pattern = "[0-9]+"
    if name == '':
        return invalidName
    match = re.findall(pattern, name)
    if len(match) != 0:
        return invalidName
    else:
        return name


