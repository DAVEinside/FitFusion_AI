import React, { useState, useEffect } from 'react';
import axios from 'axios';

const ProfileForm = ({ user }) => {
    const [profile, setProfile] = useState(user);

    const handleProfileUpdate = async (event) => {
        event.preventDefault();
        try {
            const response = await axios.put(`http://localhost:8000/users/${user.id}`, profile);
            setProfile(response.data);
        } catch (error) {
            console.error('Error:', error.response.data);
        }
    };

    const handleChange = (e) => {
        setProfile({ ...profile, [e.target.name]: e.target.value });
    };

    useEffect(() => {
        const fetchProfile = async () => {
            try {
                const response = await axios.get(`http://localhost:8000/users/${user.id}`);
                setProfile(response.data);
            } catch (error) {
                console.error('Error:', error.response?.data || error.message);
            }
        };

        fetchProfile();
    }, [user.id]);

    return (
        <div>
            <h1>Profile</h1>
            <form onSubmit={handleProfileUpdate}>
                <input
                    type="text"
                    name="full_name"
                    placeholder="Full Name"
                    value={profile.full_name || ''}
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
                    placeholder="Height"
                    value={profile.height || ''}
                    onChange={handleChange}
                />
                <input
                    type="number"
                    name="weight"
                    placeholder="Weight"
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
                <button type="submit">Update Profile</button>
            </form>
        </div>
    );
};

export default ProfileForm;
