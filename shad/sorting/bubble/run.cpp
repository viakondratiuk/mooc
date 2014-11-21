#include <iostream>

using namespace std;

void show(int array[], int length)
{
	for (int i = 0; i < length; i++) {
		cout << array[i] << ", ";
	}
	cout << endl;
}

void bubble(int *array, int length)
{
	int i,j;
    for(i = 0; i < length; i++) {
        for(j = 0;j < i; j++) {
            if(array[i] < array[j]) {
                int temp = array[i]; //swap 
                array[i] = array[j];
                array[j] = temp;
            }
        }
        show(array, length);
    }
}

int main()
{
	int array[7] = {6, 5, 4, 3, 2, 1, 0};
	int length = 7;
	
	cout << "Before: " << endl; 
	show(array, length);
	bubble(array, length);
	cout << "After: " << endl;
	show(array, length);

	return 0;
}