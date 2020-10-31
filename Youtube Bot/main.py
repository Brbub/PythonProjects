from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os
import keyboard



class Youtube():
   def  __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Chrome(executable_path=r"C:\Users\Brandon\Downloads/chromedriver.exe")
   def login(self):
        self.driver.get("https://www.youtube.com/")
        time.sleep(1)
        self.driver.find_element_by_xpath('/html/body/ytd-app/div/div/ytd-masthead/div[3]/div[2]/div[2]/ytd-button-renderer/a/paper-button').click()
        time.sleep(1)
        try:
            self.driver.find_element_by_xpath('//*[@id="view_container"]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div/div/ul/li[3]/div').click()
        except:
            pass
        self.driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input').clear()
        self.driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input').send_keys(self.username)
        self.driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input').send_keys(Keys.RETURN)
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input').clear()
        self.driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input').send_keys(self.password)
        self.driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input').send_keys(Keys.RETURN)
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="passwordNext"]/div[2]').click()
   def channel(self, channel):
       self.driver.get("https://www.youtube.com/user/" + channel)
   def main(self): 
        self.login()
        self.channel('PewDiePie')

if __name__ == "__main__":
    Youtube('brbub67@yahoo.com','Guinnessbub11').main()



"""
def login(password, username):
    driver.get("https://www.instagram.com/")
    time.sleep(1)
    driver.get("https://www.instagram.com/accounts/login/?source=auth_switcher")   
    time.sleep(1)
    username_field = driver.find_element_by_name("username")
    password_field = driver.find_element_by_name("password")
    username_field.send_keys(username)
    password_field.send_keys(password)
    time.sleep(1)
    driver.find_elements_by_xpath("//div[contains(text(), 'Log In')]")[0].click()
    time.sleep(3.5)
    driver.find_elements_by_xpath("//button[contains(text(), 'Not Now')]")[0].click()
def comment(account, comment):
    #driver.get(("https://www.instagram.com/" + str(account) + "/"))   
    driver.find_element_by_class_name("BrX75").click()
    time.sleep(1)
    driver.find_element_by_class_name("_9AhH0").click()
    time.sleep(1)
    driver.find_element_by_class_name("dCJp8 afkep").click()
    driver.find_elements_by_xpath("//div[contains(text(), 'Add a comment…')]")[0].click()
    driver.find_element_by_class_name("Ypffh").send_keys(comment)
    driver.find_element_by_class_name("sqdOP yWX7d    y3zKF     ").click()




login("14724174214","ThisIsNotAnAutomatedBot")   
comment("_schmula_", "Great post!")
if keyboard.is_pressed("q"):  # if key 'q' is pressed 
        exit()

    


"""










"""
html = requests.get("https://en.wikipedia.org/wiki/Dog")
doc = lxml.html.fromstring(html.content)
title = doc.xpath("//div[@class='hatnote navigation-not-searchable']/text()")
information = doc.xpath('//p[@]')
print(title)
"""


