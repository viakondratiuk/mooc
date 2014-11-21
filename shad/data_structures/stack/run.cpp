#include <iostream>

using namespace std;

#define MAX 10

int stack[MAX];
int top = 0;

void push(int number) {
    if (top > MAX) {
    	cout << "Stack overflow.\n" << endl;
    	return;
    }

    stack[top] = number;
    top++;
}

int pop() {
	top--;
	if (top < 0) {
		cout << "Stack is empty.\n" << endl;
		return 0;		
	}

    return stack[top];
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