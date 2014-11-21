#include <iostream>

using namespace std;

void strcat(char *dest, char *src) 
{
	while (*dest) dest++;
	while ((*dest++ = *src++));
}

char* mystrcat( char* dest, char* src )
{
     while (*dest) dest++;
     while ((*dest++ = *src++));
     return --dest;
}

int main() {
	//strcat((char*)"Destination", (char*)"Source");

	char bigString[1000];     /* I never know how much to allocate... */
	bigString[0] = '\0';
	strcat(bigString, (char*)"John, ");
	strcat(bigString, (char*)"Paul, ");
	strcat(bigString, (char*)"George, ");
	strcat(bigString, (char*)"Joel ");
	cout << bigString << endl;

	char bigString2[1000];     /* I never know how much to allocate... */
	char *p = bigString2;
	bigString2[0] = '\0';
	p = mystrcat(p, (char*)"John, ");
	p = mystrcat(p, (char*)"Paul, ");
	p = mystrcat(p, (char*)"George, ");
	p = mystrcat(p, (char*)"Joel ");		
	cout << bigString2 << endl;

	return 0;
}