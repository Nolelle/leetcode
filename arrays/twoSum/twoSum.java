class twoSum {
    public int[] twoSumFunction(int[] nums, int target) {
        for (int i = 0; i < nums.length; i++) {
            for (int j = i + 1; j < nums.length; j++) {
                if (nums[i] + nums[j] == target) {
                    return new int[] { i, j };
                }
            }
        }
        return null;
    }
}

class Solution {
    public static void main(String[] args) {
        twoSum obj = new twoSum();
        int[] nums = { 2, 7, 11, 15 };
        int target = 9;
        int[] answer = obj.twoSumFunction(nums, target);
        for (int i = 0; i < answer.length; i++) {
            System.out.println(answer[i]);
        }
    }
}
