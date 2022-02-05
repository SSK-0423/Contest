#include <iostream>

using namespace std;
int main(){
    int A;
    int B;
    cin >> A >> B;
    if(6 * A < B || A > B){
        cout << "No" << endl;
    }else{
        cout << "Yes" << endl;
    }
    return 0;
}