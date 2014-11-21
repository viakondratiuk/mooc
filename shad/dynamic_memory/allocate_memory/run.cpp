#include <iostream>
#include <stdlib.h>

using namespace std;

void use_malloc_free() {
	int *p;
	p = (int*) malloc(10 * sizeof(int));

	for (int i = 0; i < 10; i++) {
		p[i] = i + 5;
	}

	for (int i = 0; i < 10; i++) {
		cout << p[i] << endl;
	}
	
	free(p);
	cout << p << endl;
	p = NULL;
	cout << p << endl;	
}

void use_new_delete() {
	int *p = new int [10];

	for (int i = 0; i < 10; i++) {
		p[i] = i + 5;
	}

	for (int i = 0; i < 10; i++) {
		cout << p[i] << endl;
	}

	delete[] p;
	cout << p << endl;
	p = NULL;
	cout << p << endl;		
}

int main() {
	//use_malloc();
	use_new_delete();

	return 0;
}