// src/components/Dashboard.js
import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { Link } from 'react-router-dom';

const Dashboard = ({ user }) => {
    const [profile, setProfile] = useState(null);

    useEffect(() => {
        const fetchProfile = async () => {
            try {
                const response = await axios.get(`http://localhost:8000/users/${user.id}`);
                setProfile(response.data);
            } catch (error) {
                console.error('Error:', error.response?.data || error.message);
            }
        };

        if (user?.id) {
            fetchProfile();
        }
    }, [user]);

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
                <Link to="/profile/edit">Edit Profile</Link>
            </div>
        </div>
    );
};

export default Dashboard;
