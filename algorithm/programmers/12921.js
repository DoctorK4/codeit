function solution(n) {
  let check = Array(n + 1)
    .fill()
    .map((v, i) => false);
  console.log(check);
  const answer = [];

  for (let i = 2; i <= n; i++) {
    if (!check[i]) {
      answer.push(i);

      for (let j = i + i; j <= n; j += i) {
        check[j] = true;
        // console.log(check)
      }
    }
  }
  return answer.length;
}

// 에라토스테네스의 체 로직을 듣고 직접 짠 코드
// function solution (n) {
//   let arr = Array.from({length: n-1}, (v, i) => i+2);
//   let answer = 0;

//   while (arr.length > 0) {
//     // console.log('arr', arr)
//     // 1. 맨 앞 숫자를 소수로 간주
//     const target = arr.shift();
//     answer += 1;
//     // console.log('target', target);

//     // 2. 그것으로 나눠떨어지는 수들을 제거
//     arr = arr.filter(num => num % target !== 0);
//   }
//   return answer;
// }

/**
 * 효율성 통과 못한 코드 ㅠㅠ
 * 
 * function solution(n) {
  if (n === 2) return 1;
    
  let answer = 1; // 2를 포함한 소수의 개수 합
  for (let i = 3; i < n+1; i += 2) {
    if (i !== 3 && i % 3 === 0) continue;
    if (isPrime(i)) answer += 1;
  }
    
  return answer;
}

function isPrime(num) {
  if (num === 2 || num === 3) return true;
  if (num % 2 === 0 || num % 3 === 0) return false;
    
  let num_sqrt = Math.sqrt(num);
    
  for (let i = 2; i <= num_sqrt; i++) {
    if (num % i === 0) return false;
  }
  return true;
}   
 */
