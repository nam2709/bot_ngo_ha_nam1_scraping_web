
from selenium import webdriver
from selenium.webdriver.common.by import By
import json
import time
import selenium 
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.service import Service 
print(selenium.__version__)
chrome_options = webdriver.ChromeOptions()
chrome_driver_path = r'C:\Users\ngo ha nam\bot_scrape-data-web\chromedriver.exe'
service  =  ChromeService(r'C:\Users\ngo ha nam\bot_scrape-data-web\chromedriver.exe')

chrome_options.binary_location = chrome_driver_path
with open("data.json", "w") as f:
    json.dump([], f)
def write_json(new_data, filename='data.json'):
    with open(filename,'r+') as file:
        # First we load existing data into a dict.
        file_data = json.load(file)
        # Join new_data with file_data inside emp_details
        file_data.append(new_data)
        # Sets file's current position at offset.
        file.seek(0)
        # convert back to json.
        json.dump(file_data, file, indent = 10) 
        # số 10 này là số thuộc tín cần lưu

def getData():
    browser = webdriver.Chrome(options=chrome_options)
    # browser = webdriver.Chrome(service=service)
    # browser=webdriver.Chrome(service=ChromeService(ChromeDriverManager(version="114.0.5735.90").install()),options=options)
    browser.get('https://clutch.co/hr/california?page=1') # đây là địa chỉ trang web
    browser.maximize_window() # mở rộng tối đa cửa sổ
    time.sleep(5)
    browser.find_element(By.ID, 'CybotCookiebotDialogBodyButtonAccept').click()
    elements = browser.find_elements(By.CLASS_NAME, 'provider')
    for element in elements:
        try:
            # Click on the element
            # time.sleep(1)  # Give time for the action to take effect
            company_element = element.find_element(By.CLASS_NAME, 'company_title')
            link_element = element.find_element(By.CLASS_NAME, 'website-link__item')
            company = company_element.text
            link = link_element.get_attribute('href')
            # Retrieve the value of the clicked element
            value = element.text
            print("Element value:", value)
            
            data = {
                "company": company,
                "link"  : link
            }

            write_json(data)
            
            # Use your write_json function to save the data
            
                # Go back to the previous page to continue the loop
        except:
            print("Element not found or could not be clicked")
     
    
    time.sleep(2000)
    
if __name__ == '__main__': #chương trình sẽ chạy nếu đây là main
    getData()
# import pandas as pd
# with open("data-info.json") as f:
#     data= pd.read_json(f)
# data.to_excel('data.xlsx',index=False)