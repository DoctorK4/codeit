function solution(n) {
  const three = n.toString(3);
  // console.log(three);

  let reverse = "";

  for (let i = three.length - 1; i >= 0; i--) {
    reverse += three[i];
  }

  return parseInt(reverse, 3);
}
