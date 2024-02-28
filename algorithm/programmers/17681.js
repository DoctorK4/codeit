function solution(n, arr1, arr2) {
  const answer = [];
  console.log(answer);

  for (let i = 0; i < arr1.length; i++) {
    let line = "";
    let str1 = arr1[i].toString(2);
    let str2 = arr2[i].toString(2);

    while (str1.length < n) {
      str1 = "0" + str1;
    }
    while (str2.length < n) {
      str2 = "0" + str2;
    }

    for (let j = 0; j < str1.length; j++) {
      if (str1[j] === "1" || str2[j] === "1") {
        line = line + "#";
      } else {
        line = line + " ";
      }
    }

    answer.push(line);
  }

  return answer;
}
