import logo from './logo.svg';
import './App.css';
import React, { useState } from 'react';
import EmployeeList from './components/employeeList';
import EmployeeForm from './components/employeeForm';

function App() {
  const [selectedEmployee, setSelectedEmployee] = useState(null);
  return (
    <>
    <div className="App">
       <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        
      </header> 
      <h1>CRUD App with Django $ React </h1>
      <EmployeeForm selectedEmployee={selectedEmployee} onFormSubmit={() => setSelectedEmployee(null)} />
        <EmployeeList onEdit={setSelectedEmployee} /> 
        </div> 
    </>
  );
}

export default App;
