from google.oauth2 import id_token
from google.auth.transport import requests as google_requests
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from dj_rest_auth.registration.views import SocialLoginView
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
import requests
from rest_framework.authtoken.models import Token
from .models import Customuser


class GoogleAuthAPIView(APIView):
    def post(self, request):
        auth_code = request.data.get('auth_code')
        
        if not auth_code:
            return Response({"error": "Authorization code is required"}, status=status.HTTP_400_BAD_REQUEST)
        
        token_url = 'https://oauth2.googleapis.com/token'
        token_data = {
            'code': auth_code,
            'client_id': "1003444393201-ipknt1l4g7k087701jvlh2fvoct8h3d7.apps.googleusercontent.com",
            'client_secret': "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",
            'redirect_uri': 'http://localhost:3000',
            'grant_type': 'authorization_code',
        }
        
        token_response = requests.post(token_url, data=token_data)
        
        if token_response.status_code != 200:
            print('Google API error:', token_response.text)
            return Response({"error": token_response.json().get('error_description', 'Failed to obtain access token')}, status=status.HTTP_400_BAD_REQUEST)
        
        token_json = token_response.json()
        access_token = token_json.get('access_token')
        
        if not access_token:
            return Response({"error": "Access token not found in response"}, status=status.HTTP_400_BAD_REQUEST)
        
        user_info_url = 'https://www.googleapis.com/oauth2/v1/userinfo'
        user_info_params = {
            'access_token': access_token,
            'alt': 'json'
        }
        user_info_response = requests.get(user_info_url, params=user_info_params)
        
        if user_info_response.status_code != 200:
            return Response({"error": "Failed to fetch user info"}, status=status.HTTP_400_BAD_REQUEST)
        
        user_info = user_info_response.json()

        return Response({
            "access_token": access_token,
            "user_info": user_info
        }, status=status.HTTP_200_OK)
    

# frontend


# import React, { useEffect } from 'react';
# import axios from 'axios';
# import { useNavigate } from 'react-router-dom';

# const GoogleLogin = () => {

#   const handleLogin = () => {
#     // Define the Google OAuth endpoint URL
#     const googleAuthURL = 'https://accounts.google.com/o/oauth2/v2/auth';
#     const clientId = '1003444393201-ipknt1l4g7k087701jvlh2fvoct8h3d7.apps.googleusercontent.com';
#     const redirectUri = 'http://localhost:3000'; // Update to your redirect URI
#     const responseType = 'code';
#     const scope = 'profile email';
#     console.log(`🚀  handleLogin  scope:`, scope)

#     // Redirect the user to Google's OAuth2 authorization endpoint
#     window.location.href = `${googleAuthURL}?client_id=${clientId}&redirect_uri=${redirectUri}&response_type=${responseType}&scope=${scope}`;
#   };

#   return (
#     <button onClick={handleLogin}>Login with Google</button>
#   );
# };

# export default GoogleLogin;




# import React, { useEffect } from 'react';
# import axios from 'axios';
# import { useNavigate } from 'react-router-dom';
# const Home = () => {
#     const navigate = useNavigate();

#     useEffect(() => {
#         // Extract the authorization code from the URL
#         const queryParams = new URLSearchParams(window.location.search);
#         const authCode = queryParams.get('code');
#         console.log(`🚀  useEffect  authCode:`, authCode)
    
#         if (authCode) {
#           axios.post('http://localhost:8000/api/google/',{ auth_code: authCode },{
#               headers: {
#                 'Content-Type': 'application/json',
#               }
#             }
#           )
#             .then(response => {
#               // Handle successful response
#               console.log('Login successful:', response.data);
#               // Store the token in local storage or state management
#               localStorage.setItem('authToken', response.data.token);
#               // Redirect to a protected route or homepage
#               navigate('/');
#             })
#             .catch(error => {
#               // Handle errors
#               console.error('Login failed:');
#             });
#         } else {
#           console.error('Authorization code not found in the URL.');
#         }
#       }, []);

#   return (
#     <div>Home</div>
#   )
# }

# export default Home;

