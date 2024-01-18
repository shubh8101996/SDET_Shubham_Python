# Rename your script file to something other than jwt.py, e.g., my_jwt_script.py
import jwt
import datetime

# Create a payload with user information
payload = {
    'user_id': 154,
    'username': 'shubham shedge',
    'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=1)  # Token expiration time
}

# Create a secret key for signing the token
secret_key = 'your_secret_key'

# Encode the payload and create the token
token = jwt.encode(payload, secret_key, algorithm='HS256')

# Print the generated token
print(token)
