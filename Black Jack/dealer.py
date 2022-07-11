"""
Dealer class
"""

import functions as f

class Dealer:

    def __init__(self, name, hasSpeech):
        self._name = name
        self._hasSpeech = hasSpeech

    @property
    def getSayings(self):
        if self._hasSpeech == "Y":

        else:
            print("The dealer doesn't feel like talking today.")

    @property
    def getDealerName(self):
        return self._name

