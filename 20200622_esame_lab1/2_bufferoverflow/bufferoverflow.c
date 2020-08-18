#include <stdio.h>

//sudo sysctl -w kernel.randomize_va_space=0
//gcc -fno-stack-protector -z execstack bof1.c -o bof1
int main(int argc, char **argv) {

	int flag;
	int isadmin;
	int islogged;
	char secret[100];
	char username[10];
	FILE *adminfile;

	printf("Insert your username:");
	gets(username);

	if((strcmp(username, "administrator") == 0 || islogged == 0x4841434B) && isadmin != 0x01020304){
		printf("Logged succesfully\n");
		
		adminfile = fopen("adminfile", "r");
		fread(secret, sizeof(char), 128, adminfile);

		printf("is admin %x - %x\n", &isadmin, isadmin);
		printf("flag %x - %x\n", &flag, flag);
	
		if(isadmin == 0x01020304 && flag == 0x50415353){
			printf("You win!\n");
			return;
		}
		
		printf("You're normal user\n");
	}

	printf("Username not valid\n");		
	return 0;
}
