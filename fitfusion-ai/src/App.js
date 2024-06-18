import React from 'react';
import axios from 'axios';
import './App.css';

function App() {
    const [message, setMessage] = React.useState("");

    React.useEffect(() => {
        axios.get('http://localhost:8000/')
            .then(response => {
                setMessage(response.data.Hello);
            })
            .catch(error => {
                console.error("There was an error!", error);
            });
    }, []);

    return (
        <div className="App">
            <header className="App-header">
                <h1>{message}</h1>
            </header>
        </div>
    );
}

export default App;
