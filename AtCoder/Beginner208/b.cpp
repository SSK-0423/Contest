#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main(){
    long long P;
    cin >> P;
    vector<long long> kouka(10);

    for(int i = 1; i <= 10; i++){
        long long s = 1;
        for(int j = 1; j <= i; j++){
            s *= (long long)j;
        }
        kouka[i - 1] = s;
    }

    long long cnt = 0;

    while(true){
        for(int i = 9; i >= 0; i--){
            if(P - kouka[i] >= 0){
                P -= kouka[i];
                cnt++;
                break;
            }
        }
        if(P == 0) break;
    }
    cout << cnt << endl;
    return 0;
}