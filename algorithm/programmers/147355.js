function solution(t, p) {
  let answer = 0;

  for (let i = 0; i < t.length; i++) {
    const str = t.slice(i, i + p.length);
    // console.log(str);
    if (str.length === p.length && Number(str) <= Number(p)) answer += 1;
  }

  return answer;
}
