#include <iostream>

using namespace std;

struct array
{
	int a;
	int b;
	char s;
};

struct ideal_woman
{
	int bust;
	int waist;
	int hip;
	array i;
};

void array_of_structures() 
{
	array some[10];

	some[0].a = 5;
	some[0].b = 10;
	some[0].s = 'a';
	
	some[1].a = 5;
	some[1].b = 10;
	some[1].s = 'b';

	cout << some[1].a << endl;
	cout << some[0].s << endl;	
}

void get_params(int member, int *member_address, ideal_woman woman)
{
	cout << "Member value: " << member << endl;
	cout << "Member address: " << member_address << endl;
	cout << "Member waist: " << woman.waist << endl;
}

void by_pointer(ideal_woman *kate)
{
	cout << kate->bust << endl;
	cout << kate->waist << endl;
	cout << kate->hip << endl;
}

int main() 
{
	array_of_structures();

	ideal_woman kate;
	kate.bust = 90;
	kate.waist = 60;
	kate.hip = 90;

	get_params(kate.bust, &kate.waist, kate);

	by_pointer(&kate);

	ideal_woman jane;
	jane.i.a = 1;
	jane.i.b = 2;
	jane.i.s = 'm';

	cout << jane.i.a << endl;
	cout << jane.i.b << endl;
	cout << jane.i.s << endl;

	return 0;
}