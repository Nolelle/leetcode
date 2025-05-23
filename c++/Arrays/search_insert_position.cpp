#include <vector>;
using namespace std;

class Solution
{
public:
    int searchInsert(vector<int> &nums, int target)
    {
        // Implement binary search
        int left = 0;
        int right = nums.size();

        while (left < right)
        {
            int mid = left + (right - left) / 2;
            if (nums[mid] == target)
            {
                return mid;
            }
            else if (nums[mid] < target)
            {
                left = mid + 1;
            }
            else
            {
                right = mid;
            }
        }
        return left; // return left if target not found
    }
};