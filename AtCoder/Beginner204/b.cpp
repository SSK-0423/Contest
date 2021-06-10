#include <iostream>
#include <vector>
using namespace std;
int main(void){
    int n;
    cin >> n;
    vector<int> a(n);
    for(int i = 0; i < n; i++){
        cin >> a.at(i);
    }
    int sum = 0;
    for(int i = 0; i < n; i++){
        a[i] -= 10;
        if(a[i] >= 0){
            sum += a[i]; 
        }
    }
    cout << sum << endl;
    return 0;
}