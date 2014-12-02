#include <iostream>
#include <cmath>

using namespace std;

int main() {
    double x1, y1, r1, x2, y2, r2, d;
    cin >> x1 >> y1 >> r1 >> x2 >> y2 >> r2;

    d = sqrt(pow((x2 - x1),2) + pow((y2-y1),2));

    if (d == 0) {
        if (r1 == r2) {
            cout << -1 << endl;
        } else {
            cout << 0 << endl;
        }
    } else if (abs(r1 - r2) > d) {
        cout << 0 << endl;
    } else if (d == r1 + r2) {
        cout << 1 << endl;
    } else if (d < r1 + r2) {
        cout << 2 << endl;
    } else {
        cout << 0 << endl;
    }

    return 0;
}
