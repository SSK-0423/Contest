#include <iostream>
#include <vector>

using namespace std;

int main()
{
    int N;
    cin >> N;
    vector<int> A(N);

    for(int i = 0; i < N; i++){
        cin >> A[i];
    }
    int count = 0; 
    for(int i = 0; i < N; i++){
        for(int j = i+1; j < N; j++){
            if(A[i] != A[j]){
                count++;
            }
        }
    }
    cout << count;
    return 0;
}