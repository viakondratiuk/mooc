#include <iostream>

using namespace std;

int calls_count = 0;

int fib_recursion(int n)
{
	if (n <= 2) { 
		return 1;
	} else {
		return fib_recursion(n - 2) + fib_recursion(n - 1);
	}
}

int fib_dynamic(int n)
{
	if (n <= 2) return 1;
	int x = 1, y = 1;
	int fib;

	for (int i = 3; i <= n; i++) {
		fib = x + y;
		x = y;
		y = fib;
	}

	return fib;
}

int fib_matrix(int n)
{
  int a = 1, ta, 
      b = 1, tb,
      c = 1, rc = 0,  tc,
      d = 0, rd = 1; 
 
  while (n) { 
    if (n & 1) {
      // Умножаем вектор R на матрицу A
      tc = rc;
      rc = rc*a + rd*c;
      rd = tc*b + rd*d;
    } 
 
    // Умножаем матрицу A на саму себя
    ta = a; tb = b; tc = c;
    a = a*a  + b*c;
    b = ta*b + b*d;
    c = c*ta + d*c;     
    d = tc*tb+ d*d;
 
    n >>= 1;  // Уменьшаем степень вдвое
 
  }

  return rc;
}

int main()
{
	int n = 4;
	cout << "Recusrsion fib " << n << ": " << fib_recursion(n) << endl;

	int m = 7;
	cout << "Dynamic fib " << m << ": " << fib_dynamic(m) << endl;

	int d = 8;
	cout << "Matrix fib" << d << " : " << fib_matrix(d) << endl;
}