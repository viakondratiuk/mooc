#include <iostream>
#include <stdlib.h>

using namespace std;

struct node {
	int data;
	node *next;
};

int main() 
{
	node *curr, *head;
	head = NULL;

	for (int i = 1; i <= 10; i++) {
		curr = (node*)malloc(sizeof(node));
		curr->data = i;
		curr->next = head;
		head = curr;
	}

	curr = head;

	while (curr) {
		cout << curr->data << endl;
		curr = curr->next;
	}

	return 0;
}