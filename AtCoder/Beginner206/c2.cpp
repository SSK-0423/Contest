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
    int num = 0;
    num = N * (N - 1) / 2;

    set<int> s;
    for(auto i : A){
        s.insert(i);

    }
    vector<int> Count(s.size());
    int j = 0;
    for(auto i : s){
        Count[j] = std::count(A.begin(),A.end(),i);
        j++;
    }
    int sum = 0;
    for(auto i : Count){
        if(i >= 2) sum += i;
    }

    cout << num - sum << endl;
    return 0;
}