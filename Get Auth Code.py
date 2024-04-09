"""
Module: Fyers API Integration
Description: This script demonstrates the integration of Fyers API to authenticate and generate an authorization code for accessing Fyers API.
"""

# Import the required module from the fyers_apiv3 package
from fyers_apiv3 import fyersModel

# Replace these values with your actual API credentials
client_id = "##########-###"  # Your Fyers API client ID
secret_key = "##########"     # Your Fyers API secret key
redirect_uri = "bytequity.com"   # The redirect URI configured in your Fyers API dashboard
response_type = "code"        # The response type for authorization code flow
state = "sample_state"       # A unique identifier for maintaining state during authorization process

# Create a session model with the provided credentials
session = fyersModel.SessionModel(
    client_id=client_id,
    secret_key=secret_key,
    redirect_uri=redirect_uri,
    response_type=response_type,
    grant_type='authorization_code'
)

# Generate an authorization code
response = session.generate_authcode()

# Print the authorization code and instruction for further steps
print(response)
print("Click on the link to get the access token.")
