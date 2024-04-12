from webdriver_manager.chrome import ChromeDriverManager 
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from PIL import Image
import io
import binascii

from pathlib import Path
from time import sleep
from base64 import b64decode
from bs4 import BeautifulSoup
from openpyxl import load_workbook

def takeImage(string, dir, fileName):
        
    imge_bytes = b64decode(string)
    image_stream = io.BytesIO(imge_bytes)
    img = Image.open(image_stream)


    path = Path(dir)
    path.mkdir(parents=True, exist_ok=True)

    path =   f'./{dir}/{fileName}.png'
    img.save(path)

    return path

def estpenalty(html): 

    soup = BeautifulSoup(html, 'html.parser')
    select_all_div = soup.findAll('g')

    dic = {}

    for num in range(0, len(select_all_div) -2):
        text = select_all_div[num].findAll('text')
        dic[text[0].text] = text[-1].text

    return dic

def selenium_chrome(value, folderName):

    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get("https://www.be-exchange.org/calculator/")

    sleep(10)

    cal_page = driver.find_element(By.CSS_SELECTOR, ".sc-gswNZR.sc-hLBbgP.fkJIIU.hFTahi")
    cal_page.click()
    
    sleep(5)

    input_tag = driver.find_element(By.CSS_SELECTOR, ".MuiInputBase-input.MuiOutlinedInput-input.css-1x5jdmq")
    input_tag.send_keys(value)

    sleep(25)


    select_table = driver.find_element(By.CSS_SELECTOR, ".MuiTable-stickyHeader")
    select_table_all_tr = select_table.find_elements(By.CSS_SELECTOR, ".MuiTableRow-root.css-18rv9fi")

    if len(select_table_all_tr) == 1:
        driver.close()
        return False 

    for tr in select_table_all_tr:



        if value.lower() in str(tr.get_attribute("innerText")).lower():

            button = tr.find_element(By.TAG_NAME, "button")

            button.click()

            select_building_summary = driver.find_element(By.CSS_SELECTOR, ".sc-jfvxQR.ljYkBH")

            inner_Summary_div = select_building_summary.find_elements(By.TAG_NAME,'div')

            dic = {}
            
            for div in inner_Summary_div:

                select_div =  str(div.get_attribute("innerText")).split(':')
                dic[select_div[0]] = select_div[-1]

            print(dic)

            
            
            Bbl =  dic["NYC BBL"].strip().replace("-", "")

            Bin = dic["NYC BIN"].strip().replace("-", "")
          
            # res =  getGrade(Bin, Bbl)
            
            
            next_button =  driver.find_element(By.CSS_SELECTOR, '.sc-iveFHk')
            
            next_button.click()

            sleep(5)

            table_data =  driver.find_element(By.CSS_SELECTOR, ".table-g")

            html =  table_data.get_attribute("innerHTML")
            # est_dic =   estpenalty(html)


            res = estpenalty(html)

            print(res)

            carbon = driver.find_element(By.CSS_SELECTOR,'.sc-kgTSHT.cmoktC').screenshot_as_base64

            takeImage(string=carbon, dir=value.lower(), fileName="carbon")

            sleep(1)


            cost_page = driver.find_element(By.CSS_SELECTOR, ".fClbry")
            cost_page.click()

            sleep(1)

            cost = driver.find_element(By.CSS_SELECTOR,'.sc-kgTSHT.cmoktC').screenshot_as_base64

            # print(carbon, cost)
            takeImage(string=cost, dir=value.lower(), fileName="cost")

ls = load_workbook('data.xlsx').active

for num in range(2, len(ls["A"])):
    value = [data.value for data in ls[num:num]]

    selenium_chrome(value[1], folderName=value[1])
    # print()