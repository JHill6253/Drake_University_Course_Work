/*
Author: John Hill
Date: October 3rd, 2020
Title: Assignment 4
Description: Basic Functions for high level programming languages written in low level
    scripting language C for CS 130 at Drake University in Des Moine, Iowa. 
Functions: Main, stringcompare, string_upper, and string_repeater
*/


//include calls to use different functions for C programming 
#include <stdio.h>
#include<stdlib.h>
#include<string.h>

//funtion prototype declarations 
int stringCompare(char[], char[]);  //uses two char arrays 
void string_upper(char[]); // uses one char array also is void as it does not return a value 
char* string_repeater(char[], int num); //uses a char array and int 

// Constructor/driver for code. Simple UI using terminal line to interact with client
int main()
{       
    // decloration of char and int varaibles 
    // st1 and st2 used in string comparison //st3 used for string upper call // word is used for string repeater
    char st1[100], st2[100], st3[100], word[100];
    int different, num, choice; // choice is the selector for the user interface // num is the number of times to repeat in string repeat 
    // different is the varible that stores the "boolean" to determine if strings were compared in the user interface 

    // simple do to start user interface 
    do {
        //user interface menu
        printf("\n");
        printf("Select a program to run: \n");
        printf("\n\t 1. String Compare ");
        printf("\n\t 2. String to Upper ");
        printf("\n\t 3. Repeat String ");
        printf("\n\t 4. Exit \n" );
        //assigns int from user input to choice var 
        scanf("%d", &choice);
    } while (choice < 1 || choice > 4); // while choice consdition to set loop for userinterface 
    //switch allows simple transistion between cases 
    switch (choice)
    {
    case(1):
    //calls to gain requirments
        printf("\nEnter string 1: \n ");
        scanf("%s",&st1);

        printf("\nEnter String 2: \n ");
        scanf("%s",&st2);
        //assigning result from string compare
        different = stringCompare(st1, st2);
        //if to check "Boolean" for truth for user interface 
        if(different == 1)
            printf("Strings are the same! \n");
        // if "boolean" is false this will be displayed to UI
        else
            printf("Strings are different!\n");
        break; // break to signify end of case 
    case(2):
            //user interface to collect requiremnts for string upper and return
            printf("\n Enter a string to convert to uppercase: \n");
            scanf("%s",&st3);
            string_upper(st3);
            printf("\n The string in uppercase: %s \n ",st3);
        break;
    case(3):
            //user interface requiremnt gathering collecting string value and int 
            printf("\nEnter string to repeat: \n");
            scanf("%s", &word); //would have prefered to use fgets but was running into issues when trying to use scanf after
            printf("\nEnter Number of times to repeat:\n");
            scanf("%d", &num);
            printf("\nRepeating %s %d times...\n",word, num );
            printf(" Your new string is: %s \n ", string_repeater(word,num) );
        break;
    case(4):
            printf("Smell ya later");
            exit(0);
        break;

    default:
        printf("Smell ya later");
        exit(0);
        break;
    }
}


//Problem 1
// parameters are two string memory locations s1 and s2 
int stringCompare(char *s1, char *s2)  
{               //diff is used a flag/ comparision variable used to determine if their are differernces to break the loop
    int i = 0, dif = 0; // decloration of I value for "Indexing" of while loop
    while(s1[i] != '\0' && s2[i] != '\0') // while to compare array position i of s1 and s2 to confirm the are not null 
    {   //if to check char array of s1 and s2 for not being the same 
        if(s1[i] != s2[i]) 
        {
            dif = 1; // if not true the dif variable will change to one signifying it is true
            break;
        }
        i++; //i iterates to next position in char arrays 
    }
    if(dif == 0 && s1[i] == '\0' && s2[i] == '\0') //if to signify end of array  and that their were no differences 
    {
        return 1;
    }
    else
    {
        return 0;
    }
}

//problem 2
//parameter memory location of s. with this being void it can only mutate not create
void string_upper(char *s) {
   int i = 0; // i variable set for indexing in while loop 
   
   while (s[i] != '\0') { // while checking to make sure char array position is not null to signify end of array 
      if (s[i] >= 'a' && s[i] <= 'z') { // with char values being assigned a numeric value, we can check to see of the char is lower case
         s[i] = s[i] - 32; // if char is we will set that array index to -32 to assign it as a psotive 
      }
      i++; //iteration 
   }
}

// problem 3
//parameters char *s is memory location of assigned value and int value for num 
char* string_repeater(char *s, int num)
{
    if(num ==0) return NULL; //check if num is null signify no more repeats 
    char *temp = (char *) malloc(sizeof(s)*(num +num)); //setting temporary char addess temp to hold memory address for the size of our string times the value of numer plus number 
    if (temp == NULL) return NULL; //check value of temp 
    strcpy(temp, s); // copy  function in c to create the new values to be added 
    while(num-- > 0) { //continuous decrease in num while it is greater than 0 will add concation with temp and s
        strcat(temp,"");
        strcat(temp,s);
        
    }
    return temp; // return temp as new char
}

// command to create exe file named strlibs 
//gcc strlib.c strlibs