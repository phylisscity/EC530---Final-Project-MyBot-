// Import React library and other components needed
import React from 'react';
import ReactDOM from 'react-dom/client';
import App from './App.jsx';
import './index.css'; 

// ----------------------------------
// Render the App component into the 'root' div
// React.StrictMode helps catch common mistakes during development
// ----------------------------------

ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
  
);
