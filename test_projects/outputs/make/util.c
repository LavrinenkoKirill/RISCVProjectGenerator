#include <stdio.h>
#include "util.h"

int factorial(int n){
    if(n!=1){
	return(n * factorial(n-1));
    }
    else return 1;
}

void print_hello(){
   printf("Hello World! ");
}
