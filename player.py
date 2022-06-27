"""
Player class
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
    def lastName(self, newLastName):
        self._lastname = newLastName

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
        year = self._birthYear
        month = self._birthMonth
        day = self._birthDay

        if len(str(day)) < 2:
            day = "0" + str(day)

        if len(str(month)) < 2:
            month = "0" + str(month)

        dateOfBirth = "{}/{}/{}".format(month, day, year)
        return dateOfBirth

    @property
    def getAge(self):
        currentTime = datetime.datetime.now()
        birthYear = currentTime.year
        birthMonth = currentTime.month
        birthDay = currentTime.day

        if birthDay == self._birthDay & birthMonth == self._birthMonth:
            hadBirthday = True
        elif birthDay >= self._birthDay & birthMonth == self._birthMonth:
            hadBirthday = True
        elif birthMonth > self._birthMonth:
            hadBirthday = True
        else:
            hadBirthday = False

        if hadBirthday:
            return birthYear - self._birthYear
        else:
            return (birthYear - self._birthYear) - 1

    @property
    def provState(self):
        return self._provState

    # Setter to allow change of Province or State
    @provState.setter
    def provState(self, newProvState):
        self._provState = newProvState

    @property
    def phoneNumber(self):
        return self._phoneNumber

    # Setter to allow player to update their Phone Number
    @phoneNumber.setter
    def phoneNumber(self, newPhoneNumber):
        self._phoneNumber = newPhoneNumber

    @property
    def email(self):
        return self._email

    # Setter to allow player to update their Email
    @email.setter
    def email(self, newEmail):
        self._email = newEmail

    @property
    def money(self):
        return self._money

    # Setter to make updating Player's account balance possible
    @money.setter
    def money(self, newAmount):
        self._money = newAmount


