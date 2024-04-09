"""
Module: Fyers API Integration
Description: This script demonstrates the integration of Fyers API to active the fyer's app.
"""


# Import the required module from the fyers_apiv3 package
from fyers_apiv3 import fyersModel

# Replace these values with your actual API credentials
client_id = "##########-###"
secret_key = "##########"
redirect_uri = "bytequity.com"
response_type = "code"  
state = "sample_state"

# Create a session model with the provided credentials
session = fyersModel.SessionModel(
    client_id=client_id,
    secret_key=secret_key,
    redirect_uri=redirect_uri,
    response_type=response_type,
    grant_type = 'authorization_code'
)



response = session.generate_authcode()
print(response)
print("App will be active after provide the access click on link to provide")
