import React from 'react';
import GoogleOAuth from './GoogleLogin';
import api from './ApiService';
import axios from 'axios';
import { useGoogleLogin, GoogleOAuthProvider } from '@react-oauth/google';
function App() {

  const login = useGoogleLogin({
    onSuccess: codeResponse => console.log(codeResponse),
    flow: 'auth-code',
  });

  return (
      <button onClick={login}>Sign in with Google</button>
  )

}

export default App;
