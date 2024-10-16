grammar FourierTransform;

// Reglas de entrada
program: statement* EOF;

statement: assignment ';'  // Declaración de asignación
          | functionCall ';' // Llamada a función
          ;

assignment: IDENTIFIER '=' expression;

functionCall: IDENTIFIER '(' arguments ')';

arguments: expression (',' expression)*; // Argumentos separados por coma

expression: 
      IDENTIFIER // variables
    | INT         // enteros
    | list        // lista de números
    | functionCall; // llamada a funciones

list: '[' (INT (',' INT)*)? ']'; // lista de enteros

IDENTIFIER: [a-zA-Z_][a-zA-Z0-9_]*;
INT: [0-9]+;
WS: [ \t\r\n]+ -> skip; // ignorar espacios en blanco
