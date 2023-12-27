function solution(array, commands) {
  const answer = [];

  while (commands.length != 0) {
    const copy = [...array];
    const target = commands.shift();
    const [i, j, k] = target;

    // console.log('copy', copy);

    const cut = copy.splice(i - 1, j - i + 1).sort((a, b) => a - b);
    // console.log('cut', cut);

    answer.push(cut[k - 1]);
  }

  return answer;
}

/**
 * 1. sort로 정렬할 때 오름차순, 내림차순을 확실히 하기 위해 안에 콜백함수를 귀찮더라도 잘 적어두자.
 *
 */
