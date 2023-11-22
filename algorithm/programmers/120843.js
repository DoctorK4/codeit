function solution(numbers, k) {
  const position = (2 * k - 1) % numbers.length;
  if (position === 0) return numbers.at(-1);
  const answer = numbers[position - 1];
  return answer;
}
