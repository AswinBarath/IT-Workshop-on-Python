# Write a python program to invoke Chrome browser/Firefox/internet explorer and load the Website to automate,
# apply different WebDriver methods to get Title, get url, quit(), forward(), backward(), close the session and
# navigate to some other website.  Using Facebook , gmail

from selenium import webdriver
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(executable_path="C:\\Users\\Admin-pc\\Downloads\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/angularpractice/")

# driver.find_element_by_name("name").send_keys("Rahul")
driver.find_element_by_css_selector("input[name='name']").send_keys("Rahul")
driver.find_element_by_name("email").send_keys("Shetty")

driver.find_element_by_id("exampleCheck1").click()

# select class provide the methods to handle the options in dropdown
dropdown = Select(driver.find_element_by_id("exampleFormControlSelect1"))
dropdown.select_by_visible_text("Male")
dropdown.select_by_index(0)

driver.find_element_by_xpath("//input[@type='submit']").click()

message = driver.find_element_by_class_name("alert-success").text

assert "success" in message
# driver.close()
