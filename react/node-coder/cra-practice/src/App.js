import styles from "./App.module.css";
import { useState, useEffect } from "react";

function App() {
  const [toDo, setToDo] = useState("");
  const onChange = (e) => {
    setToDo((toDo) => e.target.value);
  };

  const onSubmit = (e) => {
    e.preventDefalut()
    if (toDo === ""){
      return;
    }
    setToDo("");
  }

  return (
    <div>
      <form onSubmit={onSubmit}>
        <input
          onChange={onChange}
          value={toDo}
          type="text"
          placeholder="Write your to do..."
        />
        <button>Add to Do</button>
      </form>
    </div>
  );
}

export default App;
