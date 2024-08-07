from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time

# Configure Selenium WebDriver
options = Options()
options.add_argument("--start-maximized")  # Open browser in maximized mode
options.add_argument("--disable-infobars")  # Disable infobars
options.add_argument("--disable-extensions")  # Disable extensions
options.add_argument("--disable-gpu")  # Applicable to windows os only
options.add_argument("--no-sandbox")  # Bypass OS security model
options.add_argument("--disable-dev-shm-usage")  # Overcome limited resource problems

# Provide the path to your WebDriver executable
driver_path = 'path_to_your_chromedriver'
driver = webdriver.Chrome(service=Service(driver_path), options=options)

# Open LinkedIn job page
job_url = 'https://www.linkedin.com/jobs/search/?currentJobId=3992464539'
driver.get(job_url)

# Wait for the page to load
time.sleep(5)  # Adjust sleep time as needed

# If login is required, automate the login process (example for illustration only)
username = 'your_linkedin_username'
password = 'your_linkedin_password'

# Locate and interact with login fields if necessary
try:
    username_field = driver.find_element(By.ID, 'username')
    password_field = driver.find_element(By.ID, 'password')
    login_button = driver.find_element(By.XPATH, '//*[@type="submit"]')

    username_field.send_keys(username)
    password_field.send_keys(password)
    login_button.click()

    # Wait for login to complete
    time.sleep(5)
except Exception as e:
    print("Login not required or failed:", e)

# Parse job details using BeautifulSoup
soup = BeautifulSoup(driver.page_source, 'html.parser')

# Example of extracting job title, company, location, etc.
try:
    job_title = soup.find('h1', {'class': 'top-card-layout__title'}).text.strip()
    company_name = soup.find('a', {'class': 'topcard__org-name-link'}).text.strip()
    location = soup.find('span', {'class': 'topcard__flavor topcard__flavor--bullet'}).text.strip()
    job_description = soup.find('div', {'class': 'description__text'}).text.strip()

    print(f"Job Title: {job_title}")
    print(f"Company Name: {company_name}")
    print(f"Location: {location}")
    print(f"Job Description: {job_description}")
except Exception as e:
    print("Failed to extract job details:", e)

# Close the driver
driver.quit()
