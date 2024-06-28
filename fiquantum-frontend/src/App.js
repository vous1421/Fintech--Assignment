import 'bootstrap/dist/css/bootstrap.min.css'; 
import React, { useState } from 'react';
import axios from 'axios';

function App() {
  const [inputData, setInputData] = useState('');
  const [result, setResult] = useState('');

  const handleSubmit = async (event) => {
    event.preventDefault();
    try {
      const response = await axios.post('http://127.0.0.1:5000/optimize', { data: inputData }, {
        headers: {
          'Content-Type': 'application/json',
        },
      });
      setResult(response.data.result);
    } catch (error) {
      console.error('Error optimizing portfolio', error);
    }
  };

  return (
    <div className="App">
      <header className="App-header">
        <h1>FiQuantum</h1>
        <form onSubmit={handleSubmit}>
          <label>
            Input Data:
            <textarea value={inputData} onChange={(e) => setInputData(e.target.value)} />
          </label>
          <button type="submit">Optimize Portfolio</button>
        </form>
        <div>
          <h2>Result:</h2>
          <pre>{result}</pre>
        </div>
      </header>
    </div>
  );
}

export default App;
