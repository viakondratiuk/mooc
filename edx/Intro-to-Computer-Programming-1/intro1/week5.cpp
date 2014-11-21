#include "header.h"

int alg_selection_sort(int a[], int s)
{
    int temp = 0;

    for (int i = 0; i < s; i++) {
        for (int j = (i + 1); j < s; j++) {
            if (a[j] < a[i]) {
                temp = a[i];
                a[i] = a[j];
                a[j] = temp;
            }
        }
    }

    return *a;
}

void selection_sort()
{
    int a[8] = {105, 2, 311, 4, 50, 6, 71, 8};

    a[8] = alg_selection_sort(a, 8);

    for (int i = 0; i < 8; i++) {
        cout << a[i] << " ";
    }
    cout << endl;
}

int alg_bin_search(int a[], int start, int end, int n)
{
    if (start == end) {
        if (a[start] == n) {
            return 1;
        }
        return -1;
    }

    int half;
    half = start + ((end - start ) / 2);
    if (n > a[half]) {
        alg_bin_search(a, half + 1, end, n);
    } else {
        alg_bin_search(a, start, half, n);
    }
}

void bin_search()
{
    int a[10] = {10, 90, 100, 80, 20, 70, 30, 60, 40, 50};
    a[10] = alg_selection_sort(a, 10);

    int n, res;
    cout << "Enter search number: " << endl;
    cin >> n;

    res = alg_bin_search(a, 0, 10, n);
    if (res == 1) {
        cout << "Element was found!" << endl;
    } else if (res == -1) {
        cout << "Element not found :(" << endl;
    }
}
