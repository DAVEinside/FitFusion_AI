import React, { useState } from 'react';
import Register from './components/Register';
import Workout from './components/Workout';
import MealPlan from './components/MealPlan';

// Main App component
const App = () => {
    const [userId, setUserId] = useState(null);

    const handleRegistrationSuccess = (id) => {
        setUserId(id);  // Set the user ID after successful registration
    };

    return (
        <div>
            <Register onSuccess={handleRegistrationSuccess} />  {/* Include the Register component */}
            {userId && (
                <div>
                    <Workout userId={userId} />  {/* Include the Workout component */}
                    <MealPlan userId={userId} />  {/* Include the MealPlan component */}
                </div>
            )}
        </div>
    );
};

export default App;
