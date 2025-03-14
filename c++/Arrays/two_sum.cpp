#include <vector>
#include <unordered_map>

using namespace std;

// each iteration im getting the compliement and chekcing if it is in the map
// if it is that means i have found the two numbers's index.
// i return the index of the current iteration and then i find the index of the
// complement in the map and return that as well.
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        // Create map
        unordered_map<int,int> numMap;

        // Iteraate through the vector
        for (int i = 0; i < nums.size(); i++) {
            // compute the compelement
            int complement = target - nums[i];
            // check if the complement is in the map
            if (numMap.count(complement)) {
                return {numMap[complement], i };
            }
            // if complement is not in the map, this means for that
            // number in nums the two numbers dont add up to the target.
            // therefore just add it to the dictionary.
            numMap[nums[i]] = i;
        }
        return {};
}
};
