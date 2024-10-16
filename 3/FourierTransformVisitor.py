# Generated from FourierTransform.g4 by ANTLR 4.13.0
from antlr4 import *
if "." in __name__:
    from .FourierTransformParser import FourierTransformParser
else:
    from FourierTransformParser import FourierTransformParser

# This class defines a complete generic visitor for a parse tree produced by FourierTransformParser.

class FourierTransformVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by FourierTransformParser#program.
    def visitProgram(self, ctx:FourierTransformParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FourierTransformParser#statement.
    def visitStatement(self, ctx:FourierTransformParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FourierTransformParser#assignment.
    def visitAssignment(self, ctx:FourierTransformParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FourierTransformParser#functionCall.
    def visitFunctionCall(self, ctx:FourierTransformParser.FunctionCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FourierTransformParser#arguments.
    def visitArguments(self, ctx:FourierTransformParser.ArgumentsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FourierTransformParser#expression.
    def visitExpression(self, ctx:FourierTransformParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FourierTransformParser#list.
    def visitList(self, ctx:FourierTransformParser.ListContext):
        return self.visitChildren(ctx)



del FourierTransformParser