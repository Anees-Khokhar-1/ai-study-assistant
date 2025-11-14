import React, { useState } from 'react';
import axios from 'axios';

function App() {
  const [file, setFile] = useState(null);
  const [summary, setSummary] = useState("");

  const handleFileChange = (e) => {
    setFile(e.target.files[0]);
  };

  const handleUpload = async () => {
    const formData = new FormData();
    formData.append('file', file);
    
    const response = await axios.post('http://localhost:8000/api/upload', formData, {
      headers: { 'Content-Type': 'multipart/form-data' }
    });

    setSummary(response.data.summary);
  };

  return (
    <div className="App">
      <h1>AI Study Assistant</h1>
      <input type="file" onChange={handleFileChange} />
      <button onClick={handleUpload}>Upload & Summarize</button>
      <div>
        <h2>Summary</h2>
        <p>{summary}</p>
      </div>
    </div>
  );
}

export default App;
