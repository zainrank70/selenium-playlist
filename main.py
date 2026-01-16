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

# ********************Select multiple checkboxes ,select using conditions********************

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
options = Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
# for i in range(1, 4):
#     driver.find_element(By.XPATH, f"//input[@value='option{i}']").click()

# checkboxes = driver.find_elements(By.XPATH, "(//input[starts-with(@name, 'checkBoxOption')])[position()<3]") #use elements when we have to find multiple elements. position()<3 means first 2 elements.
# print(len(checkboxes))
# for checkbox in checkboxes:
#     print(checkbox.get_attribute("value")) #get_attribute used to get value of the attribute.
#     checkbox.click()

# if we wanna not to check all checkboxes then we can use the following code
checkboxes = driver.find_elements(By.XPATH, "//input[starts-with(@name, 'checkBoxOption')]") 
print(len(checkboxes))
for checkbox in checkboxes:
    if checkboxes.index(checkbox)+1 != 2:
        checkbox.click()