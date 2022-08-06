package deletion;

class removeElement {
  public int remove(int[] nums, int val) {
    int k = 0;
    int r1 = nums.length - 1;
    for (int i = 0; i < nums.length; i++) {
      if (nums[i] == val) {
        nums[r1] = nums[i];
      }
    }
    return k;
  }
}
