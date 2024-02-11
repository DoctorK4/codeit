function solution(s) {
  const memo = {};
  const answer = [];
  for (let i = 0; i < s.length; i++) {
    // memo에 없다면
    if (memo[s[i]] === undefined) answer.push(-1);
    // memo에 있다면
    else answer.push(i - memo[s[i]]);

    memo[s[i]] = i;
  }

  return answer;
}
