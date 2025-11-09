grammar TurismoLang;

// ----------- Reglas Sintácticas -----------

program        : scene+ EOF ;
scene          : ESCENA ID '{' dialogue+ '}' ;
dialogue       : decir | opcion ;
decir          : DECIR STRING ';' ;
opcion         : OPCION STRING IR_A ID ';' ;

// ----------- Tokens (Léxico) -----------

ESCENA         : 'escena' ;
DECIR          : 'decir' ;
OPCION         : 'opcion' ;
IR_A           : 'ir_a' ;

ID             : [a-zA-Z_][a-zA-Z0-9_]* ;
STRING         : '"' (~["\r\n])* '"' ;

WS             : [ \t\r\n]+ -> skip ;
COMMENT        : '//' ~[\r\n]* -> skip ;
