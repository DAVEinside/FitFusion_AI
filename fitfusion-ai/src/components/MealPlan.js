import React, { useState, useEffect } from 'react';
import axios from 'axios';

const MealPlan = ({ userId }) => {
    const [mealPlans, setMealPlans] = useState([]);

    useEffect(() => {
        const fetchMealPlans = async () => {
            const response = await axios.get(`http://localhost:8000/users/${userId}/meal_plans/`);
            setMealPlans(response.data);
        };

        fetchMealPlans();
    }, [userId]);

    return (
        <div>
            <h2>Meal Plans</h2>
            <ul>
                {mealPlans.map((mealPlan) => (
                    <li key={mealPlan.id}>{mealPlan.name}: {mealPlan.description}</li>
                ))}
            </ul>
        </div>
    );
};

export default MealPlan;
