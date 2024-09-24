from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import time
from bs4 import BeautifulSoup
import base64
from PIL import Image
import pytesseract
import numpy as np
from de_noise import noise_remove_pil
import json
from selenium.webdriver.common.keys import Keys
import pyautogui


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
    time.sleep(3)
    '''
    while (1):
        t = time.time()
        tt =(time.localtime(t))
        if (tt.tm_hour != 0):
            time.sleep(0.01)
    '''
    

    driver.refresh()
    

    #code source from:https://steam.oxxostudio.tw/category/python/spider/selenium.html
    
    book = driver.find_element(By.XPATH,'//*[@value="613"]').click() # 013

    pyautogui.press("enter") 
    time.sleep(0.5)

    book = driver.find_element(By.XPATH,'//*[@value="614"]').click() # 013
    pyautogui.press("enter") 
    time.sleep(0.5)   
    
    driver.quit()

#Search()






