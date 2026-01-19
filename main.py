# from selenium import webdriver

# driver = webdriver.Chrome() #it install the chrome driver automatically to automate the chrome browser by selenium manager to avoid external dependency of ChromeDriverManager and to avoid service parameter in the code.
# driver.get("https://www.google.com")
# print(driver.title)
# driver.quit()

# ***********************************Naviagtion and locators*******************
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.options import Options
# options = Options()
# options.add_experimental_option("detach", True) #detach mean separate will be opened diffrent from original chrome browser.
# driver = webdriver.Chrome(options=options) #to update deafult behaviour of chrome settings to keep the browser open after the script is executed
# driver.get("https://rahulshettyacademy.com/AutomationPractice/")
# driver.find_element(By.ID, "checkBoxOption1").click()
# driver.find_element(By.NAME, "checkBoxOption2").click()
# driver.find_element(By.CLASS_NAME, "radioButton").click() #it is used to click the radio button but top botom approahc results only first elkelement to dind it beacuse of clklaases are not unique
# driver.find_element(By.LINK_TEXT, "Free Access to InterviewQues/ResumeAssistance/Material").click() #it is used to click the link text
# driver.find_element(By.PARTIAL_LINK_TEXT, "InterviewQues/ResumeAssistance").click() #it is used to click the partial link text when we think link text can change in future.
# driver.quit() #it is used to close the browser


# ****************************** CSS SELECTOR ***********************
#when we dont find unique id, name, class name, link text, partial link text, tag name, we use css selector.
#we use double quotes for id, name, class name, link text, partial link text, tag name and single quotes for xpath.
#we use square brackets for attributes.

# from selenium import webdriver #it is used to open the browser
# from selenium.webdriver.common.by import By #it is used to find the elements on the page
# from selenium.webdriver.chrome.options import Options #it is used to set the options for the browser
# options = Options()
# options.add_experimental_option("detach", True) #it is used to keep the browser open after the script is executed
# driver = webdriver.Chrome(options=options) #Instantiates a Chrome WebDriver with the configured options
# driver.get("https://rahulshettyacademy.com/AutomationPractice/") #it is used to open the url
# driver.find_element(By.CSS_SELECTOR, "[value='radio2']").click() #it is used to click the radio button

#**************************XPATH**************************
#we use double quotes for id, name, class name, link text, partial link text, tag name and single quotes for xpath and we use square brackets for attributes @ show that it is an attribute.

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.options import Options
# options = Options()
# options.add_experimental_option("detach", True)
# driver = webdriver.Chrome(options=options)
# driver.get("https://rahulshettyacademy.com/AutomationPractice/")
# # driver.find_element(By.XPATH, "//input[@value='radio2']").click()
# # driver.find_element(By.XPATH, "//legend[text()='Suggession Class Example']").click()
# # driver.find_element(By.XPATH, "//input[starts-with(@value, 'rad')]").click() #we need it when we have to click multiple elements 1 by 1 but we don't know the exact value of the element.
# # driver.find_element(By.XPATH, "//input[contains(@value, 'adio')]").click() #contains used when we have to find the element by partial text.
# # driver.find_element(By.XPATH, "//legend[contains(text(), 'Class Example')]").click() #find the element by partial text. #contains used when we don't know the exact text of the element and it is dynamically generated.
# # # driver.find_element(By.XPATH, "//div[@id='radio-btn-example']/fieldset/label[@for='radio3']/input").click() #find the element by parent id and child for attribute to reach our goal of unique element.
# # driver.find_element(By.XPATH, "/html//body//select[@id='dropdown-class-example']//option[@value='option2']").click() #find the element by absolute xpath single slash means absolute to the root element and we can use // slashes for staring matching at any element to the grand child instead of direct childs.
# # driver.find_element(By.XPATH, "(//div[@id='radio-btn-example']//input[starts-with(@value, 'radio')])[last()]").click() #find the element by last child of the parent id radio-btn-example using starts-with to match radio1, radio2, radio3.
# driver.find_element(By.XPATH, "(//input[@value='radio3']/ancestor::div[@id]//input)[2]").click() #ancestor used for finding from child to parent to grand parent to find the element.

