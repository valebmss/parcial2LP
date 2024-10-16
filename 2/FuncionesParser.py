# Generated from Funciones.g4 by ANTLR 4.13.0
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,15,81,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,1,0,4,0,22,8,0,11,0,12,0,23,1,0,1,0,1,
        1,1,1,1,1,3,1,31,8,1,1,2,1,2,1,2,1,2,1,2,1,3,1,3,1,3,1,3,1,3,1,3,
        1,3,1,3,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,5,1,5,1,5,3,5,57,8,5,1,
        6,1,6,3,6,61,8,6,1,6,1,6,1,7,1,7,3,7,67,8,7,1,7,1,7,1,8,1,8,1,8,
        5,8,74,8,8,10,8,12,8,77,9,8,1,9,1,9,1,9,0,0,10,0,2,4,6,8,10,12,14,
        16,18,0,1,1,0,5,8,78,0,21,1,0,0,0,2,30,1,0,0,0,4,32,1,0,0,0,6,37,
        1,0,0,0,8,45,1,0,0,0,10,56,1,0,0,0,12,58,1,0,0,0,14,64,1,0,0,0,16,
        70,1,0,0,0,18,78,1,0,0,0,20,22,3,2,1,0,21,20,1,0,0,0,22,23,1,0,0,
        0,23,21,1,0,0,0,23,24,1,0,0,0,24,25,1,0,0,0,25,26,5,0,0,1,26,1,1,
        0,0,0,27,31,3,4,2,0,28,31,3,6,3,0,29,31,3,8,4,0,30,27,1,0,0,0,30,
        28,1,0,0,0,30,29,1,0,0,0,31,3,1,0,0,0,32,33,5,5,0,0,33,34,5,13,0,
        0,34,35,3,10,5,0,35,36,5,12,0,0,36,5,1,0,0,0,37,38,5,1,0,0,38,39,
        5,10,0,0,39,40,5,5,0,0,40,41,5,9,0,0,41,42,3,10,5,0,42,43,5,11,0,
        0,43,44,5,12,0,0,44,7,1,0,0,0,45,46,5,2,0,0,46,47,5,10,0,0,47,48,
        5,5,0,0,48,49,5,9,0,0,49,50,3,10,5,0,50,51,5,11,0,0,51,52,5,12,0,
        0,52,9,1,0,0,0,53,57,3,12,6,0,54,57,3,14,7,0,55,57,5,5,0,0,56,53,
        1,0,0,0,56,54,1,0,0,0,56,55,1,0,0,0,57,11,1,0,0,0,58,60,5,3,0,0,
        59,61,3,16,8,0,60,59,1,0,0,0,60,61,1,0,0,0,61,62,1,0,0,0,62,63,5,
        4,0,0,63,13,1,0,0,0,64,66,5,10,0,0,65,67,3,16,8,0,66,65,1,0,0,0,
        66,67,1,0,0,0,67,68,1,0,0,0,68,69,5,11,0,0,69,15,1,0,0,0,70,75,3,
        18,9,0,71,72,5,9,0,0,72,74,3,18,9,0,73,71,1,0,0,0,74,77,1,0,0,0,
        75,73,1,0,0,0,75,76,1,0,0,0,76,17,1,0,0,0,77,75,1,0,0,0,78,79,7,
        0,0,0,79,19,1,0,0,0,6,23,30,56,60,66,75
    ]

class FuncionesParser ( Parser ):

    grammarFileName = "Funciones.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'MAP'", "'FILTER'", "'['", "']'", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "','", "'('", 
                     "')'", "';'", "'='" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "IDENTIFIER", "INT", "FLOAT", "STRING", 
                      "COMMA", "LPAREN", "RPAREN", "SEMI", "EQUAL", "WS", 
                      "COMMENT" ]

    RULE_program = 0
    RULE_statement = 1
    RULE_assignment = 2
    RULE_mapExpr = 3
    RULE_filterExpr = 4
    RULE_iterable = 5
    RULE_list_ = 6
    RULE_tuple = 7
    RULE_elements = 8
    RULE_expression = 9

    ruleNames =  [ "program", "statement", "assignment", "mapExpr", "filterExpr", 
                   "iterable", "list_", "tuple", "elements", "expression" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    IDENTIFIER=5
    INT=6
    FLOAT=7
    STRING=8
    COMMA=9
    LPAREN=10
    RPAREN=11
    SEMI=12
    EQUAL=13
    WS=14
    COMMENT=15

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.0")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(FuncionesParser.EOF, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(FuncionesParser.StatementContext)
            else:
                return self.getTypedRuleContext(FuncionesParser.StatementContext,i)


        def getRuleIndex(self):
            return FuncionesParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = FuncionesParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 21 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 20
                self.statement()
                self.state = 23 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 38) != 0)):
                    break

            self.state = 25
            self.match(FuncionesParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignment(self):
            return self.getTypedRuleContext(FuncionesParser.AssignmentContext,0)


        def mapExpr(self):
            return self.getTypedRuleContext(FuncionesParser.MapExprContext,0)


        def filterExpr(self):
            return self.getTypedRuleContext(FuncionesParser.FilterExprContext,0)


        def getRuleIndex(self):
            return FuncionesParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = FuncionesParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.state = 30
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [5]:
                self.enterOuterAlt(localctx, 1)
                self.state = 27
                self.assignment()
                pass
            elif token in [1]:
                self.enterOuterAlt(localctx, 2)
                self.state = 28
                self.mapExpr()
                pass
            elif token in [2]:
                self.enterOuterAlt(localctx, 3)
                self.state = 29
                self.filterExpr()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(FuncionesParser.IDENTIFIER, 0)

        def EQUAL(self):
            return self.getToken(FuncionesParser.EQUAL, 0)

        def iterable(self):
            return self.getTypedRuleContext(FuncionesParser.IterableContext,0)


        def SEMI(self):
            return self.getToken(FuncionesParser.SEMI, 0)

        def getRuleIndex(self):
            return FuncionesParser.RULE_assignment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignment" ):
                listener.enterAssignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignment" ):
                listener.exitAssignment(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment" ):
                return visitor.visitAssignment(self)
            else:
                return visitor.visitChildren(self)




    def assignment(self):

        localctx = FuncionesParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 32
            self.match(FuncionesParser.IDENTIFIER)
            self.state = 33
            self.match(FuncionesParser.EQUAL)
            self.state = 34
            self.iterable()
            self.state = 35
            self.match(FuncionesParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MapExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LPAREN(self):
            return self.getToken(FuncionesParser.LPAREN, 0)

        def IDENTIFIER(self):
            return self.getToken(FuncionesParser.IDENTIFIER, 0)

        def COMMA(self):
            return self.getToken(FuncionesParser.COMMA, 0)

        def iterable(self):
            return self.getTypedRuleContext(FuncionesParser.IterableContext,0)


        def RPAREN(self):
            return self.getToken(FuncionesParser.RPAREN, 0)

        def SEMI(self):
            return self.getToken(FuncionesParser.SEMI, 0)

        def getRuleIndex(self):
            return FuncionesParser.RULE_mapExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMapExpr" ):
                listener.enterMapExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMapExpr" ):
                listener.exitMapExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMapExpr" ):
                return visitor.visitMapExpr(self)
            else:
                return visitor.visitChildren(self)




    def mapExpr(self):

        localctx = FuncionesParser.MapExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_mapExpr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 37
            self.match(FuncionesParser.T__0)
            self.state = 38
            self.match(FuncionesParser.LPAREN)
            self.state = 39
            self.match(FuncionesParser.IDENTIFIER)
            self.state = 40
            self.match(FuncionesParser.COMMA)
            self.state = 41
            self.iterable()
            self.state = 42
            self.match(FuncionesParser.RPAREN)
            self.state = 43
            self.match(FuncionesParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FilterExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LPAREN(self):
            return self.getToken(FuncionesParser.LPAREN, 0)

        def IDENTIFIER(self):
            return self.getToken(FuncionesParser.IDENTIFIER, 0)

        def COMMA(self):
            return self.getToken(FuncionesParser.COMMA, 0)

        def iterable(self):
            return self.getTypedRuleContext(FuncionesParser.IterableContext,0)


        def RPAREN(self):
            return self.getToken(FuncionesParser.RPAREN, 0)

        def SEMI(self):
            return self.getToken(FuncionesParser.SEMI, 0)

        def getRuleIndex(self):
            return FuncionesParser.RULE_filterExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFilterExpr" ):
                listener.enterFilterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFilterExpr" ):
                listener.exitFilterExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFilterExpr" ):
                return visitor.visitFilterExpr(self)
            else:
                return visitor.visitChildren(self)




    def filterExpr(self):

        localctx = FuncionesParser.FilterExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_filterExpr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 45
            self.match(FuncionesParser.T__1)
            self.state = 46
            self.match(FuncionesParser.LPAREN)
            self.state = 47
            self.match(FuncionesParser.IDENTIFIER)
            self.state = 48
            self.match(FuncionesParser.COMMA)
            self.state = 49
            self.iterable()
            self.state = 50
            self.match(FuncionesParser.RPAREN)
            self.state = 51
            self.match(FuncionesParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IterableContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def list_(self):
            return self.getTypedRuleContext(FuncionesParser.List_Context,0)


        def tuple_(self):
            return self.getTypedRuleContext(FuncionesParser.TupleContext,0)


        def IDENTIFIER(self):
            return self.getToken(FuncionesParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return FuncionesParser.RULE_iterable

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIterable" ):
                listener.enterIterable(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIterable" ):
                listener.exitIterable(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIterable" ):
                return visitor.visitIterable(self)
            else:
                return visitor.visitChildren(self)




    def iterable(self):

        localctx = FuncionesParser.IterableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_iterable)
        try:
            self.state = 56
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3]:
                self.enterOuterAlt(localctx, 1)
                self.state = 53
                self.list_()
                pass
            elif token in [10]:
                self.enterOuterAlt(localctx, 2)
                self.state = 54
                self.tuple_()
                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 3)
                self.state = 55
                self.match(FuncionesParser.IDENTIFIER)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def elements(self):
            return self.getTypedRuleContext(FuncionesParser.ElementsContext,0)


        def getRuleIndex(self):
            return FuncionesParser.RULE_list_

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterList_" ):
                listener.enterList_(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitList_" ):
                listener.exitList_(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_" ):
                return visitor.visitList_(self)
            else:
                return visitor.visitChildren(self)




    def list_(self):

        localctx = FuncionesParser.List_Context(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_list_)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 58
            self.match(FuncionesParser.T__2)
            self.state = 60
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 480) != 0):
                self.state = 59
                self.elements()


            self.state = 62
            self.match(FuncionesParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TupleContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LPAREN(self):
            return self.getToken(FuncionesParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(FuncionesParser.RPAREN, 0)

        def elements(self):
            return self.getTypedRuleContext(FuncionesParser.ElementsContext,0)


        def getRuleIndex(self):
            return FuncionesParser.RULE_tuple

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTuple" ):
                listener.enterTuple(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTuple" ):
                listener.exitTuple(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTuple" ):
                return visitor.visitTuple(self)
            else:
                return visitor.visitChildren(self)




    def tuple_(self):

        localctx = FuncionesParser.TupleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_tuple)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 64
            self.match(FuncionesParser.LPAREN)
            self.state = 66
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 480) != 0):
                self.state = 65
                self.elements()


            self.state = 68
            self.match(FuncionesParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElementsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(FuncionesParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(FuncionesParser.ExpressionContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(FuncionesParser.COMMA)
            else:
                return self.getToken(FuncionesParser.COMMA, i)

        def getRuleIndex(self):
            return FuncionesParser.RULE_elements

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterElements" ):
                listener.enterElements(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitElements" ):
                listener.exitElements(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElements" ):
                return visitor.visitElements(self)
            else:
                return visitor.visitChildren(self)




    def elements(self):

        localctx = FuncionesParser.ElementsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_elements)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 70
            self.expression()
            self.state = 75
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==9:
                self.state = 71
                self.match(FuncionesParser.COMMA)
                self.state = 72
                self.expression()
                self.state = 77
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(FuncionesParser.INT, 0)

        def FLOAT(self):
            return self.getToken(FuncionesParser.FLOAT, 0)

        def STRING(self):
            return self.getToken(FuncionesParser.STRING, 0)

        def IDENTIFIER(self):
            return self.getToken(FuncionesParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return FuncionesParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)




    def expression(self):

        localctx = FuncionesParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 78
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 480) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





