# Instagram Playground

Instagram Playground is just a random repository I built to download photo profile, photos, and even stories from specific user(s) on Instagram.
If you ever think about view or even download your friend stories, this repository might helps you.

### Prerequisites

What things you need to run the program
```
python
```
yep, that's it.

### Input

You need to input `username` of your target, and your `instagram cookie`.

example of username: `raihaniyai`

example of instagram cookie: 
```
ig_did=AA00AA00-AA00-1234-1234-B989AC099579; mid=Xy_VjwAEAAFBq7qXyYHP4nR-9-w6; ig_nrcb=1; shbid=1234; ds_user_id=1234567890; sessionid=1234567890%3ARN6rtXBPWkt3Xq%3A15; csrftoken=eBeC7jwaFRxPabgdWyvpRwK6152NEwhQ; rur=PRN; shbts=1606988700.9176435; urlgen="{\"123.123.123.12\": 1234\123 \"123.123.123.123\": 12345\123 \"123.123.123.12\": 123}:1kklEJ:C-8jhVYzCcHfBlJlxTWTBU6fuHg"
```

Here is how you get the cookie:
1. login to your instagram account from your favorite browser
2. go to inspect element and go to tab 'Network'
3. go to the network named `reels_tray`
4. once you find the network, look for request header, and copy the `cookie` from it

enjoy!
