#include <iostream>

using namespace std;
int main()
{
    int N;
    cin >> N;
    if(int(1.08*N) == 206){
        cout << "so-so" << endl;
        return 0;
    }
    if(int(1.08 * N) < 206){
        cout << "Yay!" << endl;
        return 0;
    }
    else{
        cout << ":(" << endl;
    }
    return 0;
}