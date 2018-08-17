from selenium import webdriver
import os
import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
try:
	options = Options()
	options.add_argument("--headless")  # Runs Chrome in headless mode.
	options.add_argument('--no-sandbox')  # Bypass OS security model
	options.add_argument('--disable-gpu')  # applicable to windows os only
	options.add_argument('start-maximized')  #
	options.add_argument('disable-infobars')
	options.add_argument("--disable-extensions")
	driver = webdriver.Chrome(chrome_options=options,executable_path=r'C:\Users\shoebah\Downloads\chromedriver.exe')
	print("Headless Chrome Initialized on Windows OS")
	driver.implicitly_wait(20)
	driver.maximize_window()
	driver.get("https://www.naukri.com/mnjuser/homepage?id=")
	driver.find_element_by_id("usernameField").send_keys("user name") #give your user name or mail id here
	driver.find_element_by_id("passwordField").send_keys("password") # give your password here
	print("Page Successfully Login")
	driver.find_element_by_xpath("""//*[@id="loginForm"]/div[5]/div/button""").click()
	driver.find_element_by_xpath("""//*[@id="root"]/div/div/span/div/div/div[2]/div[1]/div[2]/div[1]/div/div[1]/a""").click()
	print("Enter into update profile section")
	ele=driver.find_element_by_tag_name("html")
	ele.send_keys(Keys.END,Keys.ARROW_UP,Keys.ARROW_UP,Keys.ARROW_UP)
	cwd = (os.path.expanduser("~/Desktop/ResumeAutomation/"))
	for i in os.listdir(cwd):
		path = os.path.join(cwd, i)
		if os.path.isdir(path):
			# skip directories
			continue
	print("Start reading file at loaction", path)
	driver.find_element_by_xpath("""//*[@id="attachCV"]""").send_keys(path)
	print("Resume Start Process")
	path2=r"C:\Users\shoebah\Desktop\ResumeAutomation\Snap\ResultOutput.png"
	driver.save_screenshot(path2)
	print("Resume Upadte successful")
	driver.quit()
except NoSuchElementException as exception:
	print ("Element not found and test failed")