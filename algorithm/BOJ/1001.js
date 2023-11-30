const fs = require("fs");
const input = fs.readFileSync("./dev/stdin.txt").toString().split(" ");

console.log(input[0] - input[1]);
