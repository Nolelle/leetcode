#include <vector>
using namespace std;

class Solution
{
public:
    int removeElement(vector<int> &nums, int val)
    {
        if (nums.empty())
            return 0;

        int i = 0; // i tracking non val elements

        for (int j = 0; j < nums.size(); j++)
        {
            if (nums[j] != val)
            {
                nums[i] = nums[j];
                i++;
            }
        }

        return i;
    }
};
