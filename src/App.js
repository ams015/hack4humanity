import "./App.css";
import { Router, Route, Link, useNavigate, Routes } from "react-router-dom";
import Login from "./Login";
import Map from "./Map";

function App() {
  return (
    <Routes>
      <Route path="/" element={<Login />}></Route>
      <Route path="/map" element={<Map />}></Route>
    </Routes>
  );
}

export default App;
