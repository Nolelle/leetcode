import java.util.Arrays;

// Space Complexity = O(n)
// class productExceptSelf {
// public int[] productExceptSelfFunction(int[] nums) {
// int[] answer = new int[nums.length];
// int[] left = new int[nums.length];
// int[] right = new int[nums.length];
// left[0] = 1;
// right[nums.length - 1] = 1;
// for (int i = 1; i < nums.length; i++) {
// left[i] = left[i - 1] * nums[i - 1];
// }
//
// for (int j = nums.length - 2; j >= 0; j--) {
// right[j] = right[j + 1] * nums[j + 1];
// }
//
// for (int k = 0; k < left.length; k++) {
// answer[k] = left[k] * right[k];
// }
//
// return answer;
// }
// }

// Space Compleixity: O(1)
// Time Complexity: O(n)
//
class productExceptSelf {
    public int[] productExceptSelfFunction(int[] nums) {
        int length = nums.length;
        int[] answer = new int[length];

        answer[0] = 1;
        for (int i = 1; i < length; i++) {
            answer[i] = answer[i - 1] * nums[i - 1];
        }
        int right = 1;
        for (int j = nums.length - 1; j >= 0; j--) {
            answer[j] = right * answer[j];
            right *= nums[j];
        }

        return answer;
    }
}

class Solution {
    public static void main(String[] args) {
        productExceptSelf obj = new productExceptSelf();
        int[] nums = { 1, 2, 3, 4 };
        int[] result = obj.productExceptSelfFunction(nums);
        System.out.println(Arrays.toString(result));
        ;
    }
}
