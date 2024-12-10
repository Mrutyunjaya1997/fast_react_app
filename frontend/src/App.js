import React, { useState } from "react";
import axios from "axios";
import Greeting from "./components/Greeting";

const App = () => {
  const [name, setName] = useState("");
  const [greeting, setGreeting] = useState("");

  // const fetchGreeting = async () => {
  //   try {
  //     const response = await axios.get(`http://127.0.0.1:8000/greet/${name}`);
  //     setGreeting(response.data.message);
  //   } catch (error) {
  //     console.error("Error fetching greeting:", error);
  //   }
  // };

  const fetchGreeting = async () => {
    const API_BASE_URL =
      process.env.NODE_ENV === "development"
        ? "http://127.0.0.1:8000"
        : "https://backed-fast-api.onrender.com";
  
    try {
      const response = await axios.get(`${API_BASE_URL}/greet/${name}`);
      setGreeting(response.data.message);
    } catch (error) {
      console.error("Error fetching greeting:", error);
    }
  };
  

  return (
    <div style={{ textAlign: "center", marginTop: "50px" }}>
      <h1>React + FastAPI App</h1>
      <input
        type="text"
        placeholder="Enter your name"
        value={name}
        onChange={(e) => setName(e.target.value)}
      />
      <button onClick={fetchGreeting}>Get Greeting</button>
      <Greeting message={greeting} />
    </div>
  );
};

export default App;
