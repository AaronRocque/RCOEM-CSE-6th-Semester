/* . */

/* ----------Definition Section---------- */
%{
    #include<stdio.h>
    #include<string.h>
    int male = 0;
    int female = 0;
    int tcs = 0;
    int infosys = 0;
    int wipro = 0;
    int accenture = 0;
    int informatica = 0;
    int cse = 0;
    int it = 0;
    int ec = 0;
%}

/* ----------Rules Section---------- */
%%

"Male" {male++;}

"Female" {female++;}

"TCS" {tcs++;}

"Infosys" {infosys++;}

"Wipro" {wipro++;}

"Accenture" {accenture++;}

"Informatica" {informatica++;}

"CSE" {cse++;}

"IT" {it++;}

"EC" {ec++;}

[A-Za-z]+ {printf("\nName: %s\n", yytext);}

[0-9]\.[0-9]+ {printf("CGPA: %s\n", yytext);}

[0-9]{10} {printf("Mobile Number: %s\n", yytext);}

[0-9]+ {printf("Package: %s\n", yytext);}

[a-zA-Z0-9]+.[@].[a-zA-Z0-9]+.[/.].[a-zA-Z.]+ {printf("Email: %s\n", yytext);}

%%

/* ----------Subroutine Section---------- */
int yywrap() {
       return(1);
}

int main(void) {
    yyin = fopen("input.txt","r");
    yylex();
    printf("\nThe number of Female students are %d\n", female);
    printf("The number of Male students are %d\n", male);
    printf("The number of placed in TCS are %d\n", tcs);
    printf("The number of placed in Infosys are %d\n", infosys);
    printf("The number of placed in Wipro are %d\n", wipro);
    printf("The number of placed in Accenture are %d\n", accenture);
    printf("The number of placed in Informatica are %d\n", informatica);
    printf("The number of CSE students placed are %d\n", cse);
    printf("The number of IT students placed are %d\n", it);
    printf("The number of EC students placed are %d\n", ec);
    return 0;
}