package deletion;

// Solution 1: Two Pointers
class removeElement {
  public int remove(int[] nums, int val) {
    int j = 0;
    for (int i = 0; i < nums.length; i++) {
      if (nums[i] != val) {
        nums[i] = nums[j];
        j++;
      }
    }
    return j;
  }
}
// Time Complexity: O(n)
// Space Complexity: O(1)
