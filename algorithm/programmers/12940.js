function solution(n, m) {
  const answer = [getGCD(n, m), getLCM(n, m)];
  return answer;
}

// 최대공약수
function getGCD(a, b) {
  let gcd = 1;
  for (let i = 2; i <= Math.min(a, b); i++) {
    if (a % i === 0 && b % i === 0) {
      gcd = i;
    }
  }
  return gcd;
}

// 최소공배수
function getLCM(a, b) {
  const gcd = getGCD(a, b);
  const lcm = (a * b) / gcd;
  return lcm;
}
