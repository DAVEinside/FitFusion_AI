import React, { useState } from 'react';
import Register from './components/Register';
import Login from './components/Login';
import ProfileForm from './components/ProfileForm';

const App = () => {
    const [isLoggedIn, setIsLoggedIn] = useState(false);
    const [user, setUser] = useState(null);

    const handleLogin = (userData) => {
        setUser(userData);
        setIsLoggedIn(true);
    };

    return (
        <div>
            {!isLoggedIn ? (
                <div>
                    <Register onRegister={handleLogin} />
                    <Login onLogin={handleLogin} />
                </div>
            ) : (
                <ProfileForm user={user} />
            )}
        </div>
    );
};

export default App;
