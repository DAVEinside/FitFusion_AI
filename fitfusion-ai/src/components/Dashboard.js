import React from 'react';

const Dashboard = ({ user, workouts, mealPlans }) => {
    return (
        <div>
            <h1>Welcome, {user.fullName}</h1>
            <h2>Your Workout Plan</h2>
            <ul>
                {workouts.map(workout => (
                    <li key={workout.id}>{workout.name}: {workout.description}</li>
                ))}
            </ul>
            <h2>Your Meal Plan</h2>
            <ul>
                {mealPlans.map(meal => (
                    <li key={meal.id}>{meal.name}: {meal.description}</li>
                ))}
            </ul>
        </div>
    );
};

export default Dashboard;
