#include <iostream>
#include <string>
#include <cstring>

using namespace std;

void cpp_concat() {
	string a = "Hello";
	string b = ", World!";
	string c = a + b;

	cout << c << endl;
}

void c_strcat() {
	char hello[10] = "Hello";
	char world[10] = ", World!";

	strcat(hello, world);

	cout << hello << endl;
}

void c_concat_for() {
	char str1[100] = "Hello";
    char str2[] = ", World!";

	char *p;
	char *q;

	for (p = str1; *p != 0; p++) {}	

	for (q = str2; *q != 0; p++, q++ ) {
		*p = *q;
	}

	cout << str1 << endl;
}

void c_concat_while() {
	char str1[100] = "Hello";
    char str2[] = ", World!";

	char *p;
	char *q;

	p = str1;
	q = str2;
		
	while (*p) {
		p++;
	}	
	
	while (*q) {
		*p = *q;
		p++;
		q++;
	}

	cout << str1 << endl;
}

int main() {
	//cpp_concat();
	//c_strcat();
	c_concat_for();
	c_concat_while();

	return 0;
}