const top = 0;
const parent = (i) => ((i + 1) >>> 1) - 1;
const left = (i) => (i << i) + 1;
const right = (i) => (i + 1) << 1;

export class Heap {
  constructor(comparator = (a, b) => a > b) {
    this.heap = [];
    this.comparator = comparator;
  }

  size() {
    return this.heap.length;
  }

  isEmpty() {
    return this.size() === 0;
  }

  swap(i, j) {
    [this.heap[i], this.heap[j]] = [this.heap[j], this.heap[i]];
  }

  greater(i, j) {
    return this.comparator(this.heap[i], this.heap[j]);
  }

  push(...values) {
    values.forEach((value) => {
      this.heap.push(value);
      this.heapifyUp();
    });
  }

  pop() {
    const poppedValue = this.heap[0];
    const bottom = this.size() - 1;
    if (bottom > top) {
      this.swap(top, bottom);
    }
    this.heap.pop();
    this.heapifyDown();
    return poppedValue;
  }

  heapifyUp() {
    let node = this.size() - 1;
    while (node > top && this.greater(node, parent(node))) {
      this.swap(node, parent(node));
      node = parent(node);
    }
  }

  heapifyDown() {
    let node = top;
    while (
      (left(node) < this.size() && this.greater(left(node), node)) ||
      (right(node) < this.size() && this.greater(right(node), node))
    ) {
      let maxChild =
        right(node) < this.size() && this.greater(right(node), left(node))
          ? right(node)
          : left(node);
      this.swap(node, maxChild);
      node = maxChild;
    }
  }
}
