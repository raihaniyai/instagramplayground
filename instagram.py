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
followings = str(data['graphql']['user']['edge_follow']['count'])
followers = str(data['graphql']['user']['edge_followed_by']['count'])
user_id = data['graphql']['user']['id']

# printing biodata of user
print("\n===== BIODATA =====\n")
print("Photo Profile\t: " + profile_pic_url_hd)
print("Username\t: " + username)
print("Full Name\t: " + full_name)
print("Biography\t: " + biography)
print("Website\t\t: " + external_url)
print("Followers\t: " + followers)
print("Followings\t: " + followings)
print("\n===== POSTS =====\n")

# getting posts of instagram user according to username
POSTS = "https://www.instagram.com/graphql/query/?query_hash=f2405b236d85e8296cf30347c9f08c2a&variables={%22id%22:%22" + user_id + "%22,%22first%22:50}"
req = requests.get(url = POSTS)
data = req.json()

i = 0 # only to make sure the num of posts is right
most_like = 0
most_comment = 0

# printing posts and total of like each post (9 last posts)
while True:
    for post in data['data']['user']['edge_owner_to_timeline_media']['edges']:
        print("Post\t\t: " + post['node']['display_url'])
        print("Likes\t\t: " + str(post['node']['edge_media_preview_like']['count']))
        # print("Caption\t: " + post['node']['edge_media_to_caption']['edges'][0]['node']['text'])
        print("Comments\t: " + str(post['node']['edge_media_to_comment']['count']) + "\n")
        print("------------------------------\n")
        i += 1

        if most_like < post['node']['edge_media_preview_like']['count']:
            most_like = post['node']['edge_media_preview_like']['count']
            liked = "https://instagram.com/p/" + post['node']['shortcode']
            pass
        if most_comment < post['node']['edge_media_to_comment']['count']:
            most_comment = post['node']['edge_media_to_comment']['count']
            commented = "https://instagram.com/p/" + post['node']['shortcode']
            pass
        # end for

    if data['data']['user']['edge_owner_to_timeline_media']['page_info']['has_next_page'] == False:
        break
    else:
        end_cursor = data['data']['user']['edge_owner_to_timeline_media']['page_info']['end_cursor']
        POSTS = "https://www.instagram.com/graphql/query/?query_hash=f2405b236d85e8296cf30347c9f08c2a&variables={%22id%22:%22" + user_id + "%22,%22first%22:50,%22after%22:%22" + end_cursor + "%22}"
        req = requests.get(url = POSTS)
        data = req.json()
    # end while

if i > 0:
    print("Total Photos\t: " + str(i))
    print("The Most Liked Post\t:" + liked)
    print("Total of Likes\t\t: " + str(most_like) + "\n")
    print("The Most Commented Post\t:" + commented)
    print("Total of Comments\t\t: " + str(most_comment) + "\n")
else:
    print(username + " hasn't upload a photo/video yet or the account is locked")


# getting stories
stories_url = 'https://www.instagram.com/graphql/query/?query_hash=45246d3fe16ccc6577e0bd297a5db1ab&variables={"reel_ids":["' + user_id + '"],"tag_names":[],"location_ids":[],"highlight_reel_ids":[],"precomposed_overlay":false}'
r = requests.get(url = stories_url)
data = r.json()

result = body['data']['reels_media'][0]

if len(result) > 0:
    print("Total Story\t: " + str(len(result)))
    print("Result\t\t: " + str(result) + "\n")