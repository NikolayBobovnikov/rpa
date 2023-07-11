from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random
import chromedriver_binary  # Adds chromedriver binary to path
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains


# start the browser
browser = webdriver.Chrome()
browser.maximize_window()


def slow_type(element, text):
    for char in text:
        ActionChains(browser).move_to_element(
            element).send_keys(char).perform()
        # Convert milliseconds to seconds
        wait_period = random.randint(50, 500) / 1000
        time.sleep(wait_period)


addresses = ["https://www.google.com", "https://www.wikipedia.org", "https://www.python.org",
             "https://1vtms.visualstudio.com/BATS/_versionControl?path=%24/BATS/bats",
             "https://trello.com/b/Ic1XMZx5/sport-new?filter=member:nikolay_bobovnikov"]

search_queries = ["webpack configuration in dotnet project",
                  "options for the typescript config in the dotnet project",
                  "DTO objects in C#",
                  "godbolt C# compiler",
                  "ASP net core controllers",
                  "ASP net core routing",
                  "ASP net core authentication",
                  "ASP net core authorization",
                  "ASP net core middleware"]

while True:
    try:
        # scenario 1: open tabs with predefined addresses
        for address in addresses:
            browser.execute_script(f"window.open('{address}');")
            wait_period = random.randint(10, 200)
            time.sleep(wait_period)

        # scenario 3: go to google.com, enter a search query, and submit
        for query in search_queries:
            browser.get("https://www.google.com")

            # Locate the search box element and send keys
            search_box = browser.find_element("name", "q")

            # Slowly type the search query
            slow_type(search_box, query)
            search_box.send_keys(Keys.RETURN)

            # Wait until the search results are loaded
            try:
                wait = WebDriverWait(browser, 10)
                search_results = wait.until(
                    EC.presence_of_element_located((By.ID, "search")))
            except Exception as e:
                print("An error occurred while waiting for search results:", str(e))

            # time.sleep(5)

            # Find the first link in the search results and click on it
            try:
                first_link = search_results.find_element(By.TAG_NAME, "a")
                first_link.click()
            except Exception as e:
                print("An error occurred while clicking the first link:", str(e))

            wait_period = random.randint(10, 200)
            time.sleep(wait_period)

        # close all tabs except the first one
        try:
            while len(browser.window_handles) > 1:
                browser.switch_to.window(browser.window_handles[-1])
                browser.close()
            browser.switch_to.window(browser.window_handles[0])
        except Exception as e:
            print("An error occurred while closing tabs:", str(e))

    except Exception as e:
        print("An error occurred:", str(e))
        browser.quit()
        continue

    # If the code reaches this point without any exceptions, exit the loop
    continue


# remember to quit the browser once finished to avoid resource leak
browser.quit()
