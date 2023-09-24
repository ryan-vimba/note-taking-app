import React from 'react';
import { GoogleLogin } from 'react-google-login';

const GoogleOAuth = ({ onSuccess, onFailure }) => {
  const responseGoogle = (response) => {
    if (response && response.profileObj) {
      onSuccess(response.profileObj);
    } else {
      console.log(response)
      onFailure();
    }
  };

  return (
    <div>
      <GoogleLogin
        clientId="669500394322-bmrc3fop25pm2mtc6er23f5h7hs946kg.apps.googleusercontent.com"
        buttonText="Login with Google"
        onSuccess={responseGoogle}
        onFailure={responseGoogle}
        cookiePolicy={'single_host_origin'}
      />
    </div>
  );
};

export default GoogleOAuth;

