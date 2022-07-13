"""
Dealer class
"""

class Dealer:

    def __init__(self, name, hasSpeech):
        self._name = name
        self._hasSpeech = hasSpeech

    @property
    def getDealerName(self):
        return self._name

    @property
    def hasSpeech(self):
        return self._hasSpeech
