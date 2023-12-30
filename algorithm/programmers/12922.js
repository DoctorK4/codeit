function solution(n) {
  return Array(n)
    .fill("")
    .map((v, i) => (i % 2 === 0 ? (v = "수") : (v = "박")))
    .join("");
}
