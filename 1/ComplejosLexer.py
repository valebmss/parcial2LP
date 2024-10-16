# Generated from Complejos.g4 by ANTLR 4.13.0
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,8,50,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,
        6,7,6,2,7,7,7,1,0,1,0,1,1,4,1,21,8,1,11,1,12,1,22,1,2,4,2,26,8,2,
        11,2,12,2,27,1,2,1,2,4,2,32,8,2,11,2,12,2,33,1,3,1,3,1,4,1,4,1,5,
        1,5,1,6,1,6,1,7,4,7,45,8,7,11,7,12,7,46,1,7,1,7,0,0,8,1,1,3,2,5,
        3,7,4,9,5,11,6,13,7,15,8,1,0,2,1,0,48,57,3,0,9,10,13,13,32,32,53,
        0,1,1,0,0,0,0,3,1,0,0,0,0,5,1,0,0,0,0,7,1,0,0,0,0,9,1,0,0,0,0,11,
        1,0,0,0,0,13,1,0,0,0,0,15,1,0,0,0,1,17,1,0,0,0,3,20,1,0,0,0,5,25,
        1,0,0,0,7,35,1,0,0,0,9,37,1,0,0,0,11,39,1,0,0,0,13,41,1,0,0,0,15,
        44,1,0,0,0,17,18,5,105,0,0,18,2,1,0,0,0,19,21,7,0,0,0,20,19,1,0,
        0,0,21,22,1,0,0,0,22,20,1,0,0,0,22,23,1,0,0,0,23,4,1,0,0,0,24,26,
        7,0,0,0,25,24,1,0,0,0,26,27,1,0,0,0,27,25,1,0,0,0,27,28,1,0,0,0,
        28,29,1,0,0,0,29,31,5,46,0,0,30,32,7,0,0,0,31,30,1,0,0,0,32,33,1,
        0,0,0,33,31,1,0,0,0,33,34,1,0,0,0,34,6,1,0,0,0,35,36,5,43,0,0,36,
        8,1,0,0,0,37,38,5,45,0,0,38,10,1,0,0,0,39,40,5,40,0,0,40,12,1,0,
        0,0,41,42,5,41,0,0,42,14,1,0,0,0,43,45,7,1,0,0,44,43,1,0,0,0,45,
        46,1,0,0,0,46,44,1,0,0,0,46,47,1,0,0,0,47,48,1,0,0,0,48,49,6,7,0,
        0,49,16,1,0,0,0,5,0,22,27,33,46,1,6,0,0
    ]

class ComplejosLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    INT = 2
    FLOAT = 3
    PLUS = 4
    MINUS = 5
    LPAREN = 6
    RPAREN = 7
    WS = 8

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'i'", "'+'", "'-'", "'('", "')'" ]

    symbolicNames = [ "<INVALID>",
            "INT", "FLOAT", "PLUS", "MINUS", "LPAREN", "RPAREN", "WS" ]

    ruleNames = [ "T__0", "INT", "FLOAT", "PLUS", "MINUS", "LPAREN", "RPAREN", 
                  "WS" ]

    grammarFileName = "Complejos.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.0")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


