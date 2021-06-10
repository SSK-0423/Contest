#include <iostream>
#include <vector>
using namespace std;
int main(void){
    int n,m;
    cin >> n >> m;
    vector<int> a(m);
    vector<int> b(m);
    int count = 0;
    for(int i = 0; i < m; i++){
        cin >> a.at(i) >> b.at(i);
    }

    count = n;
    for(int i = 0; i < m; i++){
        for(int j = 1; j < m; j++){
            if(b[i] == a[j]){
                cout << b[i] << a[j] << endl;
                count++;
            }
        }
    }
    cout << count << endl;
    return 0;
}