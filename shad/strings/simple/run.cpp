#include <iostream>

using namespace std;

int main() {
	char myChar = 'a';
	char myString[] = "abcd";
	char anotherString[] = {'a', 'b', 'c', 'd', '\0'};

	cout << sizeof(myChar) << endl;
	cout << sizeof(myString) << endl;
	cout << sizeof(anotherString) << endl;

	return 0;
}