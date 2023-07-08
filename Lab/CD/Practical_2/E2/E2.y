%{
    #include <stdio.h>
    #include <stdlib.h>
%}

%token ZERO ONE NL

%%

r : s NL {
            printf("\nSequence Accepted\n");
            exit(0);
         };

s : 
    n
|   ZERO a
|   ONE b;

a :
    n a
|   ZERO;

b :
    n b
|   ONE;

n : 
    ZERO
|    ONE;

%%

int yyerror(char *msg)
{
    printf("\nSequence Rejected\n");
    exit(0);
}

int main() 
 {
    printf("\nEnter Sequence of Zeros and Ones : ");
    yyparse();
    return 0;
 }

 int yywrap()
{
    return 1;
}