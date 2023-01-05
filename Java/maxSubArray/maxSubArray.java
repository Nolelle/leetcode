// Time Complexity: O(n^2)
// Space Complexity:O(1);
// class maxSubArray {
//     public int maxSubArrayFunction(int[] nums) {
//         int maxSubArray = Integer.MIN_VALUE;
//         for (int i = 0; i < nums.length; i++) {
//             int currentSubArray = 0;
//             for (int j = i; j < nums.length; j++) {
//                 currentSubArray += nums[j];
//                 if (currentSubArray > maxSubArray) {
//                     maxSubArray = currentSubArray;
//                 }
//             }
//         }
//         return maxSubArray;
//     }
// }

// Time Complexity: O(n)
// Space Complexity: O(1)
// Kadanes Algo
// class maxSubArray {
//     public int maxSubArrayFunction(int[] nums) {
//         int n = nums.length;
//         int local_max = 0;
//         int global_max = Integer.MIN_VALUE;
//         for (int i = 0; i < n; i++) {
//             local_max = Math.max(nums[i], local_max + nums[i]);
//             if (local_max > global_max) {
//                 global_max = local_max;
//             }
//         }
//         return global_max;
//     }
// }

// Divide and Conquer
// Time Complexity: O(nlogn)
// Space Complexity: O(n)

class maxSubArray {
    private int[] numsArray;

    public int maxSubArrayFunction(int[] nums) {
        numsArray = nums;
        return findBestSubArray(0, numsArray.length - 1);
    }

    public int findBestSubArray(int left, int right) {
        if (left > right) {
            return Integer.MIN_VALUE;
        }
        int mid = Math.floorDiv(left + right, 2);
        int curr = 0;
        int bestLeftSum = 0;
        int bestRightSum = 0;

        for (int j = mid - 1; j > left; j--) {
            curr += numsArray[j];
            bestLeftSum = Math.max(bestLeftSum, curr);
        }

        for (int i = mid + 1; i <= right; i++) {
            curr += numsArray[i];
            bestRightSum = Math.max(curr, bestRightSum);
        }

        int bestCombinedSum = numsArray[mid] + bestLeftSum + bestRightSum;
        int leftHalf = findBestSubArray(left, mid - 1);
        int rightHalf = findBestSubArray(mid + 1, right);
        return Math.max(bestCombinedSum, Math.max(leftHalf, rightHalf));
    }
}

class Solution {
    public static void main(String[] args) {
        int[] nums = { -2, 1, -3, 4, -1, 2, 1, -5, 4 };
        maxSubArray maxSubArray = new maxSubArray();
        int result = maxSubArray.maxSubArrayFunction(nums);
        System.out.println(result);
    }
}
