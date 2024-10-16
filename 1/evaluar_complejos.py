import sys
from antlr4 import *
from ComplejosLexer import ComplejosLexer
from ComplejosParser import ComplejosParser
from ComplejosVisitor import ComplejosVisitor

class EvaluadorComplejos(ComplejosVisitor):
    def visitExpr(self, ctx):
        print("Visitando Expr")
        return self.visit(ctx.complexExpr())

    def visitSuma(self, ctx):
        print("Visitando Suma")
        left = self.visit(ctx.complexExpr(0))
        right = self.visit(ctx.complexExpr(1))
        print(f"Suma: {left} + {right}")
        return (left[0] + right[0], left[1] + right[1])

    def visitResta(self, ctx):
        print("Visitando Resta")
        left = self.visit(ctx.complexExpr(0))
        right = self.visit(ctx.complexExpr(1))
        print(f"Resta: {left} - {right}")
        return (left[0] - right[0], left[1] - right[1])

    def visitParentesis(self, ctx):
        print("Visitando Paréntesis")
        return self.visit(ctx.complexExpr())

    def visitRealConImaginario(self, ctx):
        print("Visitando RealConImaginario")
        real = float(ctx.real().getText())
        if ctx.signo():
            signo = ctx.signo().getText()
            # Acceder correctamente al valor real de 'imaginary'
            imaginary_str = ctx.imaginary().real().getText()
            imaginary = float(imaginary_str)
            if signo == '-':
                imaginary = -imaginary
            print(f"Real: {real}, Signo: {signo}, Imaginario: {imaginary}")
        else:
            imaginary = 0.0
            print(f"Real: {real}, Imaginario: {imaginary}")
        return (real, imaginary)

    def visitSoloImaginario(self, ctx):
        print("Visitando SoloImaginario")
        # Acceder correctamente al valor real de 'imaginary'
        imaginary_str = ctx.imaginary().real().getText()
        imaginary = float(imaginary_str)
        print(f"Imaginario: {imaginary}")
        return (0.0, imaginary)

    def visitComplejoSimple(self, ctx):
        print("Visitando ComplejoSimple")
        return self.visit(ctx.complejo())

def main():
    if len(sys.argv) < 2:
        print("Ejemplo de uso <3: python evaluar_complejos.py \"(2 + 7i) + (3 - 4i)\"")
        return

    input_expr = sys.argv[1]
    input_stream = InputStream(input_expr)
    lexer = ComplejosLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = ComplejosParser(stream)
    tree = parser.expr()

    print("Árbol de Análisis Sintáctico:")
    print(tree.toStringTree(recog=parser))

    evaluator = EvaluadorComplejos()
    result = evaluator.visit(tree)
    print(f"Resultado de la Evaluación: {result}")

    if result is None:
        print("Error: La evaluación no devovio nada.")
        return

    real, imag = result
    # Formatear la salida
    if imag >= 0:
        print(f"Resultado: {real} + {imag}i")
    else:
        print(f"Resultado: {real} - {abs(imag)}i")

if __name__ == '__main__':
    main()
