#include <iostream>

int generate_celebrity_array(int flag, int n) {
	if (flag) {
		
	} else {
		
	}
}

int main() {
	int flag, n, celebrity_matrix;

	cout << "Will generated array contain celebrity (0/1):" << endl;
	getline(cin, flag);
	cout << "Number of people;" << endl;
	getline(cin, n);

	celebrity_matrix = generate_celebrity_array(flag, n);

	return 0;
}