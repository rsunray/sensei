# -*- coding: utf8 -*-

""" imports """
from nltk.tokenize.api import StringTokenizer
from nltk.tokenize.moses import MosesTokenizer

""" input """
aMessage = "This is a cooool #dummysmiley: :-) :-P <3 and some arrows < > -> <--"

""" process """
raw = aMessage
sTokenizer = StringTokenizer()
mTokenizer = MosesTokenizer()
sTokenizer._string = " "
sTokens = sTokenizer.tokenize(raw)
mTokens = mTokenizer.tokenize(raw)

""" output """
print(sTokens)
print(mTokens)
