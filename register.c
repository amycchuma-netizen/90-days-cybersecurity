#include <stdio.h>
int main(){
    printf("Welcome to the registration system\n");
    char name [50];
    printf("Enter your name : ");
    scanf("%49s",name);
    int age;
    do
    {
      printf("Enter your age: "); 
      scanf("%d",&age);
    } while
     (age<=1 || age >=120);
    int pin;
    do
    {
        printf("Enter pin :");
    scanf("%d",&pin);
    }
    while ( pin<1000 || pin >9999);
    int password;
    printf("Enter password: ");
    scanf("%d",&password);
    int pascode;
    printf("Enter password: ");
    scanf("%d",&pascode);
if (password == pascode)
{ 
    printf("Correct password.");
}
else  
{
    printf("Incorrect password: ");
}
    return 0;
}