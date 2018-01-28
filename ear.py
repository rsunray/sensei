# -*- coding: utf8 -*-

""" imports """
from nltk.tokenize.api import StringTokenizer
from nltk.tokenize.moses import MosesTokenizer

""" input """
aMessage = "Hi, how are you?"

""" process """
raw = aMessage
stringTokenizer = StringTokenizer()
mosesTokenizer = MosesTokenizer()
sTokenizer._string = " "
mTokenizer._string = " "
sTokens = stringTokenizer.tokenize(raw)
mTokens = mosesTokenizer.tokenize(raw)

""" output """
print(sSokens)
print(mTokens)
