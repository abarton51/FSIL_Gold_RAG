from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import os
import time

def wait_for_downloads(download_directory, timeout=300):
    start_time = time.time()
    while True:
        if all(not fname.endswith('.crdownload') for fname in os.listdir(download_directory)):
            break
        elif time.time() - start_time > timeout:
            print("Timed out waiting for downloads to finish.")
            break
        time.sleep(1)

download_directory = "/Users/shivanshsharma/Documents/Scraped_pdfs"

chrome_options = Options()
# chrome_options.add_argument("--headless")
chrome_options.add_experimental_option("prefs", {
    "download.default_directory": download_directory,
    "download.prompt_for_download": False,
    "download.directory_upgrade": True,
    "plugins.always_open_pdf_externally": True  
})

chrome_driver_path = "/usr/local/bin/chromedriver"
service = Service(chrome_driver_path)

downloaded_files = []

try:
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.get("https://www.sec.gov/litigation/litreleases")
    complaint_links = driver.find_elements(By.PARTIAL_LINK_TEXT, 'SEC Complaint')

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
    wait_for_downloads(download_directory)
    total_size = sum(os.path.getsize(os.path.join(download_directory, f)) for f in downloaded_files if os.path.exists(os.path.join(download_directory, f)))
    print(f"Total size of downloaded PDFs: {total_size} bytes")
    print(f"Downloaded {len(downloaded_files)} files: {', '.join(downloaded_files)}")
