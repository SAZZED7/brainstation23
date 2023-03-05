
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Open the browser and go to the URL
driver = webdriver.Chrome()
driver.get("https://test.sharebus.co/")
time.sleep(2)
# Click on the "Sign in" button to go to the login page
driver.find_element_by_xpath("//button[@class='sb-btn-lg']").click()

time.sleep(2)

# Enter email and password to log in
driver.find_element_by_xpath("//input[@id='email']").send_keys("brainstation23@yopmail.com")
time.sleep(2)
password_input = driver.find_element_by_xpath("//input[@id='password']")
password_input.send_keys("Pass@1234")
password_input.send_keys(Keys.ENTER)
time.sleep(2)

# Select user as "Sharelead" from the menu options
user_menu = driver.find_element_by_xpath("//span[@class='p-dropdown-trigger-icon_pi_pi-chevron-down']")
user_menu.click()
sharelead_option = driver.find_element_by_xpath("//span[@normalize-space()='Sharelead']")
sharelead_option.click()
time.sleep(2)
# Click "Set Up a ShareBus" button
setup_button = driver.find_element_by_xpath('//a[@href="/sharelead/setup"]')
setup_button.click()
time.sleep(2)
# Insert required Trips details and click "Continue"
from_input = driver.find_element_by_name("from")
to_input = driver.find_element_by_name("to")
from_input.send_keys("Oslo, Norway")
to_input.send_keys("Kolbotn, Norway")
continue_button = driver.find_element_by_xpath("//button[@type='submit']")
continue_button.click()
time.sleep(4)
# On Membership page click "Yes" and select "NTNUI" club and click "Continue"
yes_button = driver.find_element_by_xpath('//input[@value="yes"]')
yes_button.click()
club_select = driver.find_element_by_xpath('//select[@name="club"]')
club_select.click()
club_option = driver.find_element_by_xpath('//option[@value="NTNUI"]')
club_option.click()
continue_button = driver.find_element_by_xpath('//button[@type="submit"]')
continue_button.click()
time.sleep(2)
# Need any tickets for himself? click on "No" button
no_button = driver.find_element_by_xpath('//input[@value="no"]')
no_button.click()
time.sleep(2)
# Activate ticket discounts? click "No" button
no_button = driver.find_element_by_xpath('//input[@value="no"]')
no_button.click()
time.sleep(2)
# Click on the "Create ShareBus" button
create_button = driver.find_element_by_xpath('//button[@type="submit"]')
create_button.click()
time.sleep(2)
# Click on the "Publish" button
driver.find_element_by_xpath('//button[@id="publish-btn"]').click()
time.sleep(2)
# Insert data on required fields
title_input = driver.find_element_by_name("title")
title_input.send_keys("Test Trip")
description_input = driver.find_element_by_name("description")
description_input.send_keys("This is a test trip created with Selenium WebDriver")
time.sleep(2)
# Click on the "Review and publish" button
review_button = driver.find_element_by_xpath('//button[@id="review-btn"]')
review_button.click()
time.sleep(2)
# Click on the "Publish" button
publish_button = driver.find_element_by_xpath('//button[@id="publish-btn"]')
publish_button.click()
time.sleep(2)
# Click on the "my busses" from navbar
my_busses_link = driver.find_element_by_xpath('//a[@href="/sharelead/my-busses"]')
my_busses_link.click()
time.sleep(2)
# Verify that the new Trip is displayed on the "My busses" page
trips_list = driver.find_element_by_xpath("//ul[@class='list-group']/li")
assert "Test Trip" in trips_list.text

# Close the browser
driver.quit()