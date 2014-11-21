#include <iostream>

using namespace std;

int array[] = {11, 12, 13, 14, 15, 16, 17, 18, 19, 110, 111};	
int length = 11;
// Start indexes of request
int i = 2, j = 6; 
// Number of requests
int m = 3;

int find_sum_between_indexes(int *array, int i, int j)
{
	int sum;
	for (int k = i; k <= j; k++) {
		sum += array[k];
	}

	return sum;
}

int main()
{
	int sum = find_sum_between_indexes(array, ++i, ++j);
	cout << "Sum[" << i << ".." << j << "] = " << sum << endl;

	for (int s = 2; s <= m; s++) {
		sum = sum - array[++i-1] + array[++j]	;
		cout << "Sum[" << i << ".." << j << "] = " << sum << endl;
	}

	return 0;
}