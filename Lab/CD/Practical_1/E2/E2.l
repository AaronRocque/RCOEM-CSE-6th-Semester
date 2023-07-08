/* Write a Lex program to find the parameters given below. Consider as input a question paper
of an examination and find:
Date of examination, semester, number of questions, numbers of words, lines, small letters,
capital letters, digits, and special characters. */

/* ----------Definition Section---------- */
%{
    #include<stdio.h>
    #include<string.h>
    int words = 0;
    int qno = 0;
    int lines = 0;
    int smallLetters = 0;
    int capitalLetters = 0;
    int digits = 0;
    int specialChar = 0;
%}

digit [0-9]

special [:|,|\?|//]

/* ----------Rules Section---------- */
%%

\n {lines++; words++;}

[\t ' '] {words++;}

[A-Z] {capitalLetters++;}

[a-z] {smallLetters++;}

{digit} {digits++;}

[0-9]\/[0-9]\/[0-9][0-9][0-9][0-9] {ECHO; printf("\tDATE\n");}

Sem.* {ECHO; printf(" are semester numbers.\n");}

Question{digit} {qno++;}

{special} {specialChar++;}

%%

/* ----------Subroutine Section---------- */
int yywrap() {
       return(1);
}

int main(void) {
    yyin = fopen("QuestionPaper.txt","r");
    yylex();
    printf("\nThe number of questions are %d\n", qno);
    printf("The number of words are %d\n", words);
    printf("The number of lines are %d\n", lines);
    printf("The number of small letters are %d\n", smallLetters);
    printf("The number of capital letters are %d\n", capitalLetters);
    printf("The number of digits are %d\n", digits);
    printf("The number of special characters are %d\n", specialChar);
    
    return 0;
}