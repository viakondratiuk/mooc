#include <iostream>

using namespace std;

#define MAX 20

int *start; // start address of stack
int *top; // top address of stack
int stack[MAX]; //array where stack is stored 

void push(int i) {
	top++;
	if (top == (start + MAX)) {
		cout << "Stack Overflow\n" << endl;
	}
	*top = i;
}

int pop() {
	if (top == start) {
		cout << "Stack is Empty\n" << endl;
		return 0;	
	}

	top--;
	return *(top + 1); //value at adress (top + 1), not value at address (top) = 20 + 1 = 21;
}

void show_stack() {
	for (unsigned int i = 0; i < MAX; i++) {
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
	push(2);
	push(3);
	push(4);
	push(5);
	show_stack();
	cout << pop() << endl;
	cout << pop() << endl;
	push(6);
	push(7);
	push(8);
	show_stack();
	cout << pop() << endl;
	push(9);
	show_stack();	

	return 0;
}