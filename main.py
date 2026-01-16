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

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
options = Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
# driver.find_element(By.XPATH, "//input[@value='radio2']").click()
# driver.find_element(By.XPATH, "//legend[text()='Suggession Class Example']").click()
# driver.find_element(By.XPATH, "//input[starts-with(@value, 'rad')]").click() #we need it when we have to click multiple elements 1 by 1 but we don't know the exact value of the element.
# driver.find_element(By.XPATH, "//input[contains(@value, 'adio')]").click() #contains used when we have to find the element by partial text.
# driver.find_element(By.XPATH, "//legend[contains(text(), 'Class Example')]").click() #find the element by partial text.
driver.find_element(By.XPATH, "//div[@id='radio-btn-example']/fieldset/label[@for='radio3']/input").click() #find the element by parent id and child for attribute to reach our goal of unique element.



# contains use when we don't know the exact text of the element and it is dynamically generated.
# we use double slashes for relative xpath (relative mean it is relative to the current element) and single slash for absolute xpath (absolute mean it is absolute to the root element).

