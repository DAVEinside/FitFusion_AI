import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { Link } from 'react-router-dom';

const Dashboard = ({ user }) => {
    const [profile, setProfile] = useState(null);
    const [mealPlan, setMealPlan] = useState('');
    const [workoutPlan, setWorkoutPlan] = useState('');

    useEffect(() => {
        const fetchProfile = async () => {
            try {
                const response = await axios.get(`http://localhost:8000/users/${user.id}`);
                setProfile(response.data);
            } catch (error) {
                console.error('Error:', error.response.data);
            }
        };

        fetchProfile();
    }, [user.id]);

    const generateMealPlan = async () => {
        try {
            const response = await axios.post('http://localhost:8000/generate_meal_plan', { user_id: user.id });
            setMealPlan(response.data.description);
        } catch (error) {
            console.error('Error:', error.response.data);
        }
    };

    const generateWorkoutPlan = async () => {
        try {
            const response = await axios.post('http://localhost:8000/generate_workout_plan', { user_id: user.id });
            setWorkoutPlan(response.data.description);
        } catch (error) {
            console.error('Error:', error.response.data);
        }
    };

    if (!profile) {
        return <div>Loading...</div>;
    }

    return (
        <div>
            <h1>Dashboard</h1>
            <div>
                <h2>Profile</h2>
                <p>Username: {profile.username}</p>
                <p>Email: {profile.email}</p>
                <p>Age: {profile.age}</p>
                <p>Height: {profile.height}</p>
                <p>Weight: {profile.weight}</p>
                <p>Fitness Goals: {profile.fitness_goals}</p>
                <p>Dietary Preferences: {profile.dietary_preferences}</p>
                <p>Health Conditions: {profile.health_conditions}</p>
                <p>Sex: {profile.sex}</p>
                <Link to="/profile/edit">Edit Profile</Link>
            </div>
            <div>
                <h2>Meal Plan</h2>
                <button onClick={generateMealPlan}>Generate Meal Plan</button>
                <p>{mealPlan}</p>
            </div>
            <div>
                <h2>Workout Plan</h2>
                <button onClick={generateWorkoutPlan}>Generate Workout Plan</button>
                <p>{workoutPlan}</p>
            </div>
        </div>
    );
};

export default Dashboard;
