"""
This Module is used for validating information throughout the Black Jack game
"""
import re
from database import cursor, db
import mysql.connector
import functions as f
from player import Player
from dealer import Dealer


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


# Function to check if Username and Password match in the Database
def checkLogin(username, password):
    sql = '''SELECT count(*) FROM player p WHERE p.username = %s AND p.password = %s'''
    vals = (username, password,)

    try:
        cursor.execute(sql, vals)
        for count in cursor.fetchall():
            if count[0] < 1:
                print("\nSorry. You have entered an invalid Username or Password.\nPlease try again!\n")
                return -1
            else:
                return 1
    except mysql.connector.Error as err:
        print(err)
        f.systemShutdown()


# Function to determine if Player's Username is already taken when trying to Register
def isAvailable(username):
    sql = '''SELECT count(username) FROM player p WHERE p.username = %s'''
    vals = (username,)

    try:
        cursor.execute(sql, vals)
        for count in cursor.fetchall():
            if count > 1:
                print("I'm sorry. That Username is already in use. Please try again")
                return -1
            else:
                return 1
    except mysql.connector.Error as err:
        print(err)
        f.systemShutdown()


# Function to check if Player has enough Chips to play
def checkChips(player, dealer):
    dealerName = dealer.getDealerName
    dealerID = f.getDealerID(dealerName)
    needMoreChips = f.getDealerSayings(dealerID, "needMoreChips")
    playerChips = f.getPlayerChips(player)

    # player.chips holds a value but will not compare to 0 for some reason...
    if playerChips <= 0:
        print(needMoreChips[0])
        return -1
    else:
        return 1


# Doing some testing to ensure my Functions work as I write them
username = input("Please enter your Username:\t")
password = input("Please enter your Password:\t")
rv = checkLogin(username, password)
if rv != 1:
    f.systemShutdown()
playerAttributes = []

attributes = f.getPlayerAttributes(username, password, playerAttributes)
player = Player(*attributes)
print("Which dealer would you like to play against?\n")
f.getAllDealerNames()
dealerName = input("\nPlease select now:\t")
dealerID = f.getDealerID(dealerName)
hasSpeech = f.dealerHasSpeech(dealerID)
dealer = Dealer(dealerName, hasSpeech)

rv = checkChips(player, dealer)
if rv != 1:
    f.systemShutdown()
else:
    print("Play Ball!")
    print(player.chips)
