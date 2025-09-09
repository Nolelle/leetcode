#include <vector>
#include <set>
#include <map>
#include <cctype>
#include <iostream>
#include <string>

using namespace std;

class Solution
{
public:
    vector<string> findWords(vector<string> &words)
    {
        // Create an empty list (in C++, a std::vector<std::string>) to store the final answer.
        vector<string> answer;
        set<string> key_rows = {"qwertyuiop", "asdfghjkl", "zxcvbnm"};
        map<char, int> char_to_row;
        int row_index = 0;

        for (const string &row : key_rows)
        {
            for (char c : row)
            {
                	
            }
        }

        // Loop through each word from the input array.
        for (string word : words)
        {
            // Find the target row: Determine which row the first character belongs to.
        }
        return answer;
    }
};

int main()
{
    Solution sol;
    vector<string> test1 = {"Hello", "Alaska", "Dad", "Peace"};
    vector<string> result1 = sol.findWords(test1);
    cout << "Test 1: ";
    for (string s : result1)
        cout << s << " ";
    cout << endl;

    vector<string> test2 = {"omk"};
    vector<string> result2 = sol.findWords(test2);
    cout << "Test 2: ";
    for (string s : result2)
        cout << s << " ";
    cout << endl;

    vector<string> test3 = {"adsdf", "sfd"};
    vector<string> result3 = sol.findWords(test3);
    cout << "Test 3: ";
    for (string s : result3)
        cout << s << " ";
    cout << endl;

    return 0;
}
