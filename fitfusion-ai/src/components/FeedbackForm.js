import React, { useState } from 'react';
import axios from 'axios';

const FeedbackForm = ({ user }) => {
    const [feedback, setFeedback] = useState('');

    const handleFeedbackSubmit = async (event) => {
        event.preventDefault();
        try {
            await axios.post(`http://localhost:8000/users/${user.id}/feedback`, { feedback });
            alert('Feedback submitted successfully');
        } catch (error) {
            console.error('Error submitting feedback:', error);
        }
    };

    return (
        <div>
            <h2>Feedback</h2>
            <form onSubmit={handleFeedbackSubmit}>
                <textarea
                    value={feedback}
                    onChange={(e) => setFeedback(e.target.value)}
                    placeholder="Enter your feedback"
                />
                <button type="submit">Submit Feedback</button>
            </form>
        </div>
    );
};

export default FeedbackForm;
