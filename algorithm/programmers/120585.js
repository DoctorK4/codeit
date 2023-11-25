function solution(array, height) {
  var answer = 0;
  Array.from(array, (el) => {
    if (height < el) {
      answer += 1;
    }
  });
  return answer;
}
