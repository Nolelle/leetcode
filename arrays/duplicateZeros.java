class Solution {
  public void duplicateZeros(int[] arr) {
    int zeroCount = 0;
    int arrMaxIndex = arr.length - 1;

    for (int i = 0; i <= arrMaxIndex - zeroCount; i++) {
      if (arr[i] == 0) {
        if (i == (arrMaxIndex - zeroCount)) {
          arr[i] = 0;
          arrMaxIndex -= 1;
          break;
        }
        zeroCount++;
      }
    }

    int last = arrMaxIndex - zeroCount;

    for (int j = last; j >= 0; j++) {
      if (arr[j] == 0) {
        arr[j + zeroCount] = 0;
        zeroCount--;
        arr[j + zeroCount] = 0;
      } else {
        arr[j + zeroCount] = arr[j];
      }
    }
  }
}