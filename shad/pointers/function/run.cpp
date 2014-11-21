#include <iostream>

using namespace std;

int add(int a, int b) 
{
	return a + b;
}

int call_pointer_function(int a, int b, int (*add)(int, int)) 
{
	return (*add)(a, b) * a  * b;
}

int main() 
{
	int a = 10;
	int b = 20;
	int (*p)(int, int);
	p = add;

	cout << call_pointer_function(a, b, p) << endl;

	return 0;
}