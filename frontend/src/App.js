import React from 'react';
import GoogleOAuth from './GoogleLogin';
import api from './ApiService';
import axios from 'axios';
import { useGoogleLogin, GoogleOAuthProvider } from '@react-oauth/google';
function App() {
  const login = useGoogleLogin({
    onSuccess: codeResponse => {
    console.log(codeResponse)
    const res = axios.get('http://localhost:8000/auth', { params: { code: codeResponse.code } }).then((response) => console.log(response.data))
    },
    flow: 'auth-code',
  });
  



  return (
      <button onClick={login}>Sign in with Google</button>
  )

}

export default App;
