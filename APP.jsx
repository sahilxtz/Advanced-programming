import { useState } from "react";
import "./App.css";

export default function App() {
  const [text, setText] = useState("");
  const [list, setList] = useState([]);

  const add = () => {
    if (!text.trim()) return;

    setList([...list, { t: text, d: false }]);
    setText("");
  };

  const toggle = (i) => {
    const copy = [...list];
    copy[i].d = !copy[i].d;
    setList(copy);
  };

  const remove = (i) => {
    setList(list.filter((_, x) => x !== i));
  };

  return (
    <div className="bg">
      <div className="todo-box">
        <h1>✨ My Tasks</h1>

        <div className="row">
          <input
            value={text}
            onChange={(e) => setText(e.target.value)}
            placeholder="Type your task..."
          />
          <button onClick={add}>Add</button>
        </div>

        {list.map((x, i) => (
          <div
            className={`item ${x.d ? "done" : ""}`}
            key={i}
          >
            <span onClick={() => toggle(i)}>{x.t}</span>
            <b onClick={() => remove(i)}>✖</b>
          </div>
        ))}
      </div>
    </div>
  );
}