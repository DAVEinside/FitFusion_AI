import React, { useState, useEffect } from 'react';
import axios from 'axios';

const Workout = ({ userId }) => {
    const [workouts, setWorkouts] = useState([]);

    useEffect(() => {
        const fetchWorkouts = async () => {
            const response = await axios.get(`http://localhost:8000/users/${userId}/workouts/`);
            setWorkouts(response.data);
        };

        fetchWorkouts();
    }, [userId]);

    return (
        <div>
            <h2>Workouts</h2>
            <ul>
                {workouts.map((workout) => (
                    <li key={workout.id}>{workout.name}: {workout.description}</li>
                ))}
            </ul>
        </div>
    );
};

export default Workout;
