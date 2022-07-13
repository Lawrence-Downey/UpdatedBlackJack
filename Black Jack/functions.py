"""
This module is used to make calls to and from the Database
"""

from database import cursor, db
from player import Player
import mysql.connector
import sys


def getDealerID(name):
    sql = "SELECT dealerID FROM dealer WHERE name = %s"
    userInput = (name.capitalize(),)

    try:
        cursor.execute(sql, userInput)
        id = cursor.fetchall()
        for dealerID in id:
            return dealerID
    except mysql.connector.Error as err:
        print(err)
        systemShutdown()


def getDealerSayings(dealerID, key):
    sql = "SELECT value FROM dealer_sayings ds WHERE ds.dealerID = %s AND ds.key = %s"
    userInput = (dealerID[0], key,)

    try:
        cursor.execute(sql, userInput)
        sayings = cursor.fetchone()
        for saying in sayings:
            if saying != '':
                print(saying)
                return saying
            else:
                return -1
    except mysql.connector.Error as err:
        print(err)
        systemShutdown()


def getAllDealerNames():
    sql = "SELECT dealerID, name FROM dealer ORDER BY dealerID"

    try:
        cursor.execute(sql)
        names = cursor.fetchall()
        for name in names:
            print("{}. {}".format(name[0], name[1]))
    except mysql.connector.Error as err:
        print(err)
        systemShutdown()


def dealerHasSpeech(dealerID):
    sql = '''SELECT speech FROM dealer where dealerID = %s'''
    vals = dealerID

    try:
        cursor.execute(sql, vals)
        for speech in cursor.fetchone():
            if speech[0] != 'Y' or speech[0] != 'N':
                return -1
            else:
                return speech
    except mysql.connector.Error as err:
        print(err)
        systemShutdown()


def getPlayerMoney(player):
    sql = '''SELECT money FROM player p WHERE p.playerID = %s'''
    playerID = getPlayerID(player)

    try:
        cursor.execute(sql, playerID)
        for money in cursor.fetchone():
            return money
    except mysql.connector.Error as err:
        print(err)
        systemShutdown()

def getPlayerChips(player):
    sql = '''SELECT chips FROM player p WHERE p.playerID = %s'''
    playerID = getPlayerID(player)

    try:
        cursor.execute(sql, playerID)
        for chip in cursor.fetchone():
            return chip
    except mysql.connector.Error as err:
        print(err)
        systemShutdown()


def getPlayerID(player):
    sql = '''SELECT playerID FROM player WHERE username = %s'''
    username = (player.getUsername,)

    try:
        cursor.execute(sql, username)
        playerIDS = cursor.fetchone()
        for playerID in playerIDS:
            return playerID
    except mysql.connector.Error as err:
        print(err)
        systemShutdown()


def updatePlayer(player):
    playerID = getPlayerID(player)
    sql = '''UPDATE player p 
                SET p.firstName = %s,
                    p.middleName = %s,
                    p.lastName = %s, 
                    p.username = %s,
                    p.password = %s,
                    p.birthYear = %s,
                    p.birthMonth = %s,
                    p.birthDay = %s,
                    p.city = %s,
                    p.provState = %s,
                    p.phoneNumber = %s,
                    p.email = %s,
                    p.money = %s,
                    p.chips = %s
                WHERE p.playerID = ''' + str(playerID)

    vals = (
        player.firstName, player.middleName, player.lastName, player.getUsername, player.getPassword,
        player.getBirthYear, player.getBirthMonth, player.getBirthDay, player.city, player.provState,
        player.phoneNumber, player.email, player.money, player.chips,
    )

    try:
        cursor.execute(sql, vals, multi=True)
        db.commit()
        print(player.getUsername + " has been successfully updated!")
    except mysql.connector.Error as err:
        print(err)
        systemShutdown()


def getPlayerAttributes(username, password, playerAttributes):
    vals = (username, password,)
    attributes = '''SELECT * FROM player p WHERE p.username = %s AND p.password = %s'''

    try:
        cursor.execute(attributes, vals)
        colNames = cursor.column_names
        results = cursor.fetchall()
        i = 1
        while i <= len(colNames):
            for result in results:
                match i:
                    case 1:
                        firstName = result[1]
                        playerAttributes.append(firstName)
                    case 2:
                        middleName = result[2]
                        playerAttributes.append(middleName)
                    case 3:
                        lastName = result[3]
                        playerAttributes.append(lastName)
                    case 4:
                        username = result[4]
                        playerAttributes.append(username)
                    case 5:
                        password = result[5]
                        playerAttributes.append(password)
                    case 6:
                        birthYear = result[6]
                        playerAttributes.append(birthYear)
                    case 7:
                        birthMonth = result[7]
                        playerAttributes.append(birthMonth)
                    case 8:
                        birthDay = result[8]
                        playerAttributes.append(birthDay)
                    case 9:
                        city = result[9]
                        playerAttributes.append(city)
                    case 10:
                        provState = result[10]
                        playerAttributes.append(provState)
                    case 11:
                        phoneNumber = result[11]
                        playerAttributes.append(phoneNumber)
                    case 12:
                        email = result[12]
                        playerAttributes.append(email)
                    case 13:
                        money = result[13]
                        playerAttributes.append(money)
                    case 14:
                        chips = result[14]
                        playerAttributes.append(chips)
                i += 1
        return playerAttributes
    except mysql.connector.Error as err:
        print(err)
        systemShutdown()


def systemShutdown():
    print("I'm sorry. Something went wrong.\nSystem will now shutdown.\nGoodbye!")
    sys.exit()
