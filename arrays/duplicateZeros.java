class Solution {
  public void duplicateZeros(int[] arr) {
    int extraZeros = 0;
    int l = arr.length - 1;
    for (int i = 0; i <= l - extraZeros; i++) {
      if (arr[i] == 0) {
        if (i == l - extraZeros) {
          arr[l] = 0;
          l -= 1;
          break;
        }
        extraZeros++;
      }
    }
    for (int k = l - extraZeros; k >= 0; k--) {
      if (arr[k] == 0) {
        arr[k + extraZeros] = 0;
        extraZeros--;
        arr[k + extraZeros] = 0;
      } else {
        arr[k + extraZeros] = arr[k];
      }
    }
  }
}
