"""
Used to keep track of user's money
"""

from database import cursor, db
import sys
import datetime


class Player:
    def __init__(self, firstName, middleName, lastName, username, password, birthYear, birthMonth, birthDay, city,
                 provState, phoneNumber, email, money):
        self._firstName = firstName
        self._middleName = middleName
        self._lastname = lastName
        self._username = username
        self._password = password
        self._birthYear = birthYear
        self._birthMonth = birthMonth
        self._birthDay = birthDay
        self._city = city
        self._provState = provState
        self._phoneNumber = phoneNumber
        self._email = email
        self._money = money

    @property
    def firstName(self):
        return self._firstName

    @property
    def middleName(self):
        return self._middleName

    @property
    def lastName(self):
        return self._lastname

    # Including a Setter for Last name in the even the player gets married and changes their last name.
    @lastName.setter
    def lastName(self, lastName):
        self._lastname = lastName

    @property
    def getUsername(self):
        return self._username

    @property
    def getPassword(self):
        return self._password

    @property
    def getBirthYear(self):
        return self._birthYear

    @property
    def getBirthMonth(self):
        return self._birthMonth

    @property
    def getBirthDay(self):
        return self._birthDay

    # Creates a string combination of the player's date of birth
    @property
    def getDateOfBirth(self):
        dateOfBirth = "%s/%s/%s".format(self._birthMonth, self._birthDay, self._birthYear)
        return dateOfBirth

    @property
    def getAge(self):
        currentTime = datetime.datetime.now()
        birthYear = int(Player.getBirthYear)
        birthMonth = int(Player.getBirthMonth)
        birthDay = Player.getBirthDay
        hadBirthday = False

        if currentTime.month == birthMonth & currentTime.day == birthDay:
            hadBirthday = True
            age = currentTime.year - birthYear

        if not hadBirthday:
            age = (currentTime.year - birthYear) - 1
            return age
        else:
            hadBirthday = False
            return age
