#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int find_block(const vector<int>& P, int line) {
    int low = 0, high = P.size() - 1;
    while (low < high) {
        int mid = (low + high) / 2;
        if (P[mid] < line) {
            low = mid + 1;
        } else {
            high = mid;
        }
    }
    return low + 1;
}

int main() {
    int N, M;
    cin >> N >> M;
    vector<int> lines_per_block(N);
    for (int i = 0; i < N; i++) {
        cin >> lines_per_block[i];
    }

    vector<int> P(N);
    P[0] = lines_per_block[0];
    for (int i = 1; i < N; i++) {
        P[i] = P[i - 1] + lines_per_block[i];
    }

    vector<int> mistakes(M);
    for (int i = 0; i < M; i++) {
        cin >> mistakes[i];
    }

    for (int i = 0; i < M; i++) {
        int block_number = find_block(P, mistakes[i]);
        cout << block_number << endl;
    }

    return 0;
}
