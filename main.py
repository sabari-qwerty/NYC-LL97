from openpyxl import load_workbook
from requests import get
from bs4 import BeautifulSoup
from time import sleep
from base64 import b64decode

from webdriver_manager.chrome import ChromeDriverManager 
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from PIL import Image
import io
import binascii

def getDobnow(address):
    dobnow_url = "https://a810-dobnow.nyc.gov:443/Publish/WrapperPP/PublicPortal.svc/getPublicPortalPropertyDetailsGet/" + address
    dobnow_cookies = {"ASP.NET_SessionId": "v25hp0qzu4airs2m2p4c4lgk", "_abck": "7B9BD723430B39615EB182E1B879774C~0~YAAQh7csMeYKHZqOAQAA5rVuzQtk77Lp5+Vq44++bDkmsQ+XLG1YiBp7RDNZ077Y3wZ+TDPPswwHLBmQHgAcZhKqdhULfAxeUA7BW5OA0V0vyfb5OF2hw776FqB1Gb8JUXLtApo8GWQoaj7ZgCc57aPO5jnVZYOnIfz/dNLu9qgUPswCXnre45xjzGsxcY0b2+QINnBrR31nLI6W1C+qvgsyqKYnO/ZN39QRQwx1k0jv28lO7itj60haaZ1RC5ve5+60HJ0QZDYfy/8ftM8YuYwIeHUZAkzRZfo5pA2BLmnnbpX34tZ+ZuhVBctU8A7xwQsvB2rEmhjk4IL3/fWDMK+INPuB0QyT8nqvb9PAVkLHwvX3veBFlxFf0eZgRjnOYci5U75JgDM8n1NxXdo2wl+qrOps~-1~-1~-1", "_gid": "GA1.2.689702731.1712843572", "PUNKDDUF": "02ab9cfba6-09e1-431EBSfgd9u6P62FUwH9-PeW0D-QCwSzQ1mcTNcCDqMiQfeQusVAyce_eNORTpKvfLFB8", "_gat_gtag_UA_128025137_1": "1", "bm_mi": "DC1224E8045FB1310D8FA41DB7920A7F~YAAQTQHARcfqYcSOAQAAn9vgzRcJ8P26TYNnO+8MmmrLWJPi1aI+Q5znjL/pJKCD86Lvard/JPeUcXG1O7uekbXqlcEZE0k6OmPXXczvyDnN6Kpy37Ldg5ilxS/uT+cp/Y6AcAx0ie6c4ZgTnENt/vuohJFQv/1lgHtTRHgMRJGo543oIP5b/hdqyD5YR3poN5cSGTpQiH/JQywzMw/IkpkiCEwwo7VrWKyAzqJuENw2fv0LbtCOkX0ZoUeRUxvRhAWrjnWG8CYDZIXFfudiLVCRHfuYsgLxJiS2XfXCVMBOh6xelLW3XEDvwG1oJP2wFu6i0QlqNEGVlyeLSoHCUqupq/6v/nkFtg==~1", "ak_bmsc": "E2592C13202400BFF4D383B52E1DA2AC~000000000000000000000000000000~YAAQTQHARefqYcSOAQAATPbgzRdB5n+eeiKlOTlIrFfWb7yeUOeAxlV2audnMjRZBE/nkhoIiKLtMeCb7VBx8xXURxp2YDvIfKu0zmWuqSp7Gfa+/cDijz/cTKHCDgnnK1caaCwpY2ZUy8awIPdiX7uh7YneXaxf7Csmu3MgqQoZUt38Z0KEQ3PFHXRu5YjPEJ5sD6cycN/P/DvbTssr6h3O6ZECsTFrcnafjee98UmX8SN4ydwXFVLJoZ6Z0LaPUbJ+ba1uQubpSkIyR3n4/GP+i5nkdP9wgOpDVcwXGY77h9dezZqBWpQR2zv+Z0qTvTU70tkX7mBR6Max+WpoTaHukC6fHo6ufFvL33+6fv4CODGauQrFqitW5nsesgjLvY9KSaIvz95IsfhNu1cTMvBkVWO2UsV64gJoBJ+MCOOzlXpdU3mWve0/s77vzQsDYc2c8L0FybXvnws07tqy/oggNlyBZv0hbqb7Cki//81kaybt0ne7+KRxKiqUju01BHOu9ucKdHBS", "bm_sz": "92FBD3DBDB986A0EFE3542B20EE41AD3~YAAQTQHARSjrYcSOAQAAQC7hzRf42I6qTrQzs68QctiPbBDk52ZFYO+9SpIv7xtzUMQ+YNETMmwa0LT1tHj6pPhi/cBSiK+3F2ESmqsNsUns1lhUUxmOlF9NRkCXCxQGiqldC0MGjoWm6L2HAKzs7h79zUV9X+/VNjVzKgseCeCLtEGqNfp+QkPrh83arhe5H1q3R0XiUhd6sm2PFTSsvF5heXGKOEjkhc34W5zG3UPSkCV6Ylp+H0+jnacldN02MA1/BnQqdCxxDgjHRJ9eL/cjPrx923OaJNSF4BMr+qnmtyOyyEnaHe9LGl3epkxrN0S2Rs2Qihr/dlXc0X/YpObXCLSrkS3mxsRyBQr98C9lLsIWs/Yg/FbQ1GihU13JKtdM7nSsBbYIAotv4GZ0i3QfufNPPNt9yvA=~3684145~3291461", "RT": "\"z=1&dm=a810-dobnow.nyc.gov&si=e577c804-bfa4-4a11-b664-c04d7b66cc3b&ss=luvfadaa&sl=1&tt=2kl&rl=1\"", "_ga_863DM8YSJL": "GS1.1.1712851046.4.1.1712851070.0.0.0", "_ga": "GA1.1.1937995955.1712671894", "bm_sv": "36B0CE8DBF80D5A323A413F8DA611279~YAAQTQHARTDrYcSOAQAA2zPhzReCz6YOeaCL4k4nU2RMEsEXNUPwk7zezfRmTSy8qcKSCB9HbPct/IUXTEhZLoqHYLhBK4MbJr5K0h8gdWpyt7MD7ilyUg54iKJYJD1nfkwq+DMHZzywPUFR+SHZ2DAbGY436bu6nH6YAKvt9Smym/T0CBEaGtj6NDUuPG1AcuB+mB8ADojMUuD9opZtDC0GypY0X3EpePaAhFLDTGRVbs0oX+AUeUSnWqYb~1"}
    dodnow_headers = {"Cache-Control": "no-cache", "Sec-Ch-Ua": "\"Chromium\";v=\"123\", \"Not:A-Brand\";v=\"8\"", "Pragma": "no-cache", "Userbrowserid": "PLPKJMpCzz+hVFda2UQ2RA==", "Sec-Ch-Ua-Mobile": "?0", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.6312.58 Safari/537.36", "Authtoken": "K5L7WnCGUbrax1Zvlv936w==", "Accept": "application/json, text/plain, */*", "If-Modified-Since": "Mon, 26 Jul 1997 05:00:00 GMT", "Sec-Ch-Ua-Platform": "\"Windows\"", "Sec-Fetch-Site": "same-origin", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Dest": "empty", "Referer": "https://a810-dobnow.nyc.gov/publish/Index.html", "Accept-Encoding": "gzip, deflate, br", "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8", "Priority": "u=1, i"}
    dobnow_res = get(dobnow_url, cookies=dobnow_cookies, headers=dodnow_headers).json()
    PropertyDetails = dobnow_res["PropertyDetails"]
    return PropertyDetails

def estpenalty(html): 

    soup = BeautifulSoup(html, 'html.parser')
    select_all_div = soup.findAll('g')

    dic = {}

    for num in range(0, len(select_all_div) -2):
        text = select_all_div[num].findAll('text')
        dic[text[0].text] = text[-1].text

    return dic

# def takeScreenshot(driver):


def takeImage(string):
    imge_bytes = b64decode(string)
    image_stream = io.BytesIO(imge_bytes)
    img = Image.open(image_stream)
    img.save('./data/output_image.png')



def selenium_chrome(value, name):

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


    print(len(select_table_all_tr))
    if len(select_table_all_tr) == 1:
        driver.close()
        return False 

    

    
    for tr in select_table_all_tr:

        if name.lower() in str(tr.get_attribute("innerText")).lower():

            button = tr.find_element(By.TAG_NAME, "button")

            button.click()

            select_building_summary = driver.find_element(By.CSS_SELECTOR, ".sc-jfvxQR.ljYkBH")

            inner_Summary_div = select_building_summary.find_elements(By.TAG_NAME,'div')

            dic = {}
            
            for div in inner_Summary_div:

                select_div =  str(div.get_attribute("innerText")).split(':')
                print(select_div)
                dic[select_div[0]] = select_div[-1]

            next_button =  driver.find_element(By.CSS_SELECTOR, '.sc-iveFHk')
            
            next_button.click()

            sleep(5)

            table_data =  driver.find_element(By.CSS_SELECTOR, ".table-g")

            html =  table_data.get_attribute("innerHTML")
            est_dic =   estpenalty(html)

            print(est_dic)

            png = driver.find_element(By.CSS_SELECTOR,'.sc-kgTSHT.cmoktC').screenshot_as_base64

            # print(png)
    
            imge_bytes = b64decode(png)
            image_stream = io.BytesIO(imge_bytes)
            img = Image.open(image_stream)
            img.show()
            img.save('output_image.png')
            print(png)



    sleep(10)
    driver.close()

    return True
    

sheet =  load_workbook('./NYC LL97 Targets.xlsx').active

for num in range(2, 40):

    select_data = [data.value for data in sheet[num:num]]

    property_address = select_data[1]

    door_num = ""
    street_address = ""
    
    for str_ in property_address.split(" "):

        if str(str_).isnumeric() or str(str_).split("-")[0].isnumeric():
             door_num =  str_.split("-")[0]
        else: 
            street_address += str_ + " "
    
    suffix_url = "1|" +  door_num + "|" + street_address.strip() + "|1"
    url_encode_data = suffix_url.replace("|", "%7C").replace(" ", "%20")
    donow_res =  getDobnow(url_encode_data)
    Bin =  donow_res["BIN"]

    value = ""

    for iter in range(0, 4):

        if value:
            break

        if iter % 2 == 0:
           value = selenium_chrome(str(property_address).strip(), property_address)
        else: 
           value = selenium_chrome(str(Bin).strip(), property_address)