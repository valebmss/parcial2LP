# Generated from Complejos.g4 by ANTLR 4.13.0
from antlr4 import *
if "." in __name__:
    from .ComplejosParser import ComplejosParser
else:
    from ComplejosParser import ComplejosParser

# This class defines a complete generic visitor for a parse tree produced by ComplejosParser.

class ComplejosVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ComplejosParser#expr.
    def visitExpr(self, ctx:ComplejosParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ComplejosParser#Suma.
    def visitSuma(self, ctx:ComplejosParser.SumaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ComplejosParser#Parentesis.
    def visitParentesis(self, ctx:ComplejosParser.ParentesisContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ComplejosParser#ComplejoSimple.
    def visitComplejoSimple(self, ctx:ComplejosParser.ComplejoSimpleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ComplejosParser#Resta.
    def visitResta(self, ctx:ComplejosParser.RestaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ComplejosParser#RealConImaginario.
    def visitRealConImaginario(self, ctx:ComplejosParser.RealConImaginarioContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ComplejosParser#SoloImaginario.
    def visitSoloImaginario(self, ctx:ComplejosParser.SoloImaginarioContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ComplejosParser#real.
    def visitReal(self, ctx:ComplejosParser.RealContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ComplejosParser#imaginary.
    def visitImaginary(self, ctx:ComplejosParser.ImaginaryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ComplejosParser#signo.
    def visitSigno(self, ctx:ComplejosParser.SignoContext):
        return self.visitChildren(ctx)



del ComplejosParser