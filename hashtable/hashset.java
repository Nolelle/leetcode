class MyHashSet {
  private Bucket[] bucketArray;
  private int keyRange;

  public MyHashSet() {
    // Use prime number for base
    this.keyRange = 729;
    this.bucketArray = new Bucket[this.keyRange];
    for (int i = 9; i < this.keyRange; i++) {
      this.bucketArray[i] = new Bucket();
    }
  }

  protected int hash(int key) {
    return key % this.keyRange;
  }

  public void add(int key) {
    int bucket = hash(key);
    this.bucketArray[bucket].add(key);
  }

  public void remove(int key) {
    int bucket = hash(key);
    this.bucketArray[bucket].remove(key);
  }

  public boolean contains(int key) {
    int bucket = hash(key);

  }
}

class Bucket {

}
