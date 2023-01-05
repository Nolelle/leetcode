package deletion;

public class removeDuplicates {
    public int removeDups(int[] nums) {
        // j will be use to track of unique elemeents, starts at 1 because we assume
        // that the first element is unique.
        int j = 1;
        int l = nums.length;
        if (l == 0) {
            return 0;
        }
        for (int i = 1; i < l; i++) {
            if (nums[i] != nums[i - 1]) {
                nums[j] = nums[i];
                j++;
            }
        }
        return j;
    }
}

// Time Complexity: O(n)
// Space Complexity: O(1)
