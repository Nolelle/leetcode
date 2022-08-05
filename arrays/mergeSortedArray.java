public class mergeSortedArray {
  public void merge(int[] nums1, int m, int[] nums2, int n) {
    for (int i = 0; i < m; i++) {
      if (nums2[i] >= nums1[i] && nums2[i] < nums1[i + 1]) {
        nums1[i + 1] = nums2[i];
      } else if (nums2[i] < nums1[i]) {
        nums1[i - 1] = nums2[i];
      }
    }
  }
}