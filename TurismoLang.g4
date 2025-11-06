grammar TurismoLang;

program        : scene+ EOF ;
scene          : 'escena' ID '{' dialogue+ '}' ;
dialogue       : decir | opcion ;
decir          : 'decir' STRING ';' ;
opcion         : 'opcion' STRING 'ir_a' ID ';' ;

// Tokens
ID             : [a-zA-Z_][a-zA-Z0-9_]* ;
STRING         : '"' (~["\r\n])* '"' ;
WS             : [ \t\r\n]+ -> skip ;
COMMENT        : '//' ~[\r\n]* -> skip ;
