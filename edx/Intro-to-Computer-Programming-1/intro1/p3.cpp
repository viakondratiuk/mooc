#include<iostream>
using namespace std;

struct LinkedNodes{
  int nodeId;
  LinkedNodes *next;
};

struct myNode{
  int id;
  LinkedNodes *outgoing;
  LinkedNodes *incoming;
};

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



void initNodes(myNode *nodes, int numNodes){
//// ---------------------------------------------------------------------------
//// BEGIN: Write code here to initialize all the nodes DONT_ERASE_02_2
    for (int i = 0; i < numNodes; i++) {
        nodes[i].id = i + 1;
        nodes[i].incoming = NULL;
        nodes[i].outgoing = NULL;
    }
//// END: end of function code DONT_ERASE_02_2
//// ---------------------------------------------------------------------------
}

void addEdge(myNode *nodes, int start, int end){
//// ---------------------------------------------------------------------------
//// BEGIN: Write code here to add an edge from start node to end node DONT_ERASE_03_4
    LinkedNodes *tempNode = new LinkedNodes;
    LinkedNodes *outNode = new LinkedNodes;
    LinkedNodes *inNode = new LinkedNodes;

    tempNode = nodes[start-1].outgoing;
    while (tempNode != NULL) {
        if (tempNode->nodeId == end) {
            return;
        }
        tempNode = tempNode->next;
    }
    delete[] tempNode;

    outNode->nodeId = end;
    outNode->next = nodes[start-1].outgoing;
    nodes[start-1].outgoing = outNode;

    inNode->nodeId = start;
    inNode->next = nodes[end-1].incoming;
    nodes[end-1].incoming = inNode;
//// END: end of function Code DONT_ERASE_03_4
//// ---------------------------------------------------------------------------
}

void getOutgoingNodes(myNode *nodes, int i, int *nodesArray, int &num){
//// ---------------------------------------------------------------------------
//// BEGIN: Write code here to get all the outgoing nodes of node 'i' DONT_ERASE_04_2
    LinkedNodes *node = new LinkedNodes;
    node = nodes[i].outgoing;

    while (node != NULL) {
        nodesArray[num] = node->nodeId;
        num++;
        node = node->next;
    }
//// END: end of function code DONT_ERASE_04_2
//// ---------------------------------------------------------------------------
}

void getIncomingNodes(myNode *nodes, int i, int *nodesArray, int &num){
//// ---------------------------------------------------------------------------
//// BEGIN: Write code here to get all the incoming nodes of node 'i' DONT_ERASE_05_2
    LinkedNodes *node = new LinkedNodes;
    node = nodes[i].incoming;

    while (node != NULL) {
        nodesArray[num] = node->nodeId;
        num++;
        node = node->next;
    }
//// END: end of function code Code ends DONT_ERASE_05_2
//// ---------------------------------------------------------------------------
}

int main(){
  int numNodes;
  cout<<"Give number of nodes:";
  cin >> numNodes;
  cout<<numNodes<<endl;
  myNode *nodes = new myNode[numNodes];
  if(nodes == NULL){
    cout<<"Memory allocation failure."<<endl;
    return -1;
  }
  else{
    initNodes(nodes,numNodes);
  }

  int startEdge, endEdge;
  while (true) {
    // Reading in edges, one at a time
    cout << "Give start of edge (-1 to quit): ";
    cin >> startEdge;
    cout << startEdge << endl;
    if (startEdge == -1) break;
    cout << "Give end of edge (-1 to quit): ";
    cin >> endEdge;
    cout << endEdge << endl;
    if (endEdge == -1) break;
    addEdge(nodes, startEdge, endEdge);
  }
  int *nodesArray = new int[numNodes];
  if(nodesArray == NULL){
    cout<<"Memory allocation failure."<<endl;
    return -1;
  }
  int num=0;
  cout << endl;
  // Printing adjacent nodes of every node
  for (int i = 0; i < numNodes; i++) {
    cout << "Nodes with edges from node " << i+1 << ": ";
    getOutgoingNodes(nodes, i, nodesArray, num);
    if(num!=0){
      for(int j=0;j<num-1;j++){
        cout<<nodesArray[j]<<" ";
      }
      cout << nodesArray[num-1] << endl;
    }
    if(num==0) cout << endl;
    num=0;
  }
  cout << endl;
  num=0;
  for (int i = 0; i < numNodes; i++) {
    cout << "Nodes with edges to node " << i+1 << ": ";
    getIncomingNodes(nodes, i, nodesArray, num);
    if(num!=0){
      for(int j=0;j<num-1;j++){
        cout<<nodesArray[j]<<" ";
      }
      cout << nodesArray[num-1] << endl;
    }
    if(num==0) cout << endl;
    num=0;
  }

  return 0;
}


//// ---------------------------------------------------------------------------
//// USER-DEFINED FUNCTIONS : Define all your functions BELOW this line
//// DO NOT forget to declare them inside BLOCK 1 (see beginning of file)
