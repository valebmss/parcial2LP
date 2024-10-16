# Generated from FourierTransform.g4 by ANTLR 4.13.0
from antlr4 import *
if "." in __name__:
    from .FourierTransformParser import FourierTransformParser
else:
    from FourierTransformParser import FourierTransformParser

# This class defines a complete listener for a parse tree produced by FourierTransformParser.
class FourierTransformListener(ParseTreeListener):

    # Enter a parse tree produced by FourierTransformParser#program.
    def enterProgram(self, ctx:FourierTransformParser.ProgramContext):
        pass

    # Exit a parse tree produced by FourierTransformParser#program.
    def exitProgram(self, ctx:FourierTransformParser.ProgramContext):
        pass


    # Enter a parse tree produced by FourierTransformParser#statement.
    def enterStatement(self, ctx:FourierTransformParser.StatementContext):
        pass

    # Exit a parse tree produced by FourierTransformParser#statement.
    def exitStatement(self, ctx:FourierTransformParser.StatementContext):
        pass


    # Enter a parse tree produced by FourierTransformParser#assignment.
    def enterAssignment(self, ctx:FourierTransformParser.AssignmentContext):
        pass

    # Exit a parse tree produced by FourierTransformParser#assignment.
    def exitAssignment(self, ctx:FourierTransformParser.AssignmentContext):
        pass


    # Enter a parse tree produced by FourierTransformParser#functionCall.
    def enterFunctionCall(self, ctx:FourierTransformParser.FunctionCallContext):
        pass

    # Exit a parse tree produced by FourierTransformParser#functionCall.
    def exitFunctionCall(self, ctx:FourierTransformParser.FunctionCallContext):
        pass


    # Enter a parse tree produced by FourierTransformParser#arguments.
    def enterArguments(self, ctx:FourierTransformParser.ArgumentsContext):
        pass

    # Exit a parse tree produced by FourierTransformParser#arguments.
    def exitArguments(self, ctx:FourierTransformParser.ArgumentsContext):
        pass


    # Enter a parse tree produced by FourierTransformParser#expression.
    def enterExpression(self, ctx:FourierTransformParser.ExpressionContext):
        pass

    # Exit a parse tree produced by FourierTransformParser#expression.
    def exitExpression(self, ctx:FourierTransformParser.ExpressionContext):
        pass


    # Enter a parse tree produced by FourierTransformParser#list.
    def enterList(self, ctx:FourierTransformParser.ListContext):
        pass

    # Exit a parse tree produced by FourierTransformParser#list.
    def exitList(self, ctx:FourierTransformParser.ListContext):
        pass



del FourierTransformParser