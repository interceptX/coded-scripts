from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import time

# Set up Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")
# Create a browser object

service = Service()
browser = webdriver.Chrome(service=service, options=chrome_options)

# Define the post URL
#postURL = "https://www.facebook.com/story.php?story_fbid=183397699825094&id=100044645959888"
postURL = "https://www.facebook.com/groups/linux.fans.group/posts/25926605110287926"

# Add the session cookie
browser.get("https://www.facebook.com")
browser.add_cookie({"name": "sb", "value": "iPNkZomrCx3I6tJX_B4iopPD"})
browser.add_cookie({"name": "datr", "value": "iPNkZp7hQLgsW0NFyhXqqlS5"})
browser.add_cookie({"name": "fr", "value": "0EREZ3Wm19oNW3lD3.AWVQUn7zaClrfcpIM-S6L0ryU2A.BmZPO-..AAA.0.0.BmZPO-.AWWwaYJ296M"})
browser.add_cookie({"name": "c_user", "value": "61558478504573"})
browser.add_cookie({"name": "xs", "value": "33:kCP2ZgTDGQQu1A:2:1717892031:-1:7470"})

# Refresh the page to apply the session cookie
browser.refresh()

# Open the post URL
browser.get(postURL)

# Wait for the page to load
time.sleep(5)

# Find the comment box
commentBox = browser.find_element_by_xpath("//textarea[@name='comment_text']")

# Enter the comment
commentBox.send_keys("Status Code:[200] Hello from Python!")

# Click the Comment button
browser.find_element_by_xpath("//button[@data-testid='react-composer-post-button']").click()

# Close the browser
browser.quit()
