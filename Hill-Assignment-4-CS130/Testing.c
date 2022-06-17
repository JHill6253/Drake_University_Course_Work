#include <stdio.h>
#include<stdlib.h>
#include<string.h>


char* string_repeater(char[], int num);


int main()
{
    char word[100], st2[10];
    int num;


    
    printf("\n Enter string to repeat: ");
    scanf("%s" , &word);
    printf("\n Enter Number of times to repeat:  ");
    scanf("%d", &num);
    printf("\nRepeating %s %d times...",word, num );

    
    
    //Scanner used to keep exe open 
    scanf("%s", &st2);
    return 0;
}



//problem 2
char* string_repeater(char *s, int num)
{

}
    

//gcc –Wall problem.c –o sssstrlibs