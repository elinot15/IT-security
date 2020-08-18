#include <stdio.h>
#include <string.h>

int printName(char *str) {
	char name[128];
	
	strcpy(name, str);
	printf("name addr: %x\n", &name);
	printf("name: %s\n", name);

    	return 0;
}

int main(int argc, char *argv[]) {
    	
	char offset[32];
	int flag = 0;
	char buffer[32];

	gets(buffer);
	printf("flag: %x\n - %x\n", &flag,flag);
	if(flag == 0x61626364)
		printName(argv[1]);
	
    	return 0;
}
