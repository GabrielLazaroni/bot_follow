
'''from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class InstagramBot: 
  def __init__(self, username, password):
    self.username = username
    self.password = password
    self.driver = webdriver.Chrome(executable_path=r'./chromedriver.exe')

  def login(self):
    driver = self.driver
    driver.get('https://www.instagram.com')
    time.sleep(2)
    user_element = driver.find_element_by_xpath("//input[@name='username']")
    user_element.clear()
    user_element.send_keys(self.username)
    password_element = driver.find_element_by_xpath("//input[@name='password']")
    password_element.clear()
    password_element.send_keys(self.password)
    password_element.send_keys(Keys.RETURN)
    time.sleep(10)
    self.search_name('debetti')
    self.followers()
    self.scroll_followers()
   
    
  def search_name(self, profilename):
    driver = self.driver
    driver.get('https://www.instagram.com/' + profilename + '/')
    time.sleep(5)

  def followers(self):
    driver = self.driver
    followers_button = driver.find_element_by_xpath("//a[@href='/debetti/followers/']")
    followers_button.click()
    time.sleep(5)
    
  def scroll_followers(self):
    driver = self.driver
    for i in range(1, 3):
      driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(5)

  def click_to_follow(self):
    driver = self.driver
    driver.find_element_by_css_selector('button').click()
    time.sleep(10)



gabriel_bot = InstagramBot('gabriellggomes', '96351844')
gabriel_bot.login()
'''