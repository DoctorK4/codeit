function solution(my_string) {
  const vowel = ["a", "e", "i", "o", "u"];
  let answer = "";
  for (let letter of my_string) {
    if (!vowel.includes(letter)) answer += letter;
  }
  return answer;
}
