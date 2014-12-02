#include <iostream>
#include <cmath>

using namespace std;

int main() {
    double x1, y1, r1, x2, y2, r2, d;
    cin >> x1 >> y1 >> r1 >> x2 >> y2 >> r2;
    int res = 0;

    d = sqrt(pow((x2 - x1),2) + pow((y2-y1),2));
    /**
    5,5,2 5,5,1 : 0
    5,5,2 5,5,2 : -1
    0,0,2 1,0,1 : 1
    0,0,5 1,1,1 : 0
    0,0,2 1,1,1 : 2
    0,0,2 2,2,2 : 2
    0,0,2 3,0,1 : 1
    0,0,2 4,0,1 : 0
    **/
    if (d < fmax(r1, r2)) {
        //Inside circle
        if (d == 0 && r1 != r2) {
            res = 0;
        } else if (d == 0 && r1 == r2) {
            res = -1;
        } else if (d == abs(r1 - r2)) {
            res = 1;
        } else if (d > abs(r1 - r2)) {
            res = 2;
        } else {
            res = 0;
        }
    } else {
        //Outside circle
        if (d < r1 + r2) {
            res = 2;
        } else if (d == r1 + r2) {
            res = 1;
        } else if (d > r1 + r2) {
            res = 0;
        }
    }

    cout << res << endl;
    return 0;
}
