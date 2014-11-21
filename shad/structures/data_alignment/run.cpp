#include <iostream>

using namespace std;

struct ST1 {
    char c1;
    short s;
    char c2;
    double d;
    int i;
} st1;

struct ST2 {
    double d;
    int i;
    short s;
    char c1;
    char c2;
} st2;

struct ST3 {
	char c1;
	char c2;	
	char c3;
	int i;	
} st3;

int main() {

	cout << sizeof(st1) << endl;
	cout << sizeof(st2) << endl;
	cout << sizeof(st3) << endl;	

	return 0;
}