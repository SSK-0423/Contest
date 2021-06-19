#include <iostream>
#include <vector>
#include <set>
#include <algorithm>
using namespace std;

int main()
{
    int N;
    cin >> N;
    vector<int> A(N);

    for(int i = 0; i < N; i++){
        cin >> A[i];
    }
    //nC2
    long long Count = 0;
    Count = N * (N - 1) / 2;

    set<int> s;
    for(auto i : A){
        s.insert(i);
    }
    
    vector<int> c(s.size());
    int j = 0;
    for(auto i : s){
        c[j] = count(A.begin(),A.end(),i);
        j++;
    }

    int sub = 0;
    for(long unsigned int i = 0; i < s.size(); i++){
        sub += c[i] * (c[i] - 1) / 2; 
    }
    cout << Count - sub << endl;
    return 0;
}