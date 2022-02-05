#include <iostream>
#include <vector>

using namespace std;

int main() {
    long long P;
    cin >> P;
    vector<long long> kouka(10);
    for (int i = 1; i <= 10; i++) {
        long long s = 1;
        for (int j = 1; j <= i; i++) {
            s *= (long long)j;
        }
        kouka[i - 1] = s;
    }
    for (auto i : kouka) {
        cout << i << endl;
    }
    return 0;
}