function solution(arr) {
  const min = Math.min(...arr);
  const index = arr.indexOf(min);
  arr.splice(index, 1);

  return arr.length === 0 ? [-1] : arr;
}
