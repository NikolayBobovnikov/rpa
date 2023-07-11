from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import chromedriver_binary  # Adds chromedriver binary to path

# start the browser
browser = webdriver.Chrome()

addresses = ["https://www.google.com", "https://www.wikipedia.org", "https://www.python.org",
             "https://1vtms.visualstudio.com/BATS/_versionControl?path=%24/BATS/bats",
             "https://trello.com/b/Ic1XMZx5/sport-new?filter=member:nikolay_bobovnikov"]
# add more addresses as needed

while True:
    # scenario 1: open tabs with predefined addresses
    for address in addresses:
        browser.execute_script(f"window.open('{address}');")
        time.sleep(60)  # wait for 60 seconds before opening next tab

    # scenario 3: go to google.com, enter a search query, and submit
    browser.get("https://www.google.com")
    search_box = browser.find_element("name", "q")
    # replace "Hello, world!" with your search query
    search_box.send_keys("Hello, world!" + Keys.RETURN)
    time.sleep(60)

    # close all tabs except the first one
    while len(browser.window_handles) > 1:
        browser.switch_to.window(browser.window_handles[-1])
        browser.close()
    browser.switch_to.window(browser.window_handles[0])

# remember to quit the browser once finished to avoid resource leak
browser.quit()
