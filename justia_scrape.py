from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time

# Set up Selenium options
options = Options()
options.add_argument("--headless")  # Run in headless mode
options.add_argument("--disable-gpu")
options.add_argument("--window-size=1920x1080")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

# Automatically manage ChromeDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Define the base Justia URL
BASE_URL = "https://www.justia.com/lawyers/family-law/illinois/chicago"
current_page = 1

all_data = []

while True:
    url = f"{BASE_URL}?page={current_page}"
    driver.get(url)
    print(f"Scraping page {current_page}...")
    
    # Wait for the page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "lawyer-card")))
    
    # Find all lawyer cards
    lawyer_cards = driver.find_elements(By.CLASS_NAME, "lawyer-card")
    
    if not lawyer_cards:
        print("No more lawyer cards found. Exiting...")
        break  # Stop scraping if no lawyers are found
    
    for card in lawyer_cards:
        try:
            name_tag = card.find_element(By.CLASS_NAME, "lawyer-name").text.strip()
            profile_url_tag = card.find_elements(By.CLASS_NAME, "mainprofilelink")
            profile_url = profile_url_tag[0].get_attribute("href") if profile_url_tag else "N/A"
            img_tag = card.find_elements(By.CLASS_NAME, "-avatar")
            img_url = img_tag[0].get_attribute("src") if img_tag else "N/A"
            phone_tag = card.find_elements(By.CLASS_NAME, "-phone")
            phone = phone_tag[0].text.strip() if phone_tag else "N/A"
            tagline_tag = card.find_elements(By.CLASS_NAME, "lawyer-tagline")
            tagline = tagline_tag[0].text.strip() if tagline_tag else "N/A"
            description_tag = card.find_elements(By.CLASS_NAME, "lawyer-description")
            description = description_tag[0].text.strip() if description_tag else "N/A"
            website_tag = card.find_elements(By.XPATH, ".//a[contains(text(), 'Website')]")
            website = website_tag[0].get_attribute("href") if website_tag else "N/A"
            free_consultation = "Yes" if "Free Consultation" in card.text else "No"
            
            lawyer_info = {
                "Name": name_tag,
                "Profile URL": profile_url,
                "Image URL": img_url,
                "Phone": phone,
                "Free Consultation": free_consultation,
                "Tagline": tagline,
                "Description": description,
                "Website": website
            }
            all_data.append(lawyer_info)
            print(lawyer_info)  # Print scraped data
        except Exception as e:
            print(f"Error scraping lawyer: {e}")
            continue
    
    # Check if there is a next page
    try:
        next_page = driver.find_element(By.XPATH, "//div[@id='pagination']//span[@class='next']/a")
        if next_page:
            current_page += 1
        else:
            break
    except:
        break  # No next page found, exit loop
    
# Convert to DataFrame and save to CSV
df = pd.DataFrame(all_data)
df.to_csv("justia_lawyers_selenium.csv", index=False)
print("\nScraping complete. Data saved to justia_lawyers_selenium.csv")

# Close the Selenium browser
driver.quit()
