#include <iostream>
#include <vector>

class Solution {
public:
  bool validMountainArray(std::vector<int> &arr) {
    if (arr.size() < 3)
      return false;

    int i = 0;
    int N = arr.size();

    while (i + 1 < N - 1 && arr[i] < arr[i + 1])
      i++;

    if (i == 0 || i == N - 1)
      return false;

    while (i + 1 < N - 1 && arr[i] > arr[i + 1])
      i++;
    return i == N - 1;
  }
};

int main() {
  Solution sol;
  std::vector<int> arr = {3, 5, 4};
  std::cout << sol.validMountainArray(arr) << '\n';
  return 0;
}
