#include <iostream>

using namespace std;

int fast_exp(int a, int n)
{
	int res = 1;

	while (n) {
		if (n & 1) res *= a;
		a *= a;
		n >>= 1;
	}

	return res;
}

int main()
{
	int a = 3, n = 6;

	cout << a << "^" << n << " = " << fast_exp(a, n) << endl;

	return 0;
}