# Generated from FourierTransform.g4 by ANTLR 4.13.0
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
        4,1,10,67,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,1,0,5,0,16,8,0,10,0,12,0,19,9,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,
        1,3,1,29,8,1,1,2,1,2,1,2,1,2,1,3,1,3,1,3,1,3,1,3,1,4,1,4,1,4,5,4,
        43,8,4,10,4,12,4,46,9,4,1,5,1,5,1,5,1,5,3,5,52,8,5,1,6,1,6,1,6,1,
        6,5,6,58,8,6,10,6,12,6,61,9,6,3,6,63,8,6,1,6,1,6,1,6,0,0,7,0,2,4,
        6,8,10,12,0,0,67,0,17,1,0,0,0,2,28,1,0,0,0,4,30,1,0,0,0,6,34,1,0,
        0,0,8,39,1,0,0,0,10,51,1,0,0,0,12,53,1,0,0,0,14,16,3,2,1,0,15,14,
        1,0,0,0,16,19,1,0,0,0,17,15,1,0,0,0,17,18,1,0,0,0,18,20,1,0,0,0,
        19,17,1,0,0,0,20,21,5,0,0,1,21,1,1,0,0,0,22,23,3,4,2,0,23,24,5,1,
        0,0,24,29,1,0,0,0,25,26,3,6,3,0,26,27,5,1,0,0,27,29,1,0,0,0,28,22,
        1,0,0,0,28,25,1,0,0,0,29,3,1,0,0,0,30,31,5,8,0,0,31,32,5,2,0,0,32,
        33,3,10,5,0,33,5,1,0,0,0,34,35,5,8,0,0,35,36,5,3,0,0,36,37,3,8,4,
        0,37,38,5,4,0,0,38,7,1,0,0,0,39,44,3,10,5,0,40,41,5,5,0,0,41,43,
        3,10,5,0,42,40,1,0,0,0,43,46,1,0,0,0,44,42,1,0,0,0,44,45,1,0,0,0,
        45,9,1,0,0,0,46,44,1,0,0,0,47,52,5,8,0,0,48,52,5,9,0,0,49,52,3,12,
        6,0,50,52,3,6,3,0,51,47,1,0,0,0,51,48,1,0,0,0,51,49,1,0,0,0,51,50,
        1,0,0,0,52,11,1,0,0,0,53,62,5,6,0,0,54,59,5,9,0,0,55,56,5,5,0,0,
        56,58,5,9,0,0,57,55,1,0,0,0,58,61,1,0,0,0,59,57,1,0,0,0,59,60,1,
        0,0,0,60,63,1,0,0,0,61,59,1,0,0,0,62,54,1,0,0,0,62,63,1,0,0,0,63,
        64,1,0,0,0,64,65,5,7,0,0,65,13,1,0,0,0,6,17,28,44,51,59,62
    ]

class FourierTransformParser ( Parser ):

    grammarFileName = "FourierTransform.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "';'", "'='", "'('", "')'", "','", "'['", 
                     "']'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "IDENTIFIER", "INT", "WS" ]

    RULE_program = 0
    RULE_statement = 1
    RULE_assignment = 2
    RULE_functionCall = 3
    RULE_arguments = 4
    RULE_expression = 5
    RULE_list = 6

    ruleNames =  [ "program", "statement", "assignment", "functionCall", 
                   "arguments", "expression", "list" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    IDENTIFIER=8
    INT=9
    WS=10

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
            return self.getToken(FourierTransformParser.EOF, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(FourierTransformParser.StatementContext)
            else:
                return self.getTypedRuleContext(FourierTransformParser.StatementContext,i)


        def getRuleIndex(self):
            return FourierTransformParser.RULE_program

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

        localctx = FourierTransformParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 17
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==8:
                self.state = 14
                self.statement()
                self.state = 19
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 20
            self.match(FourierTransformParser.EOF)
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
            return self.getTypedRuleContext(FourierTransformParser.AssignmentContext,0)


        def functionCall(self):
            return self.getTypedRuleContext(FourierTransformParser.FunctionCallContext,0)


        def getRuleIndex(self):
            return FourierTransformParser.RULE_statement

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

        localctx = FourierTransformParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.state = 28
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 22
                self.assignment()
                self.state = 23
                self.match(FourierTransformParser.T__0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 25
                self.functionCall()
                self.state = 26
                self.match(FourierTransformParser.T__0)
                pass


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
            return self.getToken(FourierTransformParser.IDENTIFIER, 0)

        def expression(self):
            return self.getTypedRuleContext(FourierTransformParser.ExpressionContext,0)


        def getRuleIndex(self):
            return FourierTransformParser.RULE_assignment

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

        localctx = FourierTransformParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 30
            self.match(FourierTransformParser.IDENTIFIER)
            self.state = 31
            self.match(FourierTransformParser.T__1)
            self.state = 32
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionCallContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(FourierTransformParser.IDENTIFIER, 0)

        def arguments(self):
            return self.getTypedRuleContext(FourierTransformParser.ArgumentsContext,0)


        def getRuleIndex(self):
            return FourierTransformParser.RULE_functionCall

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionCall" ):
                listener.enterFunctionCall(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionCall" ):
                listener.exitFunctionCall(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctionCall" ):
                return visitor.visitFunctionCall(self)
            else:
                return visitor.visitChildren(self)




    def functionCall(self):

        localctx = FourierTransformParser.FunctionCallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_functionCall)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 34
            self.match(FourierTransformParser.IDENTIFIER)
            self.state = 35
            self.match(FourierTransformParser.T__2)
            self.state = 36
            self.arguments()
            self.state = 37
            self.match(FourierTransformParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgumentsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(FourierTransformParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(FourierTransformParser.ExpressionContext,i)


        def getRuleIndex(self):
            return FourierTransformParser.RULE_arguments

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArguments" ):
                listener.enterArguments(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArguments" ):
                listener.exitArguments(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArguments" ):
                return visitor.visitArguments(self)
            else:
                return visitor.visitChildren(self)




    def arguments(self):

        localctx = FourierTransformParser.ArgumentsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_arguments)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 39
            self.expression()
            self.state = 44
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==5:
                self.state = 40
                self.match(FourierTransformParser.T__4)
                self.state = 41
                self.expression()
                self.state = 46
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

        def IDENTIFIER(self):
            return self.getToken(FourierTransformParser.IDENTIFIER, 0)

        def INT(self):
            return self.getToken(FourierTransformParser.INT, 0)

        def list_(self):
            return self.getTypedRuleContext(FourierTransformParser.ListContext,0)


        def functionCall(self):
            return self.getTypedRuleContext(FourierTransformParser.FunctionCallContext,0)


        def getRuleIndex(self):
            return FourierTransformParser.RULE_expression

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

        localctx = FourierTransformParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_expression)
        try:
            self.state = 51
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 47
                self.match(FourierTransformParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 48
                self.match(FourierTransformParser.INT)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 49
                self.list_()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 50
                self.functionCall()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self, i:int=None):
            if i is None:
                return self.getTokens(FourierTransformParser.INT)
            else:
                return self.getToken(FourierTransformParser.INT, i)

        def getRuleIndex(self):
            return FourierTransformParser.RULE_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterList" ):
                listener.enterList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitList" ):
                listener.exitList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList" ):
                return visitor.visitList(self)
            else:
                return visitor.visitChildren(self)




    def list_(self):

        localctx = FourierTransformParser.ListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 53
            self.match(FourierTransformParser.T__5)
            self.state = 62
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==9:
                self.state = 54
                self.match(FourierTransformParser.INT)
                self.state = 59
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==5:
                    self.state = 55
                    self.match(FourierTransformParser.T__4)
                    self.state = 56
                    self.match(FourierTransformParser.INT)
                    self.state = 61
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 64
            self.match(FourierTransformParser.T__6)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





