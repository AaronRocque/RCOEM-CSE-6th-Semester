/* Design a lexical analyzer to identify the tokens such as keywords, identifiers, operators,
symbols and strings for C language using LEX. */

/* ----------Definition Section---------- */
%{
    #include<stdio.h>
%}

/* ----------Rules Section---------- */
%%

auto|break|case|char|const|continue|default|do|double|else|enum|extern|float|for|goto|if|int|long|register|return|short|signed|sizeof|static|struct|switch|typedef|union|unsigned|void|volatile|while|_Packed  {ECHO; printf("\tKEYWORD\n");}

\".*\" {ECHO; printf("\tSTRING\n");}

[0-9]* {ECHO; printf("\tINTEGER\n");}

[0-9]*\.?[0-9]* {ECHO; printf("\tFLOAT\n");}

[a-zA-z]([a-zA-z]|[0-9])* {ECHO; printf("\tIDENTIFIER\n");}

[\+\-\*\\\%<>=!&\|\^\?] {ECHO; printf("\tOPERATOR\n");}

[{};,()] {ECHO; printf("\tSYMBOL\n");}

%%

/* ----------Subroutine Section---------- */
int yywrap() {
       return(1);
}

int main() {
    yyin = fopen("myfile.txt","r");
    yylex();
    return 0;
}