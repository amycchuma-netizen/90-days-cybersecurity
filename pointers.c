#include <stdio.h>
int main(){
int ages[3];
for(int i=0; i<3 ;i++){
    printf("Enter age: ");
    scanf("%d",&ages[i]);
}
int *p = &ages[0];
printf("%d\n",*p);
printf("%p",&p);
}