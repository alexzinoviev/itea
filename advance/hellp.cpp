#include <iostream>

using namespace std;

extern "C"
void hello() {
    cout <<"Hello, world" << endl;
}

extern "C"
int