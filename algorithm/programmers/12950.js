function solution(arr1, arr2) {
  const row = arr1.length;
  const col = arr1[0].length;
  const answer = Array.from(Array(row), () => Array(col).fill(0));

  for (let i = 0; i < row; i++) {
    for (let j = 0; j < col; j++) {
      answer[i][j] = arr1[i][j] + arr2[i][j];
    }
  }

  return answer;
}
