function solution(a, b, n) {
  let answer = 0;
  let current = n;

  while (Math.floor(current / a) !== 0) {
    const newBottle = Math.floor(current / a) * b;
    // console.log(newBottle, 'newBottle');
    // console.log(current, 'current');
    answer += newBottle;
    current = newBottle + (current % a);
  }

  return answer;
}

/**
n개를 가져다주면 총 몇 병을 받을 수 있을까
n = 20
20 / 2 = 10병 추가로 받음
10 / 2 = 5병 받음
5 / 2 = 2병 받음
2병 + 1병 / 2 = 1병받음 ... 1병
2 / 2 = 1병....0병


*/