# *********SendKeys, Click, Get and Clear Input Text, Alert Handling, Wait Time,**************

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import time
# options = Options()
# options.add_experimental_option("detach", True)
# driver = webdriver.Chrome(options=options)
# driver.get("https://rahulshettyacademy.com/AutomationPractice/")
# # Store input element in variable to avoid finding it multiple times
# name_input = driver.find_element(By.XPATH, "//input[@id='name']")
# name_input.send_keys("Ch")
# name_input.clear()
# name_input.send_keys("Zain")
# alert_example = driver.find_element(By.XPATH, "//legend[text()='Switch To Alert Example']")
# print(alert_example.text) #.text is used to get the text of the element.
# driver.find_element(By.ID, "alertbtn").click()
# # Wait for alert to appear (wait up to 3 seconds)
# wait = WebDriverWait(driver, 3)
# alert = wait.until(EC.alert_is_present()) #Ec means expected conditions to be met.
# # Wait 7 seconds after alert appears, then accept it
# time.sleep(7)
# alert.accept()

# **************Select multiple checkboxes ,select using conditions,get attribute********

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.options import Options
# options = Options()
# options.add_experimental_option("detach", True)
# driver = webdriver.Chrome(options=options)
# driver.get("https://rahulshettyacademy.com/AutomationPractice/")
# # for i in range(1, 4):
# #     driver.find_element(By.XPATH, f"//input[@value='option{i}']").click()

# # checkboxes = driver.find_elements(By.XPATH, "(//input[starts-with(@name, 'checkBoxOption')])[position()<3]") #use elements when we have to find multiple elements. position()<3 means first 2 elements.
# # print(len(checkboxes))
# # for checkbox in checkboxes:
# #     print(checkbox.get_attribute("value")) #get_attribute used to get value of the attribute.
# #     checkbox.click()

# # if we wanna not to check all checkboxes then we can use the following code
# checkboxes = driver.find_elements(By.XPATH, "//input[starts-with(@name, 'checkBoxOption')]") 
# print(len(checkboxes))
# for checkbox in checkboxes:
#     if checkboxes.index(checkbox)+1 != 2: #+1 is used to start checking  using 1 instead of 0 to match the index of the checkbox.
#         checkbox.click()
 
# **************Handle static dropdowns*****************

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.support.select import Select
# import time

# options = Options()
# options.add_experimental_option("detach", True)
# driver = webdriver.Chrome(options=options)
# driver.maximize_window()
# driver.get("https://rahulshettyacademy.com/AutomationPractice/")
# static_dropdown = driver.find_element(By.ID, "dropdown-class-example")
# select = Select(static_dropdown)
# select.select_by_index(1)
# time.sleep(3)
# select.select_by_visible_text("Option2")
# time.sleep(3)
# select.select_by_value("option3")
# time.sleep(3)

# **************Handle dynamic dropdowns flipkart*****************
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import time
# from time import sleep
# options = Options()
# options.add_experimental_option("detach", True)
# driver = webdriver.Chrome(options=options)
# driver.maximize_window()
# driver.get("https://www.flipkart.com/")
# search_box = driver.find_element(By.XPATH, "//input[@type='text']")
# search_box.send_keys("one plus headphones")
# # Wait for the dropdown suggestion to appear (wait up to 10 seconds)
# wait = WebDriverWait(driver, 10)
# # first_option = wait.until(EC.presence_of_element_located((By.XPATH, "(//form[contains(@class,'header-form-search')]//a)[1]"))) #presence_of_element_located is used to wait for the element to be located in the DOM.
# # print(first_option.get_attribute("href"))
# # print(first_option.text)
# # sleep(3)
# # first_option.click()

# Wait for the dropdown suggestions to appear before finding them basically dynmaic searching
# wait.until(EC.presence_of_element_located((By.XPATH, "(//form[contains(@class,'header-form-search')]//a)[1]")))
# # Find all dropdown options
# dynamic_search_option = driver.find_elements(By.XPATH, "(//form[contains(@class,'header-form-search')]//a)")
# print(f"Number of options found: {len(dynamic_search_option)}")
# for index, option in enumerate(dynamic_search_option):
#     print(f"Index: {index}, Option: {option.text}")
#     if "headphones" in option.text.lower():
#         option.click()
#         break
# sleep(3)

# ****************************Login Automation***********************
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.support.select import Select
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import time

