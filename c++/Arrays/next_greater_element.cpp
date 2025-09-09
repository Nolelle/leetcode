#include <vector>
#include <stack>
#include <unordered_map>
#include <iostream>

using namespace std;

class Solution
{
public:
    vector<int> nextGreaterElement(vector<int> &nums1, vector<int> &nums2)
    {
        vector<int> answer;
        stack<int> s;
        unordered_map<int, int> dict;

        for (int num2 : nums2)
        {
            while (!s.empty() && num2 > s.top())
            {
                // if it is then we found a pair add the top of stack to the map
                // as a key and set the current eleemnt as the value
                dict[s.top()] = num2;
                s.pop();
            }
            s.push(num2);
        }
        while (!s.empty())
        {
            dict[s.top()] = -1;
            s.pop();
        }

        for (int num1 : nums1)
        {
            answer.push_back(dict[num1]);
        }

        return answer;
    }
};
