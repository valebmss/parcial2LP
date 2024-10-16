import sys
from antlr4 import *
from FourierTransformLexer import FourierTransformLexer
from FourierTransformParser import FourierTransformParser
from FourierTransformVisitor import FourierTransformVisitor
import numpy as np

class Evaluator(FourierTransformVisitor):
    def __init__(self):
        self.variables = {}

    def visitAssignment(self, ctx):
        var_name = ctx.IDENTIFIER().getText()
        value = self.visit(ctx.expression())
        self.variables[var_name] = value
        return value

    def visitFunctionCall(self, ctx):
        func_name = ctx.IDENTIFIER().getText()
        args = self.visit(ctx.arguments())
        print(f"Llamada a la función: {func_name} con argumentos: {args}")  # Depuración
        if func_name == "fft":
            if not args:
                raise ValueError("No se proporcionaron argumentos para fft.")
            return self.fft_function(args)
        return None

    def visitExpression(self, ctx):
        if ctx.functionCall():
            return self.visitFunctionCall(ctx.functionCall())
        elif ctx.list():
            return self.visitList(ctx.list())
        elif ctx.INT():
            return int(ctx.INT().getText())
        return None

    def visitList(self, ctx):
        return [int(num.getText()) for num in ctx.INT()]

    def fft_function(self, data):
        if not isinstance(data, list) or not all(isinstance(x, (int, float)) for x in data):
            raise ValueError("Se esperaba una lista de números para FFT.")
        return np.fft.fft(data)

    def visitArguments(self, ctx):
        if ctx.expression():
            return [self.visit(expr) for expr in ctx.expression()]
        return []

def main():
    # Verifica que haya al menos un argumento
    if len(sys.argv) < 2:
        print("Uso: python evaluate_fourier.py <número1> <número2> ... <númeroN>")
        sys.exit(1)

    # Convierte los argumentos a una lista de números
    numbers = list(map(float, sys.argv[1:]))  # Convierte a float para manejar decimales

    evaluator = Evaluator()
    # Llama a la función FFT directamente con los números
    result = evaluator.fft_function(numbers)
    print("Resultado de FFT:", result)

if __name__ == '__main__':
    main()
