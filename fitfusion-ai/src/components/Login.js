import React, { useState } from 'react';
import axios from 'axios';

const Login = () => {
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const [userData, setUserData] = useState(null);

    const handleLogin = async (event) => {
        event.preventDefault();
        try {
            const response = await axios.post('http://localhost:8000/login', {
                username: username,
                password: password,
            });
            setUserData(response.data);
        } catch (error) {
            console.error('Error:', error.response.data);
        }
    };

    return (
        <div>
            <h1>Login</h1>
            <form onSubmit={handleLogin}>
                <input
                    type="text"
                    placeholder="Username"
                    value={username}
                    onChange={(e) => setUsername(e.target.value)}
                />
                <input
                    type="password"
                    placeholder="Password"
                    value={password}
                    onChange={(e) => setPassword(e.target.value)}
                />
                <button type="submit">Login</button>
            </form>
            {userData && (
                <div>
                    <h2>Welcome, {userData.username}!</h2>
                    <h3>Meal Plans</h3>
                    <ul>
                        {userData.meal_plans.map((plan) => (
                            <li key={plan.id}>{plan.title}: {plan.description}</li>
                        ))}
                    </ul>
                    <h3>Workout Plans</h3>
                    <ul>
                        {userData.workouts.map((workout) => (
                            <li key={workout.id}>{workout.title}: {workout.description}</li>
                        ))}
                    </ul>
                </div>
            )}
        </div>
    );
};

export default Login;
