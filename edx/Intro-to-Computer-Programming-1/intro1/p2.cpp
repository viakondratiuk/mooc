#include<iostream>
using namespace std;

struct rational {
   int numerator;
   int denominator;
} ;

// Please write ALL code, except functions that you may define yourself,  within
// the "BEGIN-END" blocks given below.  A "BEGIN-END" block is identified by the
// following signature :
//
// "//// BEGIN: Some string DONT_ERASE_xx[_yy]"
// "  Your code goes HERE"
// "//// END: Some other string DONT_ERASE_xx_[_yy]"
//
// where "xx" is a unique integer identifier for the block and "yy" is the
// number of points allocated for the block.
//
// The FIRST block (BLOCK 1) carries no points, and is a placeholder for declaring
// functions defined by you (see end of file).
//
// Feel free to write your own functions ("USER-DEFINED FUNCTIONS") at the
// designated location at the bottom of this file.  You may call these functions
// from within the blocks.  Make sure that you declare those functions inside
// BLOCK 1. Also make sure that the addition of these functions don't cause
// compilation errors.
//
// WARNING :
// (1) DO NOT tamper with the block delimiters under ANY circumstance.  This
//     will simply cause the autograder to fail on ALL test cases.
//
// (2) Any changes to code outside the blocks (except "USER-DEFINED FUNCTIONS"
//     at the bottom) MAY cause the autograder to NOT evaluate your code
//     correctly, leading to a PARTIAL or FULL loss of points for the entire
//     question.
//
// (3) Your FINAL submission should have ZERO 'cout' statements added by you.
//     Make sure that before submitting, you REMOVE all 'cout' statement(s) added
//     by you during debugging


//// ---------------------------------------------------------------------------
//// BEGIN: Fill your details as comments below DONT_ERASE_01_0
////
//// ADD declarations for USER-DEFINED functions (see the end of this file) here :
//// DECL_1 (uncomment this line)
//// DECL_2 (uncomment this line)
//// DECL_3 (uncomment this line)
//// etc.
////
//// END: Fill your details as comments above DONT_ERASE_01_0
//// ---------------------------------------------------------------------------




void reduce(struct rational *inputrational, struct rational *outputrational) {
//// ---------------------------------------------------------------------------
//// BEGIN: Write function code DONT_ERASE_02_6
//// This function reduce is called by another function 'equal'.
//// It should reduce the rational number to its lowest form
    int a = inputrational->numerator;
    int b = inputrational->denominator;

    while (b) {
        int t = a;
        a = b;
        b = t % a;
    }

    outputrational->numerator = inputrational->numerator / a;
    outputrational->denominator = inputrational->denominator / a;
//// END: Function Code ends DONT_ERASE_02_6
//// ---------------------------------------------------------------------------
}


bool equal (struct rational *rational_number1, struct rational *rational_number2) {
//// ---------------------------------------------------------------------------
//// BEGIN: Write function code DONT_ERASE_03_4
//// This function 'equal' calls another function 'reduce' for both the numbers
//// The function should return TRUE to the main function if,
//// numerators of both the numbers are same and denominators of both the numbers are same,
//// else it should return false
    struct rational red1, red2;
    reduce(rational_number1, &red1);
    reduce(rational_number2, &red2);

    return red1.numerator == red2.numerator && red1.denominator == red2.denominator;

//// END: Function code ends DONT_ERASE_03_4
//// ---------------------------------------------------------------------------
}



int main() {
   int result;
   struct rational num1, num2;
   cout << "Enter Details of Number 1 " << endl;
   cout << "Enter Numerator :" << endl;
   cin >> num1.numerator;
   cout << "Enter Denominator :" << endl;
   cin >> num1.denominator;

   cout << "Enter Details of Number 2 " << endl;
   cout << "Enter Numerator :" << endl;
   cin >> num2.numerator;
   cout << "Enter Denominator :" << endl;
   cin >> num2.denominator;

   result = equal(&num1, &num2);
   if(result == true)
      cout << "Both rational numbers are equal" << endl;
   else
      cout << "Both rational numbers are not equal" << endl;
   return 0;
}


//// ---------------------------------------------------------------------------
//// USER-DEFINED FUNCTIONS : Define all your functions BELOW this line
//// DO NOT forget to declare them inside BLOCK 1 (see beginning of file)
