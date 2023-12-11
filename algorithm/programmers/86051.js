function solution(numbers) {
  const rule = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9];

  numbers.forEach((num) => {
    rule.splice(rule.indexOf(num), 1);
  });

  return rule.reduce((acc, curr) => acc + curr, 0);
}
