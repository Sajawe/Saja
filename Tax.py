 //      income                 Tax
 //      38.000                 30%
 //      38.000 - 50.000        5%
 //      50.000 - Above         5%
 //      Note that there is no income tax below 38.000 . Take income amount
 //      as an input from the user.

 // tax= tax + %(income-baseprice)

#include<stdio.h>

int main()
{
    int tax, income;
    printf("Enter your income\n");
    scanf("%d",&income);
    
    if(income>=38000 && income<50000){
        tax= tax + 0.30*(income-38000);
    }
    if(income>=38000 && income<50000){
        tax= tax + 0.5*(income-38000);

    if(income>=38000 && income<50000)
        tax= tax + 0.05*(income-38000);
    }    
    return 0;
}

