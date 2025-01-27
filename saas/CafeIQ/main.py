import requests
import bs4
import selenium
import pandas
print("Libraries installed successfully!")

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd

# Initialize the WebDriver
driver = webdriver.Chrome(executable_path="path_to_chromedriver")

def scrape_google_maps(google_maps_urls):
    data = []
    for url in google_maps_urls:
        driver.get(url)
        time.sleep(5)  # Allow time for the page to load

        # Scrape restaurant details
        try:
            name = driver.find_element(By.CLASS_NAME, "DUwDvf").text
        except:
            name = "N/A"

        try:
            address = driver.find_element(By.CLASS_NAME, "Io6YTe").text
        except:
            address = "N/A"

        # Scroll to load reviews
        for _ in range(5):
            driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.END)
            time.sleep(2)

        # Scrape reviews
        reviews = driver.find_elements(By.CLASS_NAME, "wiI7pd")
        review_texts = [review.text for review in reviews]

        # Save data for each restaurant
        data.append({
            "Name": name,
            "Address": address,
            "Reviews": review_texts
        })

    # Save to a CSV file
    df = pd.DataFrame(data)
    df.to_csv("google_maps_data.csv", index=False)
    print("Data saved to google_maps_data.csv")

# List of Google Maps URLs to scrape
google_maps_urls = [
    "https://maps.app.goo.gl/eqJ8tiLDuk3rnGN19",
    "https://maps.app.goo.gl/KNDmg1JABKZ3gnkw9",
    "https://maps.app.goo.gl/o4xYQrJJg2LciJuH6"
]

scrape_google_maps(google_maps_urls)

# Close the browser
driver.quit()
