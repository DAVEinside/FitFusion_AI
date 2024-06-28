import React from 'react';

const MealPlans = ({ mealPlans }) => {
    return (
        <div>
            <h2>Meal Plans</h2>
            {mealPlans.map(mealPlan => (
                <div key={mealPlan.id}>
                    <h3>{mealPlan.name}</h3>
                    <p>{mealPlan.description}</p>
                    <p><strong>Calories:</strong> {mealPlan.calories}</p>
                </div>
            ))}
        </div>
    );
};

export default MealPlans;
