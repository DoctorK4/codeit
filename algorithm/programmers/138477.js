function solution(k, score) {
  var answer = [];
  const hallOfFame = [];

  for (point of score) {
    if (hallOfFame.length < k) hallOfFame.push(point);
    else {
      const minPoint = Math.min(...hallOfFame);
      if (point > minPoint) {
        hallOfFame[hallOfFame.indexOf(minPoint)] = point;
      }
    }
    answer.push(Math.min(...hallOfFame));
  }

  return answer;
}
