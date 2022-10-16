import java.util.Arrays;
import java.util.HashSet;
import java.util.Set;

// Brute Force
// Time Complexity: O(n^2)
// Space Complexity: O(1)
// class containsDuplicate {
// public boolean containsDuplicateFunction(int[] nums) {
// for (int i = 0; i < nums.length; i++) {
// for (int j = i + 1; j < nums.length; j++) {
// if (nums[i] == nums[j]) {
// return true;
// }
// }
// }
// return false;
// }
// }

// Sorting Solution
// Time Complexity: O(nlogn)
// Space Complexity: O(1)
// class containsDuplicate {
//   public boolean containsDuplicateFunction(int[] nums) {
//     Arrays.sort(nums);
//     for (int i = 0; i < nums.length - 1; i++) {
//       if (nums[i] == nums[i + 1]) {
//         return true;
//       }
//     }
//     return false;
//   }
// }

// Hash Table Solution
// Time Complexity: O(n)
// Space Complexity: O(n)
class containsDuplicate {
  public boolean containsDuplicateFunction(int[] nums) {
    Set<Integer> set = new HashSet<>(nums.length);
    for (int x : nums) {
      if (set.contains(x))
        return true;
      set.add(x);
    }
    return false;
  }
}

class Solution {
  public static void main(String[] args) {
    int[] nums = { 1, 2, 3, 4 };
    containsDuplicate obj = new containsDuplicate();
    boolean result = obj.containsDuplicateFunction(nums);
    System.out.println(result);
  }
}