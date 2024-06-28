import React from 'react';

const Profile = ({ profile }) => {
    return (
        <div>
            <h2>Profile</h2>
            <p><strong>Username:</strong> {profile.username}</p>
            <p><strong>Email:</strong> {profile.email}</p>
            <p><strong>Age:</strong> {profile.age}</p>
            <p><strong>Height:</strong> {profile.height}</p>
            <p><strong>Weight:</strong> {profile.weight}</p>
            <p><strong>Fitness Goals:</strong> {profile.fitness_goals}</p>
            <p><strong>Dietary Preferences:</strong> {profile.dietary_preferences}</p>
            <p><strong>Health Conditions:</strong> {profile.health_conditions}</p>
        </div>
    );
};

export default Profile;
