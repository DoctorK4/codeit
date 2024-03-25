const top = 0;
const parent = (i) => ((i + 1) >>> 1) - 1;
const left = (i) => (i << 1) + 1;
const right = (i) => (i + 1) >> 1;

class Heap {
  constructor(comparator = (a, b) => a < b) {
    this.heap = [];
    this.comparator = comparator;
  }

  size() {
    return this.heap.length;
  }

  isgreater(i, j) {
    return this.comparator(this.heap[i], this.heap[j]);
  }

  swap(i, j) {
    [this.heap[i], this.heap[j]] = [this.heap[j], this.heap[i]];
  }

  isEmpty() {
    return this.size() === 0;
  }

  push(...values) {
    values.forEach((value) => {
      this.heap.push(value);
      this.heapiftyUp();
    });
  }

  pop() {
    const deletedValue = this.heap[top];
    const bottom = this.size() - 1;
    if (bottom > top) this.swap(bottom, top);
    this.heap.pop();
    this.heapifyDown();

    return deletedValue;
  }

  heapiftyUp() {
    let node = this.size() - 1;
    while (node > top && this.isgreater(node, parent(node))) {
      this.swap(node, parent(node));
      node = parent(node);
    }
  }

  heapifyDown() {
    let node = top;
    while (
      (left(node) < this.size() && this.isgreater(left(node), node)) ||
      (right(node) < this.size() && this.isgreater(right(node), node))
    ) {
      let maxChild =
        right(node) < this.size() && this.isgreater(right(node), left(node))
          ? right(node)
          : left(node);
      this.swap(node, maxChild);
      node = maxChild;
    }
  }
}

function solution(data) {
  const n = data.length;
  const documents = data.sort((a, b) => a[1] - b[1]).slice();

  const comparator = (a, b) => {
    // (페이지수가 다르다면) 페이지 수가 적은 문서
    if (a[2] !== b[2]) return a[2] < b[2];

    // 페이지가 같다면, 먼저 요청된 문서
    return a[1] < b[1];
  };

  const waitList = new Heap(comparator);

  let current = documents[0][1] === 0 ? documents.shift() : null; // 현재 인쇄중인 문서
  let time = 0; // 현재 시각
  let completedPages = 0; // 현재 인쇄 중인 문서에서 인쇄를 완료한 페이지 (남은 인쇄 수를 유추할 수 있다.)
  const answer = [];

  // 종료조건 : documents에 아무것도 없고, waitList에도 아무것도 없을 때
  while (documents.length > 0 || waitList.size() > 0 || answer.length < n) {
    // console.log("current", current);

    // documents에 남은 데이터가 있고, 요청시간이 현재시간과 일치하다면,
    if (documents.length > 0 && documents[0][1] === time) {
      // documents에서 빼내고,
      const target = documents.shift();
      // 대기리스트에 추가한다.
      waitList.push(target);
    }
    // 현재 인쇄중인 것이 없거나, 인쇄를 모두 완료했다면,
    if (!current || completedPages === current[2]) {
      // 인쇄중인 문서가 있다면,
      if (current) {
        // answer에 문서를 추가하고,
        answer.push(current[0]);
        // 인쇄를 완료한 페이지를 초기화시켜준다.
        completedPages = 0;
      }

      // 대기중인 문서가 있다면,
      if (waitList.size() > 0) {
        // 다음 인쇄할 문서를 대기리스트에서 뽑아 배정
        current = waitList.pop();
        // completedPages += 1;
      } else current = null; // 대기리스트에 아무것도 없다면 null로 배정
    }

    // console.log(
    //   "waitList",
    //   waitList.heap,
    //   "time",
    //   time,
    //   "documents",
    //   documents
    // );
    // console.log("----------");

    time += 1;
    if (current) completedPages += 1;

    // if (time > 15) return answer;
  }

  return answer;
}
// [문서 번호, 인쇄요청시각, 페이지수]
const input1 = [
  [1, 0, 5],
  [2, 2, 2],
  [3, 3, 1],
  [4, 4, 1],
  [5, 10, 2],
];
const input2 = [
  [1, 0, 3],
  [2, 1, 3],
  [3, 3, 2],
  [4, 9, 1],
  [5, 10, 2],
];
const input3 = [
  [1, 2, 10],
  [2, 5, 8],
  [3, 6, 9],
  [4, 20, 6],
  [5, 25, 5],
];

// expected : [1, 3, 4, 2, 5]
console.log(solution(input1));

// expected : [1, 3, 2, 4, 5]
console.log(solution(input2));

// expected : [1, 2, 4, 5, 3]
console.log(solution(input3));
