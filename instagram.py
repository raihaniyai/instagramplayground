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
profile_pic_url_hd = data['graphql']['user']['profile_pic_url_hd']
external_url = data['graphql']['user']['external_url']

# printing biodata of user
print("Photo Profile\t: " + profile_pic_url_hd)
print("Username\t: " + username)
print("Full Name\t: " + full_name)
print("Biography\t: " + biography)
print("Website\t\t: " + external_url)

i = 0

# printing posts and total of like each post (9 last posts)
for post in data['graphql']['user']['edge_owner_to_timeline_media']['edges']:
    print("Post\t\t: " + post['node']['display_url'])
    print("Likes\t\t: " + str(post['node']['edge_liked_by']['count']))
    # print("Caption\t: " + post['node']['edge_media_to_caption']['edges'][0]['node']['text'])
    print("Comments\t: " + str(post['node']['edge_media_to_comment']['count']) + "\n\n")
    print("------------------------------")
