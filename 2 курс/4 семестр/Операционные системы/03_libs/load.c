#include <dlfcn.h>
#include <stdio.h>

int main(int argc, char *argv[])
{
    void *handle;
    void (*pprint)(char*);

    handle = dlopen("./libpprint.so", RTLD_LAZY);
    if ( NULL == (handle) ) {
	fprintf(stderr, "Ошибка загрузки библиотеки: %s\n", dlerror());
	return -1;
    }
 
    pprint = (void (*)(char*)) dlsym(handle, "pprint");

    if ( NULL != pprint ) {
	pprint("Hello, world!");
    } else {
	fprintf(stderr, "Ошибка получения функции: %s\n", dlerror());
    }
    
    dlclose(handle);
    return  ( NULL == pprint ) ? (-1) : (0);
}
