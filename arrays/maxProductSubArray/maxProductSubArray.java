class maxProductSubArray {
  public int maxProductSubArrayFunction(int[] nums) {
    if (nums.length === 0) return 0;
    int max_so_far = nums[0];
    int min_so_far = nums[0];
    int result = max_so_far;
    for (int i = 0; i < nums.length; i++) {
      
    }
  }
}

class Solution {
  public static void main(String[] args) {
    int[] nums = {};
    maxProductSubArray obj = new maxProductSubArray();
    int result = obj.maxProductSubArrayFunction(nums);
    System.out.println(result);
  }
}
