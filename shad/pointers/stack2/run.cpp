#include <iostream>

using namespace std;

#define MAX 20

int stack[MAX];
int *start;
int *top;

void push(int value) {
	top++;
	*top = value;
	cout << "Top: " << top << " Value: " << *top << endl;	
}

int pop() {
	cout << "Top before: " << top << endl;
	top--;
	cout << "Top after : " << top << endl;
	return *(top + 1);
}

void dispaly_stack() {
	for (int i = 0; i < MAX; i++) {
		if (stack[i] > 0) {
			cout << stack[i] << ", ";
		}
	}
	cout << endl;
}

int main() {
	start = stack;
	top = stack;

	push(1);
	dispaly_stack();
	push(2);
	dispaly_stack();
	push(3);
	dispaly_stack();
	push(4);
	dispaly_stack();
	cout << pop() << endl;
	cout << pop() << endl;
	cout << pop() << endl;
	push(5);
	push(6);
	push(7);
	dispaly_stack();

	return 0;
} 