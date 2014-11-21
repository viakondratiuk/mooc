#include <iostream>

using namespace std;

int use_return(int a, int b) 
{
	return a + b;
}

void use_pointer(int a, int b, int *p)
{
	*p = a + b;
}

void use_reference(int a, int b, int &result)
{
	cout << "Reference in before: " << result << endl;
	result = a + b + 40;
	cout << "Reference in after: " << result << endl;	
}

void pass_by_const_reference(const int &b)
{
	cout << "Address of param: " << &b << endl;
	b = 10;
}

int main() 
{
	int ret = 0;	
	int a = 5;
	int b = 10;
	int *p = &ret;

	ret = use_return(a, b);
	cout << "Return values is: " << ret << endl;

	cout << "-------------" << endl;

	use_pointer(a, b, p);
	cout << "Pointer value is: " << *p << endl;
	
	cout << "-------------" << endl;

	cout << "Reference out before: " << ret << endl;
	use_reference(a, b, ret);
	cout << "Reference out after: " << ret << endl;

	cout << "-------------" << endl;

	cout << "Address of b: " << &b << endl;
	//pass_by_const_reference(b);

	return 0;
}