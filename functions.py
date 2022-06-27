"""
This module is used to make calls to and from the Database
"""

from database import cursor, db


def getDealerID(name):
    sql = "SELECT dealerID FROM dealer WHERE name = '{}'".format(name.capitalize())
    cursor.execute(sql)
    id = cursor.fetchone()
    for dealerID in id:
        return dealerID

