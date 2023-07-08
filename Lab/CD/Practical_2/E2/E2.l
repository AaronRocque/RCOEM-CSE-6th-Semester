%{
    #include "y.tab.h"    
%}

%%

0 {yylval = atoi(yytext); return ZERO;}

1 {yylval = atoi(yytext); return ONE;}

\n {return NL;}

. {return yytext[0];}

%%