function solution(n, cars, links) {
  // 전체 주차장 개수, 각 주차장의 수용 가능한 자동차수, 주차장간의 연결 상태
  let answer = [];
  const graph = Array.from(Array(n + 1), () => []);
  links.forEach(([a, b]) => {
    graph[a].push(b);
    graph[b].push(a);
  });
  // console.log(graph);

  for (let i = 0; i < links.length; i++) {
    const visited = Array(n + 1).fill(false); // node번호 체킹
    const [a, b] = links[i];
    const result1 = bfs(a, b, visited, graph, cars);
    const result2 = bfs(b, a, visited, graph, cars);
    const gap = Math.abs(result1 - result2);
    answer.push(gap);
  }

  return Math.min(...answer);
  // return graph;
}

function bfs(start, exclude, visited, graph, cars) {
  const queue = [start];
  visited[start] = true;
  let count = cars[start - 1];

  while (queue.length > 0) {
    const current = queue.shift();
    for (linkedNode of graph[current]) {
      if (visited[linkedNode]) continue;
      if (linkedNode === exclude) continue;
      visited[linkedNode] = true;
      queue.push(linkedNode);
      count += cars[linkedNode - 1];
    }
  }

  return count;
}

const n1 = 13;
const cars1 = [22, 9, 1, 15, 8, 6, 20, 7, 11, 5, 10, 4, 1];
const links1 = [
  [4, 7],
  [13, 10],
  [6, 3],
  [7, 1],
  [6, 12],
  [5, 11],
  [5, 6],
  [5, 10],
  [9, 8],
  [8, 11],
  [8, 2],
  [7, 8],
];
// console.log(solution(n1, cars1, links1));
const n2 = 6;
const cars2 = [6, 4, 10, 9, 8, 4];
const links2 = [
  [4, 1],
  [3, 2],
  [1, 6],
  [3, 5],
  [5, 1],
];
// result = 3
console.log(solution(n2, cars2, links2));
