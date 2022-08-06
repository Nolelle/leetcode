// Solution 1 
// import java.util.Arrays;
// public class mergeSortedArray {
//   public void merge(int[] nums1, int m, int[] nums2, int n) {
//     for (int i = 0; i < n; i++) {
//       nums1[i + m] = nums2[i];
//     }
//     Arrays.sort(nums1);
//     return;
//   }
// }
// Time Complexity: O(N) with the Sorting Function in Java O((M+N)log(M+N))
// Space Complexity: O(1) with the Sorting Function in Java O((log(M+N))

// Solution 2: Merge Sort Algorithm
public class mergeSortedArray {
  public void merge(int[] nums1, int m, int[] nums2, int n) {
    int r1 = m - 1;
    int r2 = n - 1;
    for (int w = m + n - 1; w >= 0; w--) {
      if (r1 >= 0 && r2 >= 0) {
        nums1[w] = nums1[r1] > nums2[r2] ? nums1[r1--] : nums2[r2--];
      } else if (r1 >= 0) {
        nums1[w] = nums1[r1--];
      } else {
        nums1[w] = nums1[r2--];
      }
    }
    return;
  }
}

// Time Complexity = O(M+N)
// Space Complexity: O(1)