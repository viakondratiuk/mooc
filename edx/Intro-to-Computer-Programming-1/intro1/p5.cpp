#include<iostream>
using namespace std;

class myNode{
    int id;
    int nodeWeight;
    static int numNodes;
    struct LinkedNodes{
      int nodeId;
      int edgeWeight;
      LinkedNodes *next;
    };
    LinkedNodes *outgoing;
    LinkedNodes *incoming;
  public:
    myNode();
    void initNodes(int nodeWt[]);
    void addEdge(int start, int end, int wt);
    void calculateMetric(int *metric);
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
// from within the blocks.  Make sure that you declare those functions/any class definition inside
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
int myNode::numNodes = 0;
////
//// END: Fill your details as comments above DONT_ERASE_01_0
//// ---------------------------------------------------------------------------

myNode::myNode(){
//// ---------------------------------------------------------------------------
//// BEGIN: Write code here for the default constuctor DONT_ERASE_02_1
    this->id = 0;
    this->nodeWeight = 0;
    this->incoming = NULL;
    this->outgoing = NULL;
    numNodes++;
//// END: end of function code DONT_ERASE_02_1
//// ---------------------------------------------------------------------------
}

void myNode::initNodes(int nodeWt[]){
//// ---------------------------------------------------------------------------
//// BEGIN: Write code here to initialize all the node weights DONT_ERASE_03_2
    myNode *node = this;
    for (int i = 0; i < numNodes; i++) {
        node->id = i + 1;
        node->nodeWeight = nodeWt[i];
        node++;
    }
//// END: end of function Code DONT_ERASE_03_2
//// ---------------------------------------------------------------------------
}

void myNode::addEdge(int start, int end, int wt){
//// ---------------------------------------------------------------------------
//// BEGIN: Write code here to add an edge from node 'start' to node 'end' with edge weight 'wt' DONT_ERASE_04_3
    myNode *startNode = this + (start - 1);
    myNode::LinkedNodes *tempNode;
    //cout << "init start" << endl;

    tempNode = startNode->outgoing;
    //cout << startNode->id << endl;
    //cout << "1" << endl;
    while (tempNode != NULL) {
        //cout << "2" << endl;
        if (tempNode->nodeId == end) {
            return;
        }
        //cout << "3" << endl;
        tempNode = tempNode->next;
        //cout << "4" << endl;
    }

    //cout << "search equal" << endl;

    myNode::LinkedNodes *out = new myNode::LinkedNodes;
    out->nodeId = end;
    out->edgeWeight = wt;
    out->next = startNode->outgoing;
    startNode->outgoing = out;

    //cout << "assign start" << endl;

    myNode *endNode = this + (end - 1);
    myNode::LinkedNodes *in = new myNode::LinkedNodes;

    //cout << "init end" << endl;

    in->nodeId = start;
    in->edgeWeight = wt;
    in->next = endNode->incoming;
    endNode->incoming = in;

    //cout << "assign end" << endl;
//// END: end of function code DONT_ERASE_04_3
//// ---------------------------------------------------------------------------
}

void myNode::calculateMetric(int *metric){
//// ---------------------------------------------------------------------------
//// BEGIN: Write code here to calculate metric for each node DONT_ERASE_05_4
//// sum of all incoming edge weights - sum of all outgoing edge weights
    myNode *node = this;
    myNode::LinkedNodes *linked;
    for (int i = 0; i < numNodes; i++) {
        cout << "i = " << (i + 1) << endl;
        linked = node->incoming;
        while (linked != NULL) {
            cout << "incoming = " << linked->edgeWeight << endl;
            metric[i] += linked->edgeWeight;
            linked = linked->next;
        }
        linked = node->outgoing;
        while (linked != NULL) {
            cout << "outgoing = " << linked->edgeWeight << endl;
            metric[i] -= linked->edgeWeight;
            linked = linked->next;
        }
        node++;
    }
//// END: end of function code DONT_ERASE_05_4
//// ---------------------------------------------------------------------------
}


int main(){
  int numNodes;
  do{
    cout<<"Give number of nodes:";
    cin >> numNodes;
    //maximum 100 nodes allowed
  }while(numNodes<1 || numNodes >100);
  cout<<numNodes<<endl;

  cout <<endl;
  myNode *nodes = new myNode[numNodes];
  int *nodeWeight = new int[numNodes];
  if(nodes == NULL || nodeWeight == NULL){
    cout<<"Memory allocation failure."<<endl;
    return -1;
  }
  else{
    for(int i=0;i<numNodes;i++){
      do{
        cout<<"Enter weight(max=10,min=0) of node "<<i+1<<": ";
        cin >> nodeWeight[i];
       //weight of a node can be between 0 to 10
      }while(nodeWeight[i] <0 || nodeWeight[i] > 10);
      cout << nodeWeight[i] << endl;
    }
    //initialize all the nodes to their node weight
    nodes->initNodes(nodeWeight);
  }

  cout << endl;
  int startEdge=0, endEdge=0, edWeight=0;
  while (true) {
    // Reading in edges, one at a time
    do{
      cout << "Enter start of edge from any node in the range 1 to "<<numNodes<<" (0 to quit): ";
      cin >> startEdge;
    }while(startEdge < 0 || startEdge > numNodes);
    if(startEdge == 0){ break;}
    cout << startEdge << endl;
    do{
      cout << "Enter end of edge from node " << startEdge << " (0 to quit): ";
      cin >> endEdge;
    }while(endEdge<0 || endEdge>numNodes);
    if (endEdge == 0){ break;}
    cout << endEdge << endl;
    do{
      cout << "Enter weight(max=100, min=0) of edge from node "<<startEdge<<" to node "<<endEdge<<" (-1 to quit): ";
      cin >> edWeight;
    //edge weight can be between 0 to 100
    }while(edWeight < -1 || edWeight > 100);
    if (edWeight == -1){ break;}
    cout << edWeight << endl;
    //add edge from node 'startEdge' to node 'endEdge' with weight 'edWeight'
    nodes->addEdge(startEdge, endEdge, edWeight);
  }
  int *metric = new int[numNodes];
  if(metric == NULL){
    cout<<"Memory allocation failure."<<endl;
    return -1;
  }
  cout << endl;
  for(int i = 0 ; i < numNodes ; i++) metric[i] = 0.0;
  //calculate metric for each node: sum of all incoming edge weights - sum of all outgoing edge weights
  nodes->calculateMetric(metric);
  cout << endl;
  for(int i = 0; i < numNodes ; i++){
    cout << "Metric for node "<<i+1<<": "<<metric[i]<<endl;
  }
  return 0;
}

//// ---------------------------------------------------------------------------
//// USER-DEFINED FUNCTIONS : Define all your functions BELOW this line
//// DO NOT forget to declare them inside BLOCK 1 (see beginning of file)
