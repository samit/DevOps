import React from 'react';
import './App.css';
import NavBar from './components/NavBar';
import {BrowserRouter as Router}  from 'react-router-dom'
import NavBarToggle from './components/NavBarToggle';
 

function App() {
  return (
    <Router>
      <NavBar />
    <NavBarToggle />
    </Router>
  );
}

export default App;
