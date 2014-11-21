#include <iostream>

using namespace std;

int array[] = {0, 1, 2, 22, 0, 1, 2};
int length = 7;

int main()
{
	int sum2 = 0;

	for (int i = 0; i < length; i++) {
		sum2 ^= array[i];
	}

	cout << "Sum of module 2 is: " << sum2 << endl;

	return 0;
}