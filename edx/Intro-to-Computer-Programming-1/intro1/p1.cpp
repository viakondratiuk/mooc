#include <iostream>
#include<cstdlib>
using namespace std;

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



// Description of the program

//// ---------------------------------------------------------------------------
//// BEGIN: Write a function getArray1D DONT_ERASE_02_4
//// The function should return a 1D array to the function getArray2D from where it is called
int * getArray1D(int n, int *A) {
    A = new int[n];
    return A;
}
//// END: End of function code DONT_ERASE_02_4
//// ---------------------------------------------------------------------------

//// ---------------------------------------------------------------------------
//// BEGIN: Write function getArray2D DONT_ERASE_03_6
//// The function should return a 2D array to the main function
//// Call the function getArray1D in this function
int ** getArray2D(int m, int n, int **A) {
    A = new int*[n];
    for (int i = 0; i < m; i++) {
        //A[i] = new int [m];
        A[i] = getArray1D(n, A[i]);
    }
    return A;
}
//// END: End of function code DONT_ERASE_03_6
//// ---------------------------------------------------------------------------



int main() {
  int **Array;
  int m, n;
  cin>>m>>n;
  Array = getArray2D(m,n,Array);
  for(int i=0;i<m;i++)
    for(int j=0;j<n;j++){
      cin >> Array[i][j];
    }
    cout<<endl;
  for(int i=0;i<m;i++){
    for(int j=0;j<n;j++){
      cout<<Array[i][j]<<" ";
    }
    cout<<endl;
  }
  return 0;
}



//// ---------------------------------------------------------------------------
//// USER-DEFINED FUNCTIONS : Define all your functions BELOW this line
//// DO NOT forget to declare them inside BLOCK 1 (see beginning of file)
