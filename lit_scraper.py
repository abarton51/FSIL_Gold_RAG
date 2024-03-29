from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import os
import time

#download directory
download_directory = "/Users/shivanshsharma/Documents/Scraped_pdfs"

chrome_options = Options()
# chrome_options.add_argument("--headless")  # Headless mode
chrome_options.add_experimental_option("prefs", {
    "download.default_directory": download_directory,
    "download.prompt_for_download": False,  
    "download.directory_upgrade": True,
    "plugins.always_open_pdf_externally": True  
})

#Path to ChromeDriver
chrome_driver_path = "/usr/local/bin/chromedriver"
service = Service(chrome_driver_path)

driver = webdriver.Chrome(service=service, options=chrome_options)

try:
    driver.get("https://www.sec.gov/litigation/litreleases")

    complaint_links = driver.find_elements(By.PARTIAL_LINK_TEXT, 'SEC Complaint')

    downloaded_files = []

    for link in complaint_links:
        complaint_url = link.get_attribute('href')
        
        if complaint_url.endswith('.pdf'):
            driver.get(complaint_url)
            file_name = complaint_url.split('/')[-1]
            downloaded_files.append(file_name)
            
        else:
            print(f"Skipped non-PDF link: {complaint_url}")

finally:
    driver.quit()

print(f"Downloaded {len(downloaded_files)} files: {', '.join(downloaded_files)}")

