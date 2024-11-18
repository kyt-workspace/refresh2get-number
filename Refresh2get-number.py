from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
from datetime import datetime

# Set the URL
url = "https://buy.gomo.sg/select-number/?promocode=5GMOVALUE1111&_gl=1*1wvkkws*_gcl_aw*R0NMLjE3Mjc2MzE3OTEuQ2p3S0NBanc5ZU8zQmhCTkVpd0FvYzAtalZLRklrSVZrNFVhb2VXT25TM0xQb1I3bXlnQjRwTXhZWGp2bURrd2VhVGYtdUljaHZzbUxCb0MxZHdRQXZEX0J3RQ..*_gcl_dc*R0NMLjE3Mjc2MzE3OTEuQ2p3S0NBanc5ZU8zQmhCTkVpd0FvYzAtalZLRklrSVZrNFVhb2VXT25TM0xQb1I3bXlnQjRwTXhZWGp2bURrd2VhVGYtdUljaHZzbUxCb0MxZHdRQXZEX0J3RQ..*_gcl_au*MjEzMzgyNDk4MC4xNzI2ODk2NTQ4*_ga*MTU4Mjg3ODcxNi4xNzI2ODk2NTQ4*_ga_PVSCWPTQ2V*MTczMTcyODg2MS45LjEuMTczMTcyODg4NC4zNy4wLjA."

# Strings to search for
search_strings = ["0512"]

# Disable logging using Chrome options
chrome_options = Options()
chrome_options.add_argument("--log-level=3")  # Suppresses INFO, WARNING, and ERROR messages
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])  # Suppress logging output from ChromeDriver

# Initialize the WebDriver with the Chrome options
driver = webdriver.Chrome(options=chrome_options)

# Open the webpage
driver.get(url)

count = 0

try:
    while True:
        # Get current time for logging
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # Attempt to click the "Show more" link if it's present
        try:
            show_more_link = driver.find_element(By.CSS_SELECTOR, "a.Anchor__SCAnchor-sc-139azf2-0.bOOTXZ")
            show_more_link.click()
            time.sleep(1)  # Wait briefly to allow more items to load
        except Exception:
            print(f"No 'Show more' link found at {current_time}")
        
        # Find all elements that may contain the text
        text_elements = driver.find_elements(By.CSS_SELECTOR, '.TextItem__SCContainer-pcg7e-0.jyPbvj')

        # Check if element text ends with any of the search strings
        for element in text_elements:
            if any(element.text.endswith(f" {search_string}") for search_string in search_strings):
                print(f"Found: '{element.text}' ending with one of {search_strings} at {current_time}")
                time.sleep(9999)  # Pause the program for a long interval or end the script
                driver.refresh()
        else:
            # Refresh the webpage if search strings were not found
            driver.refresh()
            count += 1
            print(f"[{count}] Page refreshed at {current_time}")
        
        # Sleep for a short interval before refreshing (e.g., 5 seconds)
        time.sleep(1)
        
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    driver.quit()  # Ensure the browser closes when done
