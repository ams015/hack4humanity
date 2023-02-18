import "./App.css";
import { Router, Route, Link, useNavigate, Routes } from "react-router-dom";
import Login from "./Login";

function App() {
  return (
    <Routes>
      <Route path="/" element={<Login />}></Route>
    </Routes>
  );
}

export default App;
