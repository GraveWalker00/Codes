#include <iostream>
#include <deque>
#include <vector>
#include <unordered_set>

using namespace std;

int maxUniqueIntegers(int N, int M, vector<int>& arr) {
    int maxUnique = 0;
    unordered_set<int> uniqueSet;
    deque<int> dq;

    for (int i = 0; i < N; ++i) {
        while (uniqueSet.find(arr[i]) != uniqueSet.end()) {
            uniqueSet.erase(dq.front());
            dq.pop_front();
        }

        uniqueSet.insert(arr[i]);
        dq.push_back(arr[i]);

        if (dq.size() > M) {
            uniqueSet.erase(dq.front());
            dq.pop_front();
        }

        maxUnique = max(maxUnique, static_cast<int>(uniqueSet.size()));
    }

    return maxUnique;
}

int main() {
    int N, M;
    cin >> N >> M;
    vector<int> arr(N);

    for (int i = 0; i < N; ++i) {
        cin >> arr[i];
    }

    int result = maxUniqueIntegers(N, M, arr);
    cout << result << endl;

    return 0;
}
