"""
Set up for connecting to the database
"""

import mysql.connector

config = {
    "host": "localhost",
    "user": "root",
    "password": "Ernie6660",
    "database": "player_money"
}

# DB name is player_money
db = mysql.connector.connect(**config)
cursor = db.cursor()
