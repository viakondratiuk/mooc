#include <iostream>
#include <stdlib.h>

using namespace std;

int* create_object()
{
   int* p = new int(309);
   cout << p << endl;
   return p;
}

int main()
{
   int* p1 = NULL;

   p1 = create_object();
   cout << p1 << endl;

   if (p1)
   {
      cout << *p1 << endl;
      *p1 = 517;
   }

   delete p1;

   return 0;
}