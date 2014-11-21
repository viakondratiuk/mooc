#include "header.h"

void array_reverse()
{
    int n, temp;

    cout << "Enter array size: " << endl;
    cin >> n;
    int a[n];

    for (int i = 0; i < n; i++) {
        cout << "Enter array element: " << endl;
        cin >> a[i];
    }

    for (int i = 0; i < n / 2; i++) {
        temp = a[n-i-1];
        a[n-i-1] = a[i];
        a[i] = temp;
    }

    for (int i = 0; i < n; i++) {
        cout << a[i] << " ";
    }
    cout << endl;
}

void array_linear_search()
{
    int a[10], n, idx = -1;

    for (int i = 0; i < 10; i++) {
        cout << "Enter array element: " << endl;
        cin >> a[i];
    }

    cout << "Enter search number: " << endl;
    cin >> n;

    for (int i = 0; i < 10; i++) {
        if (a[i] == n) {
            idx = i;
        }
    }

    cout << "Search number " << n << " index is " << idx << endl;
}

void array_avarage()
{
    int n;
    double sum = 0;

    cout << "Enter number of students: " << endl;
    cin >> n;

    int m[n];

    for (int i = 0; i < n; i++) {
        cout << "Enter mark: " << endl;
        cin >> m[i];
        sum += m[i];
    }

    cout << "Avarage is: " << (sum/n) << endl;

}

void capitalize()
{
    char s[100];
    int i = 0;

    cout << "Enter a text string: ";
    cin.get(s, 99);

    while (s[i] != 0) {
        if (s[i] >= 97 && s[i] <= 122) {
            s[i] = s[i] - 32;
        }
        i++;
    }

    cout << "Capitalized string is: " << s << endl;
}

void enhance_contrast()
{
    int image[3][3], new_image[3][3], histogram[256], cdf[256], equalizer[256], min = 0;

    // Fill image with colors
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
            cout << "Enter a color [0-255]: " << i << " - " << j << endl;
            cin >> image[i][j];
        }
    }

    // Show image which was read from console
    cout << "Your image is: " << endl;
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
            cout << image[i][j] << "\t";
        }
        cout << endl;
    }

    // Truncate all arrays
    for (int i = 0; i < 256; i++) {
        histogram[i] = 0;
        cdf[i] = 0;
        equalizer[i] = 0;
    }

    // Count number of colors
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
            histogram[image[i][j]]++;
        }
    }

    // Calculate cumulative distribution function for histogram entries
    cdf[0] = histogram[0];
    for (int i = 1; i < 256; i++) {
        cdf[i] = cdf[i-1] + histogram[i];
    }

    // Find the minimum nonzero value in cdf table
    min = 255;
    for (int i = 1; i < 256; i++) {
        if (cdf[i] < min && cdf[i] != 0) {
            min = cdf[i];
        }
    }

    // Calculate entries in the equalizer table
    // http://en.wikipedia.org/wiki/Histogram_equalization
    for (int i = 0; i < 256; i++){
        equalizer[i] = round((float)(cdf[i] - min) / (3 * 3 - min) * (256 - 1));
    }

    // Put equalized values into new_image array
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
            new_image[i][j] = equalizer[image[i][j]];
        }
    }

    // Show new image
    cout << "Contrast image is: " << endl;
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
            cout << new_image[i][j] << "\t";
        }
        cout << endl;
    }
}
