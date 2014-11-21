#include "header.h"

void show_var_address()
{
    int a;
    int * ptrA;

    float b;
    float * ptrB;

    char c;
    char * ptrC;

    ptrA = &a;
    cout << "Address of var a is: " << ptrA << endl;

    ptrB = &b;
    cout << "Address of var b is: " << ptrB << endl;

    ptrC = &c;
    cout << "Address of var c is: " << ptrC << endl;
    cout << "Address of var c is: " << (void *)ptrC << endl;
}

void show_var_value_by_pointer()
{
    int a;
    int * ptrA;

    a = 10;
    ptrA = &a;

    cout << ptrA << " values is: " << *ptrA << endl;
}

void deref_of_deref()
{
    char c;
    char * ptrC;
    char ** ptrPtrC;

    ptrC = &c;
    ptrPtrC = &ptrC;
    cin >> c;

    cout << **ptrPtrC << endl;
}

void use_2_pointers()
{
    int m, n;
    int * ptrInt;
    int ** ptrPtrInt;

    ptrPtrInt = &ptrInt;
    cin >> m >> n;
    ptrInt = &m;
    cout << *(*ptrPtrInt) << endl;
    ptrInt = &n;
    cout << *(*ptrPtrInt) << endl;

    int b = 10, c = 15;
    *ptrInt = b + c;
    cout << *ptrInt << endl;
    cout << m << "  " << n << endl;

    int myVar;
    int * myPtr = &myVar;

}

void parent_func()
{
    int x = 5, y = 10;
    cout << "x = " << x << " y = " << y << endl;
    swap_by_ptr(&x, &y);
    cout << "x = " << x << " y = " << y << endl;
    swap_by_ref(x, y);
    cout << "x = " << x << " y = " << y << endl;
    int * b = func_ret_pointer(&y);
    cout <<  b << "--" << (*b) << endl;
}

void swap_by_ptr(int * x, int * y)
{
    int temp;

    temp = *x;
    *x = *y;
    *y = temp;
    return;
}

void swap_by_ref(int &x, int &y)
{
    int temp;

    temp = x;
    x = y;
    y = temp;
    return;
}

int *func_ret_pointer(int * ptrA)
{
    int b;
    b = (*ptrA) * (*ptrA);
    *ptrA = b;

    return ptrA;
}

void qweek6_q1()
{
    char c[]  = "CS101PROGRAMMINGCS101.1x2014";
    char * p = c;
    cout << p + p[1] - p[0];
}

void qweek6_q3()
{
    int a;
    int * b;
    int ** c = &b;
    b = new int;
    *b = 10;
    a = **c;
    *b += 5;

    cout << a << *b;
}

void qweek6_q4()
{
    int A = 4, B = 6;
    int * Aptr = &A , * Bptr = &B;
    cout << &Aptr << "  " << &Bptr << endl;
    qweek6_q4_swap(Aptr, Bptr);
    cout << &Aptr << "  " << &Bptr << endl;
}

void qweek6_q4_swap(int *a, int *b)
{
    int * temp;
    temp = a;
    a = b;
    b = temp;
}

void qweek6_q6()
{
    int * ptr1, * ptr2, ** ptr3;
    ptr3 = &ptr1;
    ptr1 = new int;
    ptr2 = *ptr3;
    cin >> *(*ptr3);
    if (ptr2 == ptr1) {
        cout << "Ahem!" << endl;
    }
    if ((*ptr2) == (*ptr1)) {
        cout << "Aha!" << endl;
    }
    return;
}

void dynamic_allocation()
{
    int n;
    int * a;

    cin >> n;
    a = new int[n];

    if (a != NULL) {
        a[0] = 1;
        a[1] = 2;
        cout << a << "  " << &a << endl;
        delete[] a;
    }
}
