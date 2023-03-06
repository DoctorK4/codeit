import ReactDOM from "react-dom";

const WINS = {
  rock: "scissor",
  scissor: "paper",
  paper: "rock",
};

const root = document.getElementById("root");

function getResult(left, right) {
  if (WINS[left] === right) return "승리";
  else if (left === WINS[right]) return "패배";
  return "무승부";
}

function handleClick() {
  console.log("가위바위보!");
}

const me = "rock";
const other = "scissor";

const result = getResult(me, other);

ReactDOM.render(
  <>
    <h1>가위바위보</h1>
    <h2>{result}</h2>
    <button onClick={handleClick}>가위</button>
    <button onClick={handleClick}>바위</button>
    <button onClick={handleClick}>보</button>
  </>,
  root
);
