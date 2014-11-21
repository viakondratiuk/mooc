#include <iostream>

using namespace std;

void not_inited_pointer() {
	int x, *p;

  	x = 10;
  	*p = x; /* error, p not inited */
}

void wrong_value() {
	int x, *p;

  	x = 10;
  	p = x;

  	cout << p << endl;
}

int main() {

	not_inited_pointer();

	return 0;
}
