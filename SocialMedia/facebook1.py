from selenium import webdriver
from selenium.webdriver.common.by import By

# Configure the Chrome driver
driver = webdriver.Chrome()

# Open Facebook
driver.get("https://www.facebook.com")

# Find the username and password input fields by their "name" attributes
username_field = driver.find_element(By.NAME, "email")
password_field = driver.find_element(By.NAME, "pass")

# Enter your Facebook email/phone number and password
username_field.send_keys("your_email_or_phone")
password_field.send_keys("your_password")

# Submit the login form (you can use a different element if needed)
password_field.submit()

# Add some wait time if needed to ensure the login process is completed
# Example: time.sleep(5)

# After logging in, you can perform further actions, such as navigating to your profile or interacting with posts.

# Close the browser
# driver.quit()
