#include <vector>
#include <iostream>

class Solution {
public:
    int removeDuplicates(std::vector<int>& nums) {
        if (nums.empty()) return 0; // Edge case: empty array

        int i = 0; // Slow pointer (keeps track of unique elements)

        for (int j = 1; j < nums.size(); j++) {
            if (nums[j] != nums[i]) { // Found a new unique element
                i++; // Move slow pointer forward
                nums[i] = nums[j]; // Overwrite with the new unique element
            }
        }

        return i + 1; // New size of unique elements
    }
};

int main() {
    std::vector<int> nums = {1, 1, 2, 2, 3, 4, 4, 5};
    Solution sol;
    int newSize = sol.removeDuplicates(nums);

    // Print result
    std::cout << "New size: " << newSize << "\n";
    for (int k = 0; k < newSize; k++) {
        std::cout << nums[k] << " ";
    }
    return 0;
}
