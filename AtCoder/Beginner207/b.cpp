#include <iostream>

using namespace std;
int main()
{
    long long A, B, C, D;
    cin >> A >> B >> C >> D;
    long long cnt = 0;
    long long blue_cnt = A;
    long long red_cnt = 0;
    if (B > C * D)
    {
        cout << -1 << endl;
        return 0;
    }
    if(B == C * D && A > 0){
        cout << -1 << endl;
        return 0;
    }
    while (true)
    {
        blue_cnt += B;
        red_cnt += C;
        cnt++;
        if (blue_cnt <= red_cnt * D)
        {
            cout << cnt << endl;
            break;
        }
    }
    return 0;
}