# Generated from Funciones.g4 by ANTLR 4.13.0
from antlr4 import *
if "." in __name__:
    from .FuncionesParser import FuncionesParser
else:
    from FuncionesParser import FuncionesParser

# This class defines a complete generic visitor for a parse tree produced by FuncionesParser.

class FuncionesVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by FuncionesParser#program.
    def visitProgram(self, ctx:FuncionesParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FuncionesParser#statement.
    def visitStatement(self, ctx:FuncionesParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FuncionesParser#assignment.
    def visitAssignment(self, ctx:FuncionesParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FuncionesParser#mapExpr.
    def visitMapExpr(self, ctx:FuncionesParser.MapExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FuncionesParser#filterExpr.
    def visitFilterExpr(self, ctx:FuncionesParser.FilterExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FuncionesParser#iterable.
    def visitIterable(self, ctx:FuncionesParser.IterableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FuncionesParser#list_.
    def visitList_(self, ctx:FuncionesParser.List_Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FuncionesParser#tuple.
    def visitTuple(self, ctx:FuncionesParser.TupleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FuncionesParser#elements.
    def visitElements(self, ctx:FuncionesParser.ElementsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FuncionesParser#expression.
    def visitExpression(self, ctx:FuncionesParser.ExpressionContext):
        return self.visitChildren(ctx)



del FuncionesParser