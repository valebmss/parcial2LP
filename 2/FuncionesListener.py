# Generated from Funciones.g4 by ANTLR 4.13.0
from antlr4 import *
if "." in __name__:
    from .FuncionesParser import FuncionesParser
else:
    from FuncionesParser import FuncionesParser

# This class defines a complete listener for a parse tree produced by FuncionesParser.
class FuncionesListener(ParseTreeListener):

    # Enter a parse tree produced by FuncionesParser#program.
    def enterProgram(self, ctx:FuncionesParser.ProgramContext):
        pass

    # Exit a parse tree produced by FuncionesParser#program.
    def exitProgram(self, ctx:FuncionesParser.ProgramContext):
        pass


    # Enter a parse tree produced by FuncionesParser#statement.
    def enterStatement(self, ctx:FuncionesParser.StatementContext):
        pass

    # Exit a parse tree produced by FuncionesParser#statement.
    def exitStatement(self, ctx:FuncionesParser.StatementContext):
        pass


    # Enter a parse tree produced by FuncionesParser#assignment.
    def enterAssignment(self, ctx:FuncionesParser.AssignmentContext):
        pass

    # Exit a parse tree produced by FuncionesParser#assignment.
    def exitAssignment(self, ctx:FuncionesParser.AssignmentContext):
        pass


    # Enter a parse tree produced by FuncionesParser#mapExpr.
    def enterMapExpr(self, ctx:FuncionesParser.MapExprContext):
        pass

    # Exit a parse tree produced by FuncionesParser#mapExpr.
    def exitMapExpr(self, ctx:FuncionesParser.MapExprContext):
        pass


    # Enter a parse tree produced by FuncionesParser#filterExpr.
    def enterFilterExpr(self, ctx:FuncionesParser.FilterExprContext):
        pass

    # Exit a parse tree produced by FuncionesParser#filterExpr.
    def exitFilterExpr(self, ctx:FuncionesParser.FilterExprContext):
        pass


    # Enter a parse tree produced by FuncionesParser#iterable.
    def enterIterable(self, ctx:FuncionesParser.IterableContext):
        pass

    # Exit a parse tree produced by FuncionesParser#iterable.
    def exitIterable(self, ctx:FuncionesParser.IterableContext):
        pass


    # Enter a parse tree produced by FuncionesParser#list_.
    def enterList_(self, ctx:FuncionesParser.List_Context):
        pass

    # Exit a parse tree produced by FuncionesParser#list_.
    def exitList_(self, ctx:FuncionesParser.List_Context):
        pass


    # Enter a parse tree produced by FuncionesParser#tuple.
    def enterTuple(self, ctx:FuncionesParser.TupleContext):
        pass

    # Exit a parse tree produced by FuncionesParser#tuple.
    def exitTuple(self, ctx:FuncionesParser.TupleContext):
        pass


    # Enter a parse tree produced by FuncionesParser#elements.
    def enterElements(self, ctx:FuncionesParser.ElementsContext):
        pass

    # Exit a parse tree produced by FuncionesParser#elements.
    def exitElements(self, ctx:FuncionesParser.ElementsContext):
        pass


    # Enter a parse tree produced by FuncionesParser#expression.
    def enterExpression(self, ctx:FuncionesParser.ExpressionContext):
        pass

    # Exit a parse tree produced by FuncionesParser#expression.
    def exitExpression(self, ctx:FuncionesParser.ExpressionContext):
        pass



del FuncionesParser