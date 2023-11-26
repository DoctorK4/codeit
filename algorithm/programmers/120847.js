function solution(numbers) {
  const highest = Math.max(...numbers);
  // console.log(highest);
  numbers.splice(numbers.indexOf(highest), 1);
  // console.log(numbers);
  const second = Math.max(...numbers);
  return second * highest;
}
