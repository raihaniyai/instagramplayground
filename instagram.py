# importing the requests library
import requests
import json

# input for username
username = input("Username: ")

# api-endpoint
URL = "https://instagram.com/"+username+"/?__a=1"

# sending get request and saving the response as response object
r = requests.get(url = URL)

# extracting data in json format
data = r.json()
# getting variable needed
username = data['graphql']['user']['username']
full_name = data['graphql']['user']['full_name']
biography = data['graphql']['user']['biography']


# printing the output
print("Username\t: " + username)
print("Full Name\t: " + full_name)
print("Biography\t: " + biography)
