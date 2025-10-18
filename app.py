import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

s = Service("C:\\Users\\Welcome\\OneDrive\\Desktop\\chromedriver.exe")
driver = webdriver.Chrome(service=s, options=chrome_options)

driver.get("https://www.smartprix.com/mobiles")

time.sleep(5)

driver.find_element(by=By.XPATH, value='//*[@id="app"]/main/aside/div/div[5]/div[2]/label[1]/input').click()
time.sleep(1)
driver.find_element(by=By.XPATH, value='//*[@id="app"]/main/aside/div/div[5]/div[2]/label[2]/input').click()
time.sleep(1)

old_height=driver.execute_script("return document.body.scrollHeight")
time.sleep(3)

counter=0
while True:
    print('clicked')
    driver.find_element(by=By.XPATH, value='//*[@id="app"]/main/div[1]/div[2]/div[3]').click()
    print(counter)
    counter+=1
    time.sleep(3)
    new_height=driver.execute_script("return document.body.scrollHeight")
    if new_height==old_height:
        break
    old_height=new_height

html = driver.page_source
with open("smartPhone.html","w",encoding="utf-8") as f:
    f.write(html)