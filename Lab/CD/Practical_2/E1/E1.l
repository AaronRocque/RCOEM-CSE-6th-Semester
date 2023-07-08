%{
    #include "y.tab.h"
%}

%%

[0-9]+ {yylval = atoi(yytext);
        return NUMBER;}

[a-zA-z] {return ID;}

\n {return NL;}

. {return yytext[0];}

%%