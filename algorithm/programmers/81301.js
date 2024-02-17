function solution(s) {
  let answer = "";
  let str = "";

  for (let i = 0; i < s.length; i++) {
    if (isNaN(Number(s[i]))) {
      str += s[i];
      if (
        (numberDict[str] !== undefined) |
        !isNaN(Number(s[i + 1])) |
        (i === s.length - 1)
      ) {
        answer += numberDict[str];
        str = "";
      }
    } else {
      answer += s[i];
    }
    // console.log(answer, str)
  }

  return Number(answer);
}

const numberDict = {
  zero: 0,
  one: 1,
  two: 2,
  three: 3,
  four: 4,
  five: 5,
  six: 6,
  seven: 7,
  eight: 8,
  nine: 9,
};
