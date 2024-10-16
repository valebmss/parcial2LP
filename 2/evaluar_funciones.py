import sys
from antlr4 import *
from FuncionesLexer import FuncionesLexer
from FuncionesParser import FuncionesParser
from FuncionesVisitor import FuncionesVisitor

# Definir las funciones que se pueden usar en MAP y FILTER
def multiple(x):
    return x * 2

def es_par(x):
    return x % 2 == 0

def cuadrado(x):
    return x ** 2

def es_impar(x):
    return x % 2 != 0

FUNCIONES = {
    'multiple': multiple,
    'es_par': es_par,
    'cuadrado': cuadrado,
    'es_impar': es_impar
}

class EvaluadorFunciones(FuncionesVisitor):
    def __init__(self):
        super().__init__()
        self.variables = {}  # Almacena las variables definidas

    def visitProgram(self, ctx):
        for stmt in ctx.statement():
            self.visit(stmt)

    def visitAssignment(self, ctx):
        var_name = ctx.IDENTIFIER().getText()
        iterable = self.visit(ctx.iterable())
        self.variables[var_name] = iterable
        print(f"Asignación: {var_name} = {iterable}")
        return iterable

    def visitMapExpr(self, ctx):
        func_name = ctx.IDENTIFIER().getText()  # Eliminado el índice
        iterable = self.visit(ctx.iterable())
        if func_name not in FUNCIONES:
            print(f"Error: Función '{func_name}' no definida.")
            return None
        funcion = FUNCIONES[func_name]
        resultado = list(map(funcion, iterable))
        print(f"MAP({func_name}, {iterable}) = {resultado}")
        return resultado

    def visitFilterExpr(self, ctx):
        func_name = ctx.IDENTIFIER().getText()  # Eliminado el índice
        iterable = self.visit(ctx.iterable())
        if func_name not in FUNCIONES:
            print(f"Error: Función '{func_name}' no definida.")
            return None
        funcion = FUNCIONES[func_name]
        resultado = list(filter(funcion, iterable))
        print(f"FILTER({func_name}, {iterable}) = {resultado}")
        return resultado

    def visitIterable(self, ctx):
        if ctx.list_():  # Usar list_ en lugar de list
            return self.visit(ctx.list_())
        elif ctx.tuple_():
            return self.visit(ctx.tuple_())
        else:
            var_name = ctx.IDENTIFIER().getText()
            if var_name in self.variables:
                return self.variables[var_name]
            else:
                print(f"Error: Variable '{var_name}' no definida.")
                return None

    def visitList_(self, ctx):
        elements = self.visit(ctx.elements()) if ctx.elements() else []
        return elements

    def visitTuple(self, ctx):
        elements = self.visit(ctx.elements()) if ctx.elements() else []
        return tuple(elements)

    def visitElements(self, ctx):
        return [self.visit(e) for e in ctx.expression()]

    def visitExpression(self, ctx):
        if ctx.INT():
            return int(ctx.INT().getText())
        elif ctx.FLOAT():
            return float(ctx.FLOAT().getText())
        elif ctx.STRING():
            # Eliminar las comillas
            return ctx.STRING().getText()[1:-1]
        else:
            var_name = ctx.IDENTIFIER().getText()
            if var_name in self.variables:
                return self.variables[var_name]
            else:
                print(f"Error: Variable '{var_name}' no definida.")
                return None

def main():
    if len(sys.argv) < 2:
        print("Uso: python evaluar_funciones.py <archivo_de_entrada>")
        return

    input_file = sys.argv[1]
    with open(input_file, 'r') as file:
        input_stream = InputStream(file.read())

    lexer = FuncionesLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = FuncionesParser(stream)
    tree = parser.program()

    evaluator = EvaluadorFunciones()
    evaluator.visit(tree)

if __name__ == '__main__':
    main()
