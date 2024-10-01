import datetime
import random
import time
from selenium.webdriver.common.by import By
import psutil
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import subprocess
import pyautogui
pyautogui.FAILSAFE = False

import zipfile, requests

def driver_initialize():
    # kill the whole chrome that opened before
    for proc in psutil.process_iter():
        try:
            process_name = proc.name()
            process_id = proc.pid

            if 'chrome.exe' in process_name:
                print(f'Terminate process: {process_name}, ID: {process_id}')
                p = psutil.Process(process_id)
                p.terminate()

        except Exception as e:
            print(e
                  )
    # open chrome driver
    time.sleep(3)
    
    #pipe
    chrome_explorer = subprocess.Popen(
        r'C:\Program Files\Google\Chrome\Application\chrome.exe --remote-debugging-port=9222 --user-data-dir="C:\Users\user\temp"')

    chrome_options = Options()
    chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
    driver = webdriver.Chrome('chromedriver', options=chrome_options)
    print(f'New driver opened')

    for i in range(2):
        time.sleep(1)
        pyautogui.press('esc')

    return driver, chrome_explorer