#include "header.h"

struct driver {
    int id;
    string name;
};

struct linkedTaxi {
    int id;
    driver *drv;
    linkedTaxi *next;
};

struct queue {
    linkedTaxi *front, *end;
    int numTaxis;
};

int dispatchTaxis()
{
    queue q;
    q.front = NULL;
    q.end = NULL;
    q.numTaxis = 0;

    while (true) {
        cout << "'j' to join the queue, 'd' to dispatch, 'x' to exit." << endl;
        char command;
        cin >> command;
        switch (command) {
            case 'j':
                driver *newDriver;
                newDriver = new driver;
                if (newDriver == NULL) {
                    cout << "Memory allocation fail" << endl;
                    return -1;
                }
                cout << "Give driver name:";
                cin >> newDriver->name;
                cout << "Give driver id:";
                cin >> newDriver->id;

                linkedTaxi *newTaxi;
                newTaxi = new linkedTaxi;
                if (newTaxi == NULL) {
                    cout << "Memory allocation fail" << endl;
                    return -1;
                }
                newTaxi->drv = newDriver;
                newTaxi->next = NULL;
                cout << "Give taxi id:";
                cin >> newTaxi->id;
                if (q.end = NULL) {
                    q.front = newTaxi;
                    q.end = newTaxi;
                    q.numTaxis = 1;
                } else {
                    (q.end)->next = newTaxi;
                    q.end = newTaxi;
                    q.numTaxis++;
                }
                break;
            case 'd':
                if (q.front == NULL) {
                    cout << "Sorry! No taxis in queue at present!" << endl;
                } else {
                    linkedTaxi *dispatchTaxi;
                    dispatchTaxi = q.front;
                    if (q.front == q.end) { // Only one taxi in queue
                        q.front = NULL;
                        q.end = NULL;
                        q.numTaxis = 0;
                    } else {
                        q.front = (q.front)->next;
                        q.numTaxis--;
                    }
                    if (dispatchTaxi != NULL) {
                        cout << "Dispatching taxi with id" << dispatchTaxi->id << endl;
                        if (dispatchTaxi->drv != NULL) {
                            delete dispatchTaxi->drv;
                        }
                        delete dispatchTaxi;
                    }
                }
                break;
            case 'x':
                cout << "Thank you" << endl;
                return 0;
            default:
                cout << "Invalid command" << endl;
        }
    }
}
