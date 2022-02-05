#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;
int main(){
    int N;
    cin >> N;
    vector<vector<long long>> vec(N,vector<long long>(3));
    int max = -1;
    for(int i = 0; i < N; i++){
        cin >> vec[i][0] >> vec[i][1] >> vec[i][2];
        if(vec[i][1] > max) max = vec[i][1];
        if(vec[i][2] > max) max = vec[i][2];
    }

    vector<long long> count_vec(max);
    for(int i = 0; i < N; i++){
        long long start_num = 0;
        long long end_num = 0;
        switch (vec[i][0])
        {
        case 1:
            start_num = vec[i][1];
            end_num = vec[i][2];
            break;
        case 2:
            start_num = vec[i][1];
            end_num = vec[i][2]-1;
            break;
        case 3:
            start_num = vec[i][1]+1;
            end_num = vec[i][2];
            break;
        case 4:
            start_num = vec[i][1]+1;
            end_num = vec[i][2]-1;
            break;
        default:
            break;
        }
        for(int j = start_num; j <= end_num; j++){
            count_vec[j]++;
        }
    }
    int ans = 0;
    for(int i = 0; i < N-1; i++){
        if(count_vec[i] != count_vec[i+1]){
            ans += count_vec[i];
        }
    }
    cout << ans << endl;
    return 0;
}