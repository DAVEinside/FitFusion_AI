import React, { useState, useEffect } from 'react';
import axios from 'axios';

const ProfileForm = ({ user }) => {
    const [profile, setProfile] = useState({});
    const [isEditing, setIsEditing] = useState(false);

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
    }, [user]);

    const handleProfileUpdate = async (event) => {
        event.preventDefault();
        try {
            const response = await axios.put(`http://localhost:8000/users/${user.id}`, profile);
            setProfile(response.data);
            setIsEditing(false);
        } catch (error) {
            console.error('Error:', error.response.data);
        }
    };

    const handleChange = (e) => {
        setProfile({
            ...profile,
            [e.target.name]: e.target.value,
        });
    };

    return (
        <div>
            <h1>Profile</h1>
            {isEditing ? (
                <form onSubmit={handleProfileUpdate}>
                    <input
                        type="text"
                        name="username"
                        placeholder="Username"
                        value={profile.username || ''}
                        onChange={handleChange}
                    />
                    <input
                        type="email"
                        name="email"
                        placeholder="Email"
                        value={profile.email || ''}
                        onChange={handleChange}
                    />
                    <input
                        type="number"
                        name="age"
                        placeholder="Age"
                        value={profile.age || ''}
                        onChange={handleChange}
                    />
                    <input
                        type="number"
                        name="height"
                        placeholder="Height (cm)"
                        value={profile.height || ''}
                        onChange={handleChange}
                    />
                    <input
                        type="number"
                        name="weight"
                        placeholder="Weight (kg)"
                        value={profile.weight || ''}
                        onChange={handleChange}
                    />
                    <input
                        type="text"
                        name="fitness_goals"
                        placeholder="Fitness Goals"
                        value={profile.fitness_goals || ''}
                        onChange={handleChange}
                    />
                    <input
                        type="text"
                        name="dietary_preferences"
                        placeholder="Dietary Preferences"
                        value={profile.dietary_preferences || ''}
                        onChange={handleChange}
                    />
                    <input
                        type="text"
                        name="health_conditions"
                        placeholder="Health Conditions"
                        value={profile.health_conditions || ''}
                        onChange={handleChange}
                    />
                    <button type="submit">Save</button>
                </form>
            ) : (
                <div>
                    <p>Username: {profile.username}</p>
                    <p>Email: {profile.email}</p>
                    <p>Age: {profile.age}</p>
                    <p>Height: {profile.height}</p>
                    <p>Weight: {profile.weight}</p>
                    <p>Fitness Goals: {profile.fitness_goals}</p>
                    <p>Dietary Preferences: {profile.dietary_preferences}</p>
                    <p>Health Conditions: {profile.health_conditions}</p>
                    <button onClick={() => setIsEditing(true)}>Edit Profile</button>
                </div>
            )}
        </div>
    );
};

export default ProfileForm;
