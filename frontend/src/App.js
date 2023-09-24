import React from 'react';
import GoogleOAuth from './GoogleLogin';
import api from './ApiService';

function App() {
  const handleGoogleSuccess = (userProfile) => {
    console.log('Logged in with Google:', userProfile);
    // Make an API request to your FastAPI backend to save or verify the user's credentials.
    api.post('/user/login', userProfile).then((response) => {
      // Handle the response from the backend.
    });
  };

  const handleGoogleFailure = () => {
    console.log('Google login failed');
  };

  return (
    <div>
      <h1>React Frontend with Google OAuth and FastAPI Backend</h1>
      <GoogleOAuth onSuccess={handleGoogleSuccess} onFailure={handleGoogleFailure} />
    </div>
  );
}

export default App;

// import logo from './logo.svg';
// import './App.css';

// function App() {
//   return (
//     <div className="App">
//       <header className="App-header">
//         <img src={logo} className="App-logo" alt="logo" />
//         <p>
//           Edit <code>src/App.js</code> and save to reload.
//         </p>
//         <a
//           className="App-link"
//           href="https://reactjs.org"
//           target="_blank"
//           rel="noopener noreferrer"
//         >
//           Learn React
//         </a>
//       </header>
//     </div>
//   );
// }

// export default App;
