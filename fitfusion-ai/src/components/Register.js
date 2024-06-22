import React, { useState } from 'react';
import axios from 'axios';

// Component for user registration form
const Register = ({ onSuccess }) => {
    const [username, setUsername] = useState('');  // State for username
    const [email, setEmail] = useState('');  // State for email
    const [password, setPassword] = useState('');  // State for password

    // Function to handle registration
    const handleRegister = async (e) => {
        e.preventDefault();
        console.log("Form submitted");
        console.log("Username:", username);
        console.log("Email:", email);
        console.log("Password:", password);

        try {
            // Send registration request to the backend
            const response = await axios.post('http://localhost:8000/register', {
                username,
                email,
                password,
            });
            console.log("Response:", response.data);
            if (onSuccess) {
                onSuccess(response.data.id);  // Call onSuccess with the user ID
            }
        } catch (error) {
            console.error("Error:", error);
            if (error.response) {
                console.error("Response Error:", error.response.data);
            }
        }
    };

    return (
        <div>
            <h2>Register</h2>
            <form onSubmit={handleRegister}>
                <input
                    type="text"
                    value={username}
                    onChange={(e) => setUsername(e.target.value)}
                    placeholder="Username"
                />
                <input
                    type="email"
                    value={email}
                    onChange={(e) => setEmail(e.target.value)}
                    placeholder="Email"
                />
                <input
                    type="password"
                    value={password}
                    onChange={(e) => setPassword(e.target.value)}
                    placeholder="Password"
                />
                <button type="submit">Register</button>
            </form>
        </div>
    );
};

export default Register;
