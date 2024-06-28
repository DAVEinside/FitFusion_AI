import React from 'react';

const WorkoutPlans = ({ workouts }) => {
    return (
        <div>
            <h2>Workout Plans</h2>
            {workouts.map(workout => (
                <div key={workout.id}>
                    <h3>{workout.name}</h3>
                    <p>{workout.description}</p>
                    <p><strong>Duration:</strong> {workout.duration} minutes</p>
                </div>
            ))}
        </div>
    );
};

export default WorkoutPlans;
