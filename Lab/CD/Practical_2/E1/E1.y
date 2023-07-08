%{
    #include <stdio.h>
    #include <stdlib.h>
    int answer = 0;
%}

%token NUMBER ID NL
%left '+' '-'
%left '*' '/'

%%

stmt : 
    exp NL {    
                printf("Valid Expression\n");
                printf("Answer = %d\n", $1);
                exit(0);
            }
|   exp2 NL {
                printf("Postfix Expression: \n");
                exit(0);
            }
|   exp1 NL {   
                printf("Valid Expression, but Calculation cannot be performed on variables.\n");
                exit(0);
            };

exp:
    exp '+' exp {$$ = $1 + $3;}
|   exp '-' exp {$$ = $1 - $3;}
|   exp '*' exp {$$ = $1 * $3;}
|   exp '/' exp {$$ = $1 / $3;}
|   '(' exp ')' {$$ = $2;}
|   NUMBER {$$ = $1;};
    
exp1: 
    exp1 '+' exp1
|   exp1 '-' exp1		
|   exp1 '*' exp1	
|   exp1 '/' exp1		
|    '(' exp1 ')'
|   ID;

exp2:
    exp2 '+' exp2 {printf("+");}
|   exp2 '-' exp2 {printf("-");}
|   exp2 '*' exp2 {printf("*");}
|   exp2 '/' exp2 {printf("/");}
|   '(' exp2 ')'
|   NUMBER {printf("%d", yylval);};

%%

int yyerror(char *msg)
{
    printf("Invalid Expression\n");
    exit(0);
}

main()
{
    printf("Enter the expression: \n");
    yyparse();
}

int yywrap()
{
    return 1;
}