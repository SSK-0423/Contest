#include <iostream>

using namespace std;
int main()
{
    int N;
    cin >> N;

    int num = 1;
    int i = 1;
    int count = 1;
    while(true){
        if(num >= N){
            cout << count << endl;
            break;
        }
        count++;
        num += count;
    }

    return 0;
}