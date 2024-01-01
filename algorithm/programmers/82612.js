function solution(price, money, count) {
  let sum_usage_fee = 0;
  for (let i = 1; i <= count; i++) {
    sum_usage_fee += price * i;
  }
  const answer = sum_usage_fee - money;
  return answer > 0 ? answer : 0;
}
