#include <iostream>
#include <stdlib.h>
#include "run.h"

using namespace std;

node *head = NULL;

node *create_node()
{
	node *result = new node;
	if (!result) {
		cout << "Out of memory" << endl;
		exit(0);
	}

	return result;
}

void insert_front(int data)
{
	node *insert = create_node();
	insert->data = data;
	insert->next = head;
	head = insert;
}

void insert_back(int data)
{
	if (head == NULL) {
		insert_front(data);
	} else {
		node *curr = head;
		
		while (curr->next != NULL) {
			curr = curr->next;
		}

		node *insert = create_node();
		insert->data = data;
		insert->next = NULL;
		curr->next = insert;
	}	
}

void insert_after(int pos, int data)
{
	node *curr = head;

	for (int i = 1; i < pos; i++) {
		curr = curr->next;

		if (curr == NULL) {
			cout << "Can't insert after node " << pos << ". It doestn't exist." << endl;
			return;
		}
	}

	node *insert = create_node();
	insert->data = data;
	insert->next = curr->next;
	curr->next = insert;	
}

void delete_front()
{
	node *del = create_node();
	del = head;
	head = del->next;
	delete del;
}

void delete_back()
{
	node *del = head;
	node *prev = create_node();
 
	while (del->next != NULL) {
      prev = del;
      del = del->next;
	}

	prev->next = NULL;
	delete del;
}

void delete_node(int pos)
{
	if (pos == 1) {
		delete_front();
	} else {
		node *del = head;
	 
		node *prev = create_node();
		prev = del;
		
		for (int i = 1; i < pos; i++) {
	    	prev = del;
	    	del = del->next;
		}

		prev->next = del->next;
		delete del;
	}	
}

void sort_nodes()
{
	node *curr1 = create_node();
	node *curr2 = create_node();
	 
	int temp = 0;
	 
	for (curr1 = head; curr1 != NULL; curr1 = curr1->next) {
	      for (curr2 = curr1->next; curr2 != NULL; curr2 = curr2->next) {
	            if (curr1->data > curr2->data) {
	                temp = curr1->data;
	                curr1->data = curr2->data;
	                curr2->data = temp;
	            }
	      }
	}	
}

void traverse()
{
	node *curr = head;
	
	while (curr != NULL) {
		cout << curr->data << endl;
		curr = curr->next;
	}
}

int main()
{
	cout << "Insert Front:" << endl;
	insert_front(10);
	insert_front(20);
	insert_front(30);
	insert_front(40);
	traverse();
	cout << "-----------" << endl;
	
	cout << "Insert Back:" << endl;
	insert_back(50);
	insert_back(60);
	insert_back(70);
	traverse();
	cout << "-----------" << endl;
	
	cout << "Insert Position:" << endl;	
	insert_after(2, 80);
	insert_after(2, 90);
	insert_after(7, 100);
	insert_after(6, 110);
	traverse();
	cout << "-----------" << endl;

	cout << "Delete Front:" << endl;	
	delete_front();
	delete_front();
	traverse();
    cout << "-----------" << endl;
	
	cout << "Delete Back:" << endl;	
	delete_back();
	delete_back();
	traverse();
	cout << "-----------" << endl;

	cout << "Delete Node:" << endl;	
	delete_node(1);
	delete_node(1);
	traverse();
	cout << "-----------" << endl;
	
	cout << "Sort Nodes:" << endl;	
	sort_nodes();	
	traverse();
	cout << "-----------" << endl;	

	return 0;
}