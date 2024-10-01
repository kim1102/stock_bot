import pickle
import random
import time
import selenium
from selenium.webdriver.common.by import By

from utils import driver_initialize

if __name__ == '__main__':
    # 1. create chrome object
    driver, chrome_explorer = driver_initialize()
    alarm_thresh = 2
    # 2. alarm the stocks that decreased -3%
    target_stocks = ['https://m.stock.naver.com/worldstock/stock/TSLA.O/total',
                     'https://m.stock.naver.com/worldstock/stock/AMZN.O/total',
                     'https://m.stock.naver.com/worldstock/stock/NKE/total',
                     'https://m.stock.naver.com/worldstock/etf/SOXL.K/total']
    daily_increse = []
    week_decrease = []
        
    for stocks in target_stocks:
        stock_dec = False
        driver.get(stocks)
        time.sleep(2)
        
        info_var = driver.find_elements(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div/div/div[2]/div[1]/div[1]/div/span[2]")[0].text
        if '-' in info_var: stock_dec = True
        info_var = str(info_var).replace('+','').replace('-','').replace('%','')
        info_var = float(info_var)
        
        if info_var > alarm_thresh:
            current_target = stocks.split('/')[-2]
            if stock_dec: # decreased stock
                daily_increse.append(current_target)
                print(f'Decreased [{current_target}] UP-DOWN{info_var}%, Its over {alarm_thresh}%')
            else: # increased stock
                print(f'Increased [{current_target}] UP-DOWN{info_var}%, Its over {alarm_thresh}%')
                
    # 3. get the greedy-fear information
    driver.get('https://www.cnn.com/markets/fear-and-greed')
    greedy_info = driver.find_elements(By.XPATH, "/html/body/div[1]/section[4]/section[1]/section[1]/div/section/div[1]/div[2]/div[1]/div/div[1]/div[1]/div/div[4]/span")[0].text
    greedy_info = float(greedy_info)
    if greedy_info < 25: print(f'extreme fear, strongly recommend for buy stocks')
    elif greedy_info < 45: print(f'fear, recommend to buy stocks')
    elif greedy_info < 55: print(f'neutral, up to you')
    elif greedy_info < 75: print(f'greedy, dont recommend to buy stocks')
    else: print(f'extreme greedy, strongly dont recommend to buy stocks')
    
    # 4. complete the sentence