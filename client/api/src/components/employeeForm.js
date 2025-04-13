import React,{useState,useEffect} from 'react';
import { createEmployee, updateEmployee } from '../api';
import { ToastContainer, toast } from 'react-toastify';
import { Container } from 'react-bootstrap';


const EmployeeForm = ({ selectedEmployee, onFormSubmit }) => {
    const [employee, setEmployee] = useState({
        name: '', emp_id: '', phone: '', address: '',working:'',department:''
    });
    useEffect(() => {
        if (selectedEmployee) {
            setEmployee(selectedEmployee);
        }
    }, [selectedEmployee]);
    const handleChange = (e) => {
        setEmployee({ ...employee, [e.target.name]: e.target.value });
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
        setEmployee({ name: '', emp_id: '', phone: '', address: '', working: '', department: '' });
    

    };

    return (
        <>
            <Container>
                <h5><ToastContainer /></h5>
            </Container>
            <form onSubmit={handleSubmit}>
                <input type='text' name='name' value={employee.name} onChange={handleChange} placeholder='Name' required  />
                <input type='text'  name='emp_id' value={employee.emp_id} onChange={handleChange} placeholder='Emp_ID' required /> 
                <input type='number' name='phone' value={employee.phone} onChange={handleChange} placeholder='PHONE' required /> 
                <input type='text'  name='address' value={employee.address} onChange={handleChange} placeholder='Address' required /> 
                <input type='text'  name='working' value={employee.working}  onChange={handleChange} placeholder='Working' required /> 
                <input type='text'  name='department' value={employee.department} onChange={handleChange} placeholder='Department' required /> 
                
        </form>


        </>
            
    )

};
export default EmployeeForm;