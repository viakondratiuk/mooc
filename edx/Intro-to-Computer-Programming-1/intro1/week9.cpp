#include "header.h"

struct V3 {
    double x, y, z;

    double length() {
        return sqrt(x * x + y * y + z * z);
    }

    V3 sum(V3 const &b) {
        V3 v;
        v.x = x + b.x;
        v.y = y + b.y;
        v.z = z + b.z;

        return v;
    }

    V3 scale(double const factor) {
        V3 v;
        v.x = x * factor;
        v.y = y * factor;
        v.z = z * factor;

        return v;
    }
};
