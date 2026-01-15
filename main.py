# from selenium import webdriver

# driver = webdriver.Chrome() #it install the chrome driver automatically to automate the chrome browser by selenium manager
# driver.get("https://www.google.com")
# print(driver.title)
# driver.quit()

# ****************************** CSS SELECTOR ***********************

# from selenium import webdriver #it is used to open the browser
# from selenium.webdriver.common.by import By #it is used to find the elements on the page
# from selenium.webdriver.chrome.options import Options #it is used to set the options for the browser
# options = Options()
# options.add_experimental_option("detach", True) #it is used to keep the browser open after the script is executed
# driver = webdriver.Chrome(options=options) #Instantiates a Chrome WebDriver with the configured options
# driver.get("https://rahulshettyacademy.com/AutomationPractice/") #it is used to open the url
# # driver.find_element(By.PARTIAL_LINK_TEXT, "InterviewQues/ResumeAssistance").click()
# driver.find_element(By.CSS_SELECTOR, "[value='radio2']").click() #it is used to click the radio button

#**************************XPATH**************************
# contains use when we don't know the exact text of the element and it is dynamically generated.
# we use double slashes for relative xpath (relative mean it is relative to the current element) and single slash for absolute xpath (absolute mean it is absolute to the root element).

