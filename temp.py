from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import time
import base64
import json
from selenium.webdriver.common.keys import Keys
import pyautogui

#joyce
def Search():
    with open('D:\Ricky\program\Auto_badminton\cookie.json') as f:
        cookies = json.load(f)
    #options.add_argument("--disable-notifications")
    '''selenium搜尋並輸入'''
    driver = webdriver.Edge()
    
    # pls ignore the next line
    #downoad link:https://developer.chrome.com/docs/chromedriver/downloads/version-selection?hl=zh-tw

    driver.get("https://nthualb.url.tw/reservation/reservation?d=4")

    for cookie in cookies:
        driver.add_cookie(cookie)
    driver.refresh()
    time.sleep(1)
    
    while (1):
        t = time.time()
        tt =(time.localtime(t))
        if (tt.tm_hour == 0):break
        time.sleep(0.01)
        if (tt.tm_sec > 50):
            print(time.asctime(tt))
        
    time.sleep(0.1)
    driver.refresh()
    

    #code source from:https://steam.oxxostudio.tw/category/python/spider/selenium.html
    
    book = driver.find_element(By.XPATH,'//*[@value="011"]').click() # 013

    pyautogui.press("enter") 
    time.sleep(0.5)
        
    book = driver.find_element(By.XPATH,'//*[@value="012"]').click() # 013

    pyautogui.press("enter") 
    time.sleep(0.5)

    
    driver.quit()

Search()






