# include <iostream>

using namespace std;

void array_index_ariphmetics(char *str) {
	for (int i = 0; str[i]; ++i) {
		cout << str[i] << endl;
	}
}

void array_address_ariphmetics(char *str) {
	while (*str) {
		cout << (*str++) << endl;
	}
}

void dispaly_array_pointers(int *x[]) {
	for (int i = 0; i < 2; i++) {
		cout << "index is: " << i << ", value is: " << x[i] << endl;	
	}
}

int main() {
	char str[6] = "Hello";
	array_index_ariphmetics(str);
	cout << "--------------" << endl;
	array_address_ariphmetics(str);
	cout << "--------------" << endl;

	int *x[2];
	int var0 = 10;
	int var1 = 20;
	x[0] = &var0;
	x[1] = &var1;

	dispaly_array_pointers(x);

	return 0;
}