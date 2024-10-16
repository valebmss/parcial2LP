grammar Funciones;

// Punto de entrada
program: (statement)+ EOF;

// Tipos de declaraciones
statement
    : assignment
    | mapExpr
    | filterExpr
    ;

// Asignación de variables
assignment: IDENTIFIER '=' iterable ';';

// Expresiones MAP y FILTER
mapExpr: 'MAP' '(' IDENTIFIER ',' iterable ')' ';';
filterExpr: 'FILTER' '(' IDENTIFIER ',' iterable ')' ';';

// Definición de iterables
iterable
    : list_
    | tuple
    | IDENTIFIER
    ;

// Definición de listas
list_: '[' elements? ']';

// Definición de tuplas
tuple: '(' elements? ')';

// Elementos de listas y tuplas
elements: expression (',' expression)*;

// Expresiones básicas
expression
    : INT
    | FLOAT
    | STRING
    | IDENTIFIER
    ;

// Tokens
IDENTIFIER: [a-zA-Z_][a-zA-Z_0-9]*;
INT: [0-9]+;
FLOAT: [0-9]+ '.' [0-9]+;
STRING: '"' (~["\\] | '\\' .)* '"';

// Símbolos
COMMA: ',';
LPAREN: '(';
RPAREN: ')';
SEMI: ';';
EQUAL: '=';

// Ignorar espacios en blanco y comentarios
WS: [ \t\r\n]+ -> skip;
COMMENT: '//' ~[\r\n]* -> skip;
