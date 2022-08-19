package search;

public class validMountainArray {
  public boolean validation(int[] arr) {
    if (arr.length < 3) {
      return false;
    }
    int biggestIntIndex = 0;
    for (int i = 0; i < arr.length; i++) {
      if (arr[i] > biggestIntIndex) {
        biggestIntIndex = i;
      }
    }
    for (int j = 0; j < biggestIntIndex - 1; j++) {
      if (arr[j + 1] - arr[j] <= 0) {
        return false;
      }
    }
    for (int k = biggestIntIndex; k < arr.length - 1; k++) {
      if (arr[k] - arr[k + 1] <= 0) {
        return false;
      }
    }
    return true;
  }
}