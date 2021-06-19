#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main(){
    int N;
    cin >> N;
    vector<int> A(N);
    for(int i = 0; i < N; i++){
        cin >> A[i];
    }

    int b[200] = {0};

    for(int i = 0; i < N; i++){
        b[A[i] % 200]++;
    }
    long long ans = 0;
    for(int i = 0; i < 200; i++){
        ans += (long long)b[i] * (long long)(b[i] - 1) / 2;
    }
    cout << ans << endl;
    return 0;
}