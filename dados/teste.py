from instascrape import *
from selenium import webdriver


driver = webdriver.Chrome()
driver.get("https://www.google.com/")
driver.quit()

google_hashtag = Hashtag('https://www.instagram.com/explore/tags/meioambiente/')
headers = {
    "user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Mobile Safari/537.36 Edg/87.0.664.57",
    "cookie": "sessionid=PASTE_YOUR_SESSIONID_HERE;"
}
google_hashtag.scrape(headers=headers)
posts = google_hashtag.get_recent_posts(webdriver=webdriver, login_first=True)
