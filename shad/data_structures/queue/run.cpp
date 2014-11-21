#include <iostream>

using namespace std;

#define MAX 10

char queue[MAX];
int spos = 0;
int rpos = 0;

void enqueue(char q)
{
  if(spos == MAX) {
    std::cout << "Queue overflow.\n" << endl;
    return;
  }

  queue[spos] = q;
  spos++;
}

char dequeue()
{
  if(rpos == spos) {
    cout << "Queue is empty.\n" << endl;
    
    return '\0';
  }

  rpos++;
  return queue[rpos-1];
}

void show_queue()
{
	for (unsigned int i = 0; i <= MAX; i++) {
		cout << queue[i] << ", ";
	}

	cout << endl;
}

int main()
{
	enqueue('A');
	enqueue('B');
	enqueue('C');
	show_queue();
	cout << dequeue() << endl;
	cout << dequeue() << endl;
	enqueue('D');
	show_queue();
	cout << dequeue() << endl;
	enqueue('E');
	enqueue('F');
	cout << dequeue() << endl;
	show_queue();

	return 0;
}