function solution(s1, s2) {
  const answer = new Set();
  for (el of s1) answer.add(el);
  for (el of s2) answer.add(el);
  // console.log(answer)
  return s1.length + s2.length - answer.size;
}
