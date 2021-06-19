#include <iostream>
#include <vector>
#include <set>
#include <algorithm>
using namespace std;

int main()
{
    long long N;
    cin >> N;
    vector<int> A(N);

    for(int i = 0; i < N; i++){
        cin >> A[i];
    }
    //nC2
    long long num = 0;
    num = N * (N - 1) / 2;
    
    long long cnt = 1;
    sort(A.begin(),A.end());
    A.push_back(-1);
    for(int i = 0; i < N; i++){
        if(A[i] != A[i + 1]){
            num -= (cnt*(cnt - 1)/2);
            cnt = 1;
        }else{
            cnt++;
        }
    }

    cout << num << endl;
    return 0;
}