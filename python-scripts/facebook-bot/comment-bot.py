import fbchat

# Define the session cookies as a dictionary
session_cookies = {
    "c_user":	"61558478504573",
    "datr":	"iPNkZp7hQLgsW0NFyhXqqlS5",
    "fr":	"0EREZ3Wm19oNW3lD3.AWVQUn7zaClrfcpIM-S6L0ryU2A.BmZPO-..AAA.0.0.BmZPO-.AWWwaYJ296M",
    "sb":	"iPNkZomrCx3I6tJX_B4iopPD",
    "xs":	"33:kCP2ZgTDGQQu1A:2:1717892031:-1:7470"
}

# Create a new client instance with the session cookies
client = fbchat.Client(None,None, max_tries=1,session_cookies=session_cookies)

# Define the post ID and comment
post_id = "25926605110287926"
comment = "Hello from Python!"

# Get the thread ID from the post ID
thread_id = client.get_thread_id_from_post_id(post_id)

# Comment on the post
client.send_message(comment, thread_id=thread_id, thread_type=fbchat.ThreadType.GROUP)

# Close the client
client.logout()
