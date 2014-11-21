#include <iostream>

using namespace std;

// Assume that a always ge b
int nod(int a, int b)
{
	int temp;

	while(b) {
		temp = a % b;
		cout << temp << endl;
		a = b;
		b = temp;
	}

	return a;
}


int main()
{	
	cout << "nod(158, 26): " << nod(158, 26) << endl;
	cout << "nod(1071, 462): " << nod(1071, 462) << endl;

	return 0;
}