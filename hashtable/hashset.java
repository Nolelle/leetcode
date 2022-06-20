import java.util.LinkedList;

class MyHashSet {
  // fields
  private Bucket[] bucketArray;
  private int keyRange;

  // constructor
  public MyHashSet() {
    // Use prime number for base
    this.keyRange = 729;
    this.bucketArray = new Bucket[this.keyRange];
    for (int i = 0; i < this.keyRange; ++i) {
      this.bucketArray[i] = new Bucket();
    }
  }

  protected int hash(int key) {
    return key % this.keyRange;
  }

  public void add(int key) {
    int bucketIndex = this.hash(key);
    this.bucketArray[bucketIndex].insert(key);
  }

  public void remove(int key) {
    int bucketIndex = this.hash(key);
    this.bucketArray[bucketIndex].delete(key);
  }

  public boolean contains(int key) {
    int bucketIndex = this.hash(key);
    return this.bucketArray[bucketIndex].exists(key);
  }
}

class Bucket {
  private LinkedList<Integer> container;

  public Bucket() {
    container = new LinkedList<Integer>();
  }

  public void insert(int key) {
    int index = this.container.indexOf(key);
    // returns -1 if no value found
    if (index == -1) {
      this.container.addFirst(key);
    }
  }

  public void delete(int key) {
    this.container.remove(key);
  }

  public boolean exists(int key) {
    int index = this.container.indexOf(key);
    return index != -1;
  }
}