# options = Options()
# options.add_experimental_option("detach", True)
# driver = webdriver.Chrome(options=options)
# driver.maximize_window()
# driver.get("https://rankyoupportal.com/")
# # Wait for element to be clickable (handles overlays and ensures element is ready)
# wait = WebDriverWait(driver, 10)
# login_link = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='d-flex justify-content-center gap-3 flex-wrap mb-4']/a[@href='/login/']")))
# # Scroll element into view before clicking
# driver.execute_script("arguments[0].scrollIntoView(true);", login_link)
# time.sleep(1)  # Small wait after scrolling
# # Try regular click, if it fails use JavaScript click
# try:
#     login_link.click()
# except:
#     driver.execute_script("arguments[0].click();", login_link)

# # Wait for login form to load and fill in credentials
# time.sleep(2)  # Wait for page navigation
# username_field = wait.until(EC.presence_of_element_located((By.ID, "id_username")))
# password_field = driver.find_element(By.ID, "id_password")

# # Enter login credentials
# username_field.send_keys("") #enter your username here
# password_field.send_keys("") #enter your password here

# # Click the submit button
# submit_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']")))
# submit_button.click()


#***********************implicit wait(it check just element present in dom not check display status of the element*************
# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.options import Options

# options = Options()
# options.add_experimental_option("detach", True)
# driver = webdriver.Chrome(options=options)
# driver.maximize_window()
# driver.implicitly_wait(3.5) #it is used to wait for the element to be loaded for 5 seconds if element found in 2 seconds it exetcute and dont wait thats the main benefit of implicit wait and good pratice instead of time.sleep() but drawback is it will wait for the element to be loaded for 5 seconds and execute rest of the code without condition checking etc so we need to use explicit wait in that case.
# driver.get("https://www.flipkart.com/")
# # time.sleep(2)
# # Try to close popup if it exists (popup may not always appear)
# try:
#     driver.find_element(By.XPATH, "//button[text()='x']").click()
# except:
#     try:
#         driver.find_element(By.XPATH, "//button[text()='✕']").click()
#     except:
#         print("No popup found, continuing...")
# search_box = driver.find_element(By.XPATH, "//input[@type='text']")
# search_box.send_keys("one plus")
# # time.sleep(2)
# dropdown_options = driver.find_elements(By.XPATH, "(//form[contains(@class,'header-form-search')]//a)")
# for index, option in enumerate(dropdown_options):
#     print(option.get_attribute("href"))
#     print(option.text)
#     if "headphones" in option.text.lower():
#         option.click()
#         break

#***********************Explicit wait*************************
# we can also use until not to wait for the element to be not present in the dom.

# import time
# from selenium import webdriver
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.by import By
# options = Options()
# options.add_experimental_option("detach", True)
# driver = webdriver.Chrome(options=options)
# driver.maximize_window()
# driver.get("https://www.flipkart.com/") 
# #3rd parameter poll frequency is 0.5 seconds by default so it will recheck after 0.5 seconds if element is not found it will wait for 10 seconds and if element is found it will click on it but if still not found it will raise TimeoutException.
# # Try to close popup if it exists (popup may not always appear)
# try:
#     WebDriverWait(driver, 2, 0.2).until(EC.visibility_of_element_located(("xpath", "//button[text()='x']")))
#     login_popup_close_button = driver.find_element("xpath", "//button[text()='x']")
#     login_popup_close_button.click()
# except:
#     print("No popup found, continuing...")
# search_box = driver.find_element("xpath", "//input[@type='text']")
# search_box.send_keys("one plus")
# WebDriverWait(driver, 2, 0.2).until(EC.presence_of_all_elements_located(("xpath", "(//form[contains(@class,'header-form-search')]//a)")))
# dropdown_options = driver.find_elements("xpath", "(//form[contains(@class,'header-form-search')]//a)")
# for index, option in enumerate(dropdown_options):
#     print(f"link present in {index+1} option: {option.get_attribute('href')}")
#     print(f"text present in {index+1} option: {option.text}")
#     if "bullets" in option.text:
#         option.click()
#         break
# else:
#     print("options not found!")


# ***********************Common Selenium Exceptions & Solutions*************************

