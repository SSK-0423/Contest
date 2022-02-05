#include <iostream>

using namespace std;
int main(){
    int A,B,C;
    cin >> A >> B >> C;
    int ans = B + C;
    int min = A;
    if(B < min){
        min = B;
        ans =  A + C;
    }
    if(C < min){
        ans =  A + B;
    }
    cout << ans << endl;
    return 0;
}