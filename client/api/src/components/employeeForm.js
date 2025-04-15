import React,{useState,useEffect} from 'react';
import { createEmployee, updateEmployee } from '../api';
import { ToastContainer, toast } from 'react-toastify';
import { Container } from 'react-bootstrap';


const EmployeeForm = ({ selectedEmployee, onFormSubmit }) => {
    const [employee, setEmployee] = useState({
        name: '', email: '', sallary: '', phone: '', address: ''
    });
    useEffect(() => {
        if (selectedEmployee) {
            setEmployee(selectedEmployee);
        }
    }, [selectedEmployee]);
    const handleChange = (e) => {
        setEmployee({ ...employee, [e.target.name]:e.target.value });
    };

    const handleSubmit = async (e) => {
        // e.preventDefault();
        if (employee.id) {
            toast.success("Data updated successfully !!!");
            await updateEmployee(employee.id, employee);
        } else {
            await createEmployee(employee);
            toast.success("Data Created successfully !!!");
        }
        onFormSubmit();
        setEmployee({ name: '', email: '', sallary: '', phone: '', address: '' });
    

    };

    return (
        <>
            <Container>
                <h5><ToastContainer /></h5>
            </Container>
            <form onSubmit={handleSubmit}>
                <input type="text" name="name" value={employee.name} onChange={handleChange} placeholder="Name" required />
                <input type="text" name="email" value={employee.email} onChange={handleChange} placeholder="Email" required />
                <input type="number" name="sallary" value={employee.sallary} onChange={handleChange} placeholder="sallary" required />
                <input type="number" name="phone" value={employee.phone} onChange={handleChange} placeholder="Phone number" required />
                <input type="text" name="address" value={employee.address} onChange={handleChange} placeholder="Address" required />
                <button id="btn-crt" type="submit">{employee.id ? "update" : "Create"}</button>
            </form>
        </>
          
    );

};
export default EmployeeForm;