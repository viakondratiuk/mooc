#include <iostream>
using namespace std;

int cubes_sum(int n) {
    int sum = 0;
    int weight[8] = {12, 8, 8, 5, 8, 5, 5, 3};

    for (int i = 0; i < n; i++) {
        if (i < 4) {
            sum += weight[i];
        } else {
            sum += weight[(4 + i % 4)];
        }
    }

    return sum;
}

int main() {
    int n;
    for (int i = 1; i < 28; i++) {
        cout << "Cubes=" << (i) << " Matches=" << cubes_sum(i) << endl;
    }


    return 0;
}
