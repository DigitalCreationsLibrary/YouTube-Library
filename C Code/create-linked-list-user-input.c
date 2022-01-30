#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define LINE_SIZE 200
typedef struct Persons {
int id;
char familyName[50];
char firstName[50];
int age;
struct Persons
* next;
} Person;
int main()
{
int i,nPersons;
char buffer[LINE_SIZE], fileName[]="myPersonsList";
Person * onePerson, * nextPerson, * headList;
FILE *myFile;
// Number of Persons in the list (length of the list )
printf("How long is your list (number of Persons )?\n");
scanf("%d",&nPersons);
fgets(buffer,LINE_SIZE,stdin);
//Allocate memory for one Person
nextPerson = (Person *) malloc (sizeof(Person));
headList = nextPerson;
//Read the values from the user input
for (i=0; i<nPersons; i++)
{
//The new element to fill
onePerson = nextPerson;
printf("Person Number %d \n",i+1);
// Id
onePerson->id= i;
// First Name
printf("\tFirst Name :");
fgets(onePerson->firstName,LINE_SIZE,stdin);
strtok(onePerson->firstName,"\n");
// Family Name
printf("\tFamily Name :");
fgets(onePerson->familyName,LINE_SIZE,stdin);
strtok(onePerson->familyName,"\n");
// Age
printf("\tAge :");
scanf("%d",&onePerson->age);
fgets(buffer,LINE_SIZE,stdin);
//Allocate memory for one Person
nextPerson = (Person *) malloc (sizeof(Person));
}
//Link to the next element
onePerson->next = nextPerson;
// The last node of the list
onePerson->next = NULL;
// Traverse and save the List
// The head of the list
printf("Traversing The List:\n--------------------\n");
onePerson = headList;
// create a new file to save the list
myFile = fopen(fileName,"wb");
if (myFile == NULL )
{
printf ("Couldn't create the file \n");
return -1;
}
// Travese and save the list
while (onePerson !=NULL)
{
printf("Person number %d:\n",onePerson->id +1);
printf("\tID :%d\n",onePerson->id);
printf("\tFirst Name :%s\n", onePerson->firstName);
printf("\tFamily Name :%s\n",onePerson->familyName);
printf("\tAge :%d\n",onePerson->age);
fwrite(onePerson,sizeof(Person),1,myFile);
onePerson = onePerson->next;
}
// Close the file
fclose(myFile);
}

