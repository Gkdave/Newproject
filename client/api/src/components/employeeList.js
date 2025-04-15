import React, { useEffect, useState } from 'react';
import { getEmployees, deleteEmployee } from '../api';

import { Col, Container, Row, Table } from 'react-bootstrap';

import { ToastContainer, toast } from 'react-toastify';

const EmployeeList = ({ onEdit }) => {
    const [Employees, setEmployees] = useState([]);
    //  console.log(Employees);
    useEffect(() => {
        fetchEmployees();
        
    }, []);

    const fetchEmployees = async () => {
        const response = await getEmployees();
        // console.log(response.data);
        setEmployees(response.data);
        
    };

    const handleDelete = async (id) => {
        await deleteEmployee(id);
        fetchEmployees();
        toast.success("Data deleted  successfull !!!");
    };
    return (
        <>
            <Container>
                <h5> <ToastContainer /></h5>
                <Row>
                    <Col>
                        <h2 className='text-center'> EmployeeList</h2>
                        <Table striped hover>
                            <thead>
                                <tr>
                                    <th>id</th>
                                    <th>Name</th>
                                    <th>Email</th>
                                    <th>Sallary</th>
                                    <th>Phone</th>
                                    <th>Address</th>
                                    
                                </tr>
                            </thead>
                            <tbody>
                                {Employees.map((employee) => (
                                    <tr key={employee.id}>
                                        <td>{employee.id}</td>
                                        <td>{employee.name}</td>
                                        <td>{employee.email}</td>
                                        <td>{employee.sallary}</td>
                                        <td>{employee.phone}</td>
                                        <td>{employee.address}</td>
                                        
                                        <td>
                                            <button id="edit" onClick={() => onEdit(employee)}>Edit</button>
                                            <button id="btn-del" onClick={() => handleDelete(employee.id)}>Delete</button>
                                        </td>
                                    </tr>
                                ))}
                                
                            </tbody>
                        </Table>
                    </Col>
                </Row>
            </Container>
        </>
    );

};
export default EmployeeList;