function solution(array, n) {
  let answer = 0;
  array.forEach((num) => {
    if (num === n) answer += 1;
  });

  return answer;
}