# 1. StaleElementReferenceException
# EXPLANATION: Occurs when you store an element reference, but the DOM changes (refresh, navigation, JS updates),
# making the stored reference invalid. The element exists, but your reference to it is "stale".
# SOLUTION: Always re-find elements after any DOM changes like page refresh or navigation.
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.options import Options
# from selenium.common.exceptions import StaleElementReferenceException
# 
# options = Options()
# options.add_experimental_option("detach", True)
# driver = webdriver.Chrome(options=options)
# driver.get("https://example.com")
# 
# # ❌ WRONG: Element reference becomes stale after DOM changes
# # search_box = driver.find_element(By.ID, "search")
# # driver.refresh()  # Page refreshes - DOM changes
# # search_box.send_keys("test")  # ❌ StaleElementReferenceException
# 
# # ✅ CORRECT: Re-find element after DOM changes
# search_box = driver.find_element(By.ID, "search")
# driver.refresh()
# search_box = driver.find_element(By.ID, "search")  # Re-find fresh reference
# search_box.send_keys("test")  # ✅ Works correctly


# 2. NoSuchElementException
# EXPLANATION: Raised when Selenium cannot find an element on the page. Common causes: element not loaded yet,
# wrong locator, element in iframe, or element doesn't exist. Most common timing issue - element appears after script runs.
# SOLUTION: Use explicit waits (WebDriverWait) to wait for element to appear, or fix the locator if element doesn't exist.
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.common.exceptions import NoSuchElementException
# 
# options = Options()
# options.add_experimental_option("detach", True)
# driver = webdriver.Chrome(options=options)
# driver.get("https://example.com")
# 
# # ❌ WRONG: Element might not be loaded yet
# # driver.find_element(By.ID, "non-existent-id").click()  # ❌ NoSuchElementException
# 
# # ✅ CORRECT: Use explicit wait to wait for element
# wait = WebDriverWait(driver, 10)
# try:
#     element = wait.until(EC.presence_of_element_located((By.ID, "my-id")))  # Wait for element
#     element.click()  # ✅ Element found and clickable
# except NoSuchElementException:
#     print("Element not found even after waiting")


# 3. ElementClickInterceptedException
# EXPLANATION: Element exists and is found, but another element (overlay, modal, banner) is covering it, making it unclickable.
# The click is "intercepted" by the overlapping element. Common with popups, cookie banners, or loading spinners.
# SOLUTION: Close overlay first, scroll element into view, use element_to_be_clickable wait, or use JavaScript click.
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.common.exceptions import ElementClickInterceptedException
# 
# options = Options()
# options.add_experimental_option("detach", True)
# driver = webdriver.Chrome(options=options)
# driver.get("https://example.com")
# wait = WebDriverWait(driver, 10)
# 
# # ❌ WRONG: Element exists but is covered by overlay/modal
# # login_button = driver.find_element(By.ID, "login-btn")
# # login_button.click()  # ❌ ElementClickInterceptedException
# 
# # ✅ CORRECT: Multiple solutions
# 
# # Solution 1: Close overlay/modal first
# try:
#     close_modal = driver.find_element(By.ID, "close-modal")
#     close_modal.click()
# except:
#     pass
# 
# # Solution 2: Wait for clickable and scroll into view
# login_button = wait.until(EC.element_to_be_clickable((By.ID, "login-btn")))
# driver.execute_script("arguments[0].scrollIntoView(true);", login_button)
# login_button.click()
# 
# # Solution 3: Use JavaScript click (bypasses interception)
# # login_button = driver.find_element(By.ID, "login-btn")
# # driver.execute_script("arguments[0].click();", login_button)  # ✅ JavaScript click works

# **************************Action Chains*************************
# move_to_element is used to move the mouse to the element(Hovering),when you call perform() the events are fired in the order they are queued up.
# click is used to click the element.
# send_keys is used to send keys to the element.
# context_click is used to right click the element.
# double_click is used to double click the element.
# drag_and_drop is used to drag and drop the element.
# drag_and_drop_by_offset is used to drag and drop the element by offset.
# key_down is used to press the key down.
# key_up is used to press the key up.
# in simple click we dont need move_to_element we can directly click the element it automatically move to the element and click it.

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains

options = Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
driver.maximize_window()
driver.get("https://www.flipkart.com/")

actions = ActionChains(driver,duration=2000) #duration is used to set the duration of the action in milliseconds of mouse speed.
actions.move_to_element(driver.find_element(By.XPATH, "//img[@alt='Dropdown with more help links']")).perform() #first we open the element dropdown to see the options.
actions.move_to_element(driver.find_element(By.XPATH, "//a[@title='Notification Preferences']")).click().perform() #then we click the notification preferences link. this order matters because if we click the link without opening the dropdown first it will not work.
