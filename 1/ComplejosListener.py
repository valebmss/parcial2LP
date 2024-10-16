# Generated from Complejos.g4 by ANTLR 4.13.0
from antlr4 import *
if "." in __name__:
    from .ComplejosParser import ComplejosParser
else:
    from ComplejosParser import ComplejosParser

# This class defines a complete listener for a parse tree produced by ComplejosParser.
class ComplejosListener(ParseTreeListener):

    # Enter a parse tree produced by ComplejosParser#expr.
    def enterExpr(self, ctx:ComplejosParser.ExprContext):
        pass

    # Exit a parse tree produced by ComplejosParser#expr.
    def exitExpr(self, ctx:ComplejosParser.ExprContext):
        pass


    # Enter a parse tree produced by ComplejosParser#Suma.
    def enterSuma(self, ctx:ComplejosParser.SumaContext):
        pass

    # Exit a parse tree produced by ComplejosParser#Suma.
    def exitSuma(self, ctx:ComplejosParser.SumaContext):
        pass


    # Enter a parse tree produced by ComplejosParser#Parentesis.
    def enterParentesis(self, ctx:ComplejosParser.ParentesisContext):
        pass

    # Exit a parse tree produced by ComplejosParser#Parentesis.
    def exitParentesis(self, ctx:ComplejosParser.ParentesisContext):
        pass


    # Enter a parse tree produced by ComplejosParser#ComplejoSimple.
    def enterComplejoSimple(self, ctx:ComplejosParser.ComplejoSimpleContext):
        pass

    # Exit a parse tree produced by ComplejosParser#ComplejoSimple.
    def exitComplejoSimple(self, ctx:ComplejosParser.ComplejoSimpleContext):
        pass


    # Enter a parse tree produced by ComplejosParser#Resta.
    def enterResta(self, ctx:ComplejosParser.RestaContext):
        pass

    # Exit a parse tree produced by ComplejosParser#Resta.
    def exitResta(self, ctx:ComplejosParser.RestaContext):
        pass


    # Enter a parse tree produced by ComplejosParser#RealConImaginario.
    def enterRealConImaginario(self, ctx:ComplejosParser.RealConImaginarioContext):
        pass

    # Exit a parse tree produced by ComplejosParser#RealConImaginario.
    def exitRealConImaginario(self, ctx:ComplejosParser.RealConImaginarioContext):
        pass


    # Enter a parse tree produced by ComplejosParser#SoloImaginario.
    def enterSoloImaginario(self, ctx:ComplejosParser.SoloImaginarioContext):
        pass

    # Exit a parse tree produced by ComplejosParser#SoloImaginario.
    def exitSoloImaginario(self, ctx:ComplejosParser.SoloImaginarioContext):
        pass


    # Enter a parse tree produced by ComplejosParser#real.
    def enterReal(self, ctx:ComplejosParser.RealContext):
        pass

    # Exit a parse tree produced by ComplejosParser#real.
    def exitReal(self, ctx:ComplejosParser.RealContext):
        pass


    # Enter a parse tree produced by ComplejosParser#imaginary.
    def enterImaginary(self, ctx:ComplejosParser.ImaginaryContext):
        pass

    # Exit a parse tree produced by ComplejosParser#imaginary.
    def exitImaginary(self, ctx:ComplejosParser.ImaginaryContext):
        pass


    # Enter a parse tree produced by ComplejosParser#signo.
    def enterSigno(self, ctx:ComplejosParser.SignoContext):
        pass

    # Exit a parse tree produced by ComplejosParser#signo.
    def exitSigno(self, ctx:ComplejosParser.SignoContext):
        pass



del ComplejosParser