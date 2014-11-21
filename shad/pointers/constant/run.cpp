#include <iostream>

using namespace std;

void const_pointer() {
	int var1 = 0, var2 = 0;
	int *const p = &var1;
	
	p = &var2;

	cout << *p << endl;
}

void pointer_to_const() {
	int var1 = 0;
	const int *p = &var1;

	*p = 1;

	cout << *p << endl;	
}

void const_pointer_to_const() {
	int var1 = 0, var2 = 0;
	const int *const p = &var1;

	*p = 1;
	p = &var2;

	cout << *p << endl;
}

int main() {
	const_pointer();
	pointer_to_const();
	const_pointer_to_const();

	return 0;
}