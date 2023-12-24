function solution(sizes) {
  const maxWarr = [];
  const maxHarr = [];
  sizes.forEach((item) => {
    if (item[0] >= item[1]) {
      maxWarr.push(item[0]);
      maxHarr.push(item[1]);
    } else {
      maxHarr.push(item[0]);
      maxWarr.push(item[1]);
    }
  });

  const maxW = Math.max(...maxWarr);
  const maxH = Math.max(...maxHarr);

  return maxW * maxH;
}
