struct ListNode {
  int val;
  ListNode *next;
  ListNode() : val(0), next(nullptr) {}
  ListNode(int x) : val(x), next(nullptr) {}
  ListNode(int x, ListNode *next) : val(x), next(next) {}
};

//[1,2,4]
//[1,3,4]

class Solution {
public:
  ListNode *mergeTwoLists(ListNode *list1, ListNode *list2) {}
};
