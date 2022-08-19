package search;

import java.util.Arrays;

class Solution {
  public boolean checkIfExists(int[] arr) {
    if (arr == null || arr.length == 0) {
      return false;
    }
    // Linear Search
    for (int j = 0; j < arr.length; j++) {
      for (int i = arr.length - 1; i >= 0; i--) {
        if (i != j && arr[i] == 2 * arr[j]) {
          return true;
        }
      }
    }
    return false;
  }
  // Time Complexity: O(n^2)
  // Space Complexity: O(1)

  // boolean binarySearch(int[] arr, int target) {
  // Arrays.sort(arr);
  // int left = 0;
  // int right = arr.length - 1;
  // while (left <= right) {
  // int mid = (left + (right - left)) / 2;
  // if (target < mid) {
  // right = mid - 1;
  // } else if (target > mid) {
  // left = mid + 1;
  // } else {
  // return true;
  // }
  // }
  // return false;
  // }

  // public boolean checkIfExists(int[] arr) {
  // if (arr == null || arr.length == 0) {
  // return false;
  // }
  // // Binary Search
  // int l = arr.length;
  // for (int i = 0; i < l; i++) {
  // int target = 2 * arr[i];
  // if (binarySearch(arr, target)) {
  // return true;
  // }
  // }
  // return false;
  // }
}
