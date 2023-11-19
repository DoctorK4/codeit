function solution(absolutes, signs) {
  let answer = 0;
  for (let i = 0; i < absolutes.length; i++) {
    let multiple = signs[i] ? 1 : -1;
    answer += absolutes[i] * multiple;
  }
  return answer;
}
