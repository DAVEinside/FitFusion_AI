import React, { useState } from 'react';
import axios from 'axios';

const Register = () => {
    const [formData, setFormData] = useState({
        username: '',
        email: '',
        password: '',
        age: '',
        height: '',
        weight: '',
        fitness_goals: '',
        dietary_preferences: '',
        health_conditions: '',
        sex: ''
    });

    const handleChange = (e) => {
        setFormData({ ...formData, [e.target.name]: e.target.value });
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            const response = await axios.post('http://localhost:8000/register', formData);
            console.log(response.data);
            // Redirect to login page or dashboard
        } catch (error) {
            console.error('Error:', error.response.data);
        }
    };

    return (
        <div>
            <h1>Register</h1>
            <form onSubmit={handleSubmit}>
                <input
                    type="text"
                    name="username"
                    placeholder="Username"
                    value={formData.username}
                    onChange={handleChange}
                />
                <input
                    type="email"
                    name="email"
                    placeholder="Email"
                    value={formData.email}
                    onChange={handleChange}
                />
                <input
                    type="password"
                    name="password"
                    placeholder="Password"
                    value={formData.password}
                    onChange={handleChange}
                />
                <input
                    type="number"
                    name="age"
                    placeholder="Age"
                    value={formData.age}
                    onChange={handleChange}
                />
                <input
                    type="number"
                    name="height"
                    placeholder="Height"
                    value={formData.height}
                    onChange={handleChange}
                />
                <input
                    type="number"
                    name="weight"
                    placeholder="Weight"
                    value={formData.weight}
                    onChange={handleChange}
                />
                <input
                    type="text"
                    name="fitness_goals"
                    placeholder="Fitness Goals"
                    value={formData.fitness_goals}
                    onChange={handleChange}
                />
                <input
                    type="text"
                    name="dietary_preferences"
                    placeholder="Dietary Preferences"
                    value={formData.dietary_preferences}
                    onChange={handleChange}
                />
                <input
                    type="text"
                    name="health_conditions"
                    placeholder="Health Conditions"
                    value={formData.health_conditions}
                    onChange={handleChange}
                />
                 <input
                    type="text"
                    name="sex"
                    placeholder="Sex"
                    value={formData.sex}
                    onChange={handleChange}
                />
                <button type="submit">Register</button>
            </form>
        </div>
    );
};

export default Register;
