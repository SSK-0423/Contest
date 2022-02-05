#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main(){
    long long N,K;
    cin >> N >> K;
    vector<long long> a_(N);
    for(int i = 0; i < N; i++){
        cin >> a_[i];
    }
    vector<vector<long long>> okashi_(N,vector<long long>(2));
    for(int i = 0; i < N; i++){
        okashi_[i][0] = a_[i];
    }

    //昇順にソート
    sort(a_.begin(),a_.end());

    // 全員に1個ずつ配る
    long long Num = (long long)(K / N);
    for(int j = 0; j < N; j++){
        okashi_[j][1] = Num;
    }
    
    K  = K - N * Num;
    for(int i = 0; i < K; i++){
        for(int j = 0; j < N; j++){
            if(okashi_[j][0] == a_[i]){
                okashi_[j][1]++;
            }
        }
    }
    //出力
    for(int i = 0; i < N; i++){
        cout << okashi_[i][1] << endl;
    }    
    return 0;
}