struct node
{
	int data;
	node *next;
};

node *create_node();

void insert_front(int data);

void insert_back(int data);

void insert_after(int pos, int data);

void delete_front();

void delete_back();

void delete_node(int pos);

void sort_nodes();