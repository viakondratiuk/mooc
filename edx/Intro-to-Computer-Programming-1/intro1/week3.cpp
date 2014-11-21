#include "header.h"

void draw_rectangle()
{
    int h, w;
    cout << "Rectangle height is: " << endl;
    cin >> h;
    cout << "Rectangle width is: " << endl;
    cin >> w;

    for (int i = 1; i <= h; i++) {
        for (int j = 1; j <= w; j++) {
            if (i == 1 || i == h || j == 1 || j == w) {
                cout << "*";
            } else {
                cout << " ";
            }
        }
        cout << endl;
    }
}

void second_highest()
{
    int n, max1, max2;
    n = max1 = max2 = 0;

    cout << "Enter a number: " << endl;
    cin >> n;
    max1 = n;

    while (n > 0) {
        cout << "Enter a number: " << endl;
        cin >> n;

        if (n > max1) {
            max2 = max1;
            max1 = n;
        } else if (n > max2) {
            max2 = n;
        }
    }

    cout << "First highest is: " << max1 << endl;
    cout << "Second highest is: " << max2 << endl;
}

void dec2bin()
{
    int n, rem, i = 1, bin = 0;

    cout << "Enter a number: " << endl;
    cin >> n;

    while (n > 0) {
        rem = n % 2;
        bin += rem * i;
        i *= 10;
        n = n / 2;
    }

    cout << "Binary number is: " << bin << endl;
}

void is_armstrong()
{
    int temp, rem, sum, div = 10;

    for (int n = 0; n < 1000; n++) {
        temp = n;
        sum = 0;
        while (temp > 0) {
            rem = temp % div;
            sum += rem * rem * rem;
            temp /= div;
        }

        if (n == sum) {
            cout << "Number " << n << " is Armstrong number" << endl;
        }
    }
}

void is_palindrome()
{
    int n, temp, rem, sum = 0;

    cout << "Enter your number: " << endl;
    cin >> n;
    temp = n;

    while (n > 0) {
        rem = n % 10;
        sum = sum * 10 + rem;
        n /= 10;
    }

    if (temp == sum) {
        cout << "The number " << temp << " is a palindrome" << endl;
    } else {
        cout << "The number " << temp << " isn't a palindrome" << endl;
    }
}

void power(double n, int p)
{
    int temp;
    double res = 1;
    temp = p;

    while (p > 0) {
        res *= n;
        p--;
    }

    cout << n << "^" << temp << " = " << res;
}

void nCr()
{
    int n, r, num1 = 1, den1 = 1, den2 = 1;

    cout << "Enter n from nCr: " << endl;
    cin >> n;
    cout << "Enter r from nCr: " << endl;
    cin >> r;

    if ((r > n) || (r < 0)) {
        cout << "Wrong input!" << endl;
    }

    if (r == 0) {
        cout << "nCr = 1" << endl;
    }

    for (int i = 1; i <= n; i++) {
        num1 *= i;
    }

    for (int i = 1; i <= (n-r); i++) {
        den1 *= i;
    }

    for (int i = 1; i <= r; i++) {
        den2 *= i;
    }

    cout << "nCr = " << (num1 / (den1 * den2)) << endl;
}

void gcd()
{
    unsigned int u, v, t;
    cin >> u >> v;

    while (v) {
        t = u;
        u = v;
        v = t % u;
    }

    cout << u;
}

void square_root()
{
    float n, res;

    cout << "Enter a number: " << endl;
    cin >> n;
    res = n / 2;

    while (abs(n - res*res) > 0.1) {
        res = (n / res + res) / 2;
    }

    cout << "Approximate sqrt of " << n << " is " << res;
}
