import React, { useState } from 'react';
import Register from './components/Register';
import Login from './components/Login';
import Workout from './components/Workout';
import MealPlan from './components/MealPlan';

const App = () => {
    const [userId, setUserId] = useState(null);

    const handleLoginSuccess = (id) => {
        setUserId(id);
    };

    const handleRegisterSuccess = (id) => {
        setUserId(id);
    };

    return (
        <div>
            {userId ? (
                <div>
                    <h1>Welcome User {userId}</h1>
                    <Workout userId={userId} />
                    <MealPlan userId={userId} />
                </div>
            ) : (
                <div>
                    <Login onSuccess={handleLoginSuccess} />
                    <Register onSuccess={handleRegisterSuccess} />
                </div>
            )}
        </div>
    );
};

export default App;
