function solution(food) {
  const [water, ...foods] = food;
  const arr = [];
  for (let i = 0; i < foods.length; i++) {
    const str = String(i + 1);
    const count = Math.floor(foods[i] / 2);
    arr.push(str.repeat(count));
  }
  const reversedArr = [...arr].reverse();
  const answer = arr.join("") + String(0) + reversedArr.join("");

  return answer;
}
