function solution(s) {
  return s.length % 2 === 0
    ? s
        .split("")
        .splice(s.length / 2 - 1, 2)
        .join("")
    : s[Math.floor(s.length / 2)];
}
