#include <vector>

using namespace std;

class Solution {
public:
  vector<int> twoSum(vector<int> &nums, int target) {
    std::vector<int> result;
    for (int i = 0; i < nums.size(); i++) {
      for (int j = 0; j < nums.size() - 1; j++) {
        if ((target - nums[i]) == nums[j]) {
          result.push_back(i);
        }
      }
    }
    return result;
  };
};
