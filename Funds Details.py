

# Import the required module from the fyers_apiv3 package
from fyers_apiv3 import fyersModel

# Replace these values with your actual API credentials

client_id = "#############"  # Your Fyers API client ID
secret_key = "##########"     # Your Fyers API secret key
redirect_uri = "bytequity.com"   # The redirect URI configured in your Fyers API dashboard
response_type = "code"        # The response type for authorization code flow
state = "sample_state"      # A unique identifier for maintaining state during authorization process

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
print("click on link to get the access token")
session.set_token(input('Enter auth code here'))

# Generate the access token using the authorization code
response = session.generate_token()
# Print the response, which should contain the access token and other details
print("Access token is ")
print(response['access_token'])



fyers = fyersModel.FyersModel(client_id=client_id, is_async=False, token=response['access_token'])
print("** USER's FUNDS DETAILS ARE **")
print(fyers.funds())
