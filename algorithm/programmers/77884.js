function solution(left, right) {
  let answer = 0;
  const target = Array(right - left + 1)
    .fill(0)
    .map((v, i) => Number(left + i));
  console.log(target);

  target.forEach((num) => {
    const divisors = getDivisors(num);
    // const sumOfDivisors = divisors.reduce((acc, curr) => acc + curr, 0);
    divisors.length % 2 === 0 ? (answer += num) : (answer -= num);
  });

  return answer;
}

function getDivisors(num) {
  const divisors = [];
  for (let i = 1; i <= Math.sqrt(num); i++) {
    if (num % i === 0) {
      divisors.push(i);
      if (num / i !== i) divisors.push(num / i);
    }
  }
  return divisors;
}
