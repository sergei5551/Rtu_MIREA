#include <stdio.h>


void __attribute__((constructor)) func(){
  puts("BAD CODE");
}

void pprint(char* msg){
  puts(msg);
}

