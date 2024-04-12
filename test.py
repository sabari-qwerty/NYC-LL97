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

from pathlib import Path

def getDobnow(address):
    dobnow_url = "https://a810-dobnow.nyc.gov:443/Publish/WrapperPP/PublicPortal.svc/getPublicPortalPropertyDetailsGet/" + address
    dobnow_cookies = {"_gid": "GA1.2.1832189801.1712661164", "_abck": "959995977197097D415C93950939B293~0~YAAQz4MsMfWjSJmOAQAANSeJ0AvE9bmSo6kKqDlJl4gLpkmS43TJbXNOecHGPwxlaFEEXA261H4+ewJ1eSn/VKjt/vidcAwZuZ+CG4EwV3z/MWHmBEgq+XspAkDTX/d6A8LHCel5OQbo2Ww7kHB61UnfQjNT22nhMk51PdSKC3V+ZoV097ciyhM86xQ0/6cKE5WHCsPMYElLV0+99BNPh3tlRNq7knosuTyH2nPycWcbCwtzsKvr7f9UpwG4p8+uKVivD1DigGoPuMQxxkbqveQLt7dsNnj0Dk7rvEAJO7Ik+aS2swq7M06xaY3D63VSLTVJqlFmY8WQFoqPF88Bd3FweJYskf+0UR4hQRbEc5MBLgNpcfM2lUI9Gk/3kINSpCKhojt9an5sA9NSXPqgT8eSfAX8~-1~-1~-1", "bm_sz": "7152039AFBB2FB8E8D57A6423E4BAB43~YAAQz4MsMWwiSZmOAQAA6ZwX0Rf9I2AToClaw5MQMZsFP2rhZYVtAo37se9ctY64vFaIphNVmTfS25BJxwyEeHzCIhkyZE6YeHGv4C7Ld5/vIybTpR9veZz0muxtf9ReuEVzP54U8iJOf4YFX7XE2+mMsvHME14WiRgYOHgsACXo39r4/8LZIOCIgws77GupqlEm6d+z9azsvHDsZExm8ehrNxt1oJYAojF4c8h2Lgz+k/7Ch0j1EuxWO7kNhHe0ldnSLWzrmFm1aNdGDzb1L8z0AbtOAJbTechhQw3gIVQ4Nv8RuAlOLM1gTM92O2274tyU5o78AulqVE9eVR1YSfe4vtMLJvdZjasqoK2F3ORJoRuLDEAezihanqMD7wUad+V38SDAfoPXDFNXvq8IQ7ztDMra~4468784~3551793", "_ga_863DM8YSJL": "GS1.1.1712904971.13.0.1712904971.0.0.0", "_ga": "GA1.2.792185897.1710760621", "_gat_gtag_UA_128025137_1": "1", "bm_mi": "62999D8ECE4142449096C2403B3BF5CE~YAAQz4MsMX8iSZmOAQAARKsX0RdBJ42PD5k9n9alKnnmXMgMB5dFOeQmCh8o+AE8a2pCY3s5ezpY+Fi+ZxaUA9asadE7UTSW58BgdO2v24MsbEgH/8nwOb0Gpvt657ysszY6sqU8BS/+/Wcfch5PqnN/1l4wPAo6b40DEL5H7gUNU0dwvoY4sklxfwDd3QdevK361teajuPk0SBywS/txCnGnQGYAWAn++vrhCg6Ip5+16N8VceLl+6mI+6sSCTsJN0+Q8ej8O90PMpsghtMJqqj1GUPkwdGLa8YrCgn9kS92W3pMbqYUjHNOp4B4Y2oOKcaOMHYfJqYULiKDb3oCg==~1", "ASP.NET_SessionId": "abew5adcqw2i5ac43li13ybw", "ak_bmsc": "DAE85DE99DFD6CF6B8A6EF97FF74F6FB~000000000000000000000000000000~YAAQz4MsMZUiSZmOAQAASrAX0RendUSns5vBxKjCqlLlR3JLTGUKyd9pHEW2wscN/ONCOd5Xm6e4PrY1Olo+VbhsnRsBbWqAKQ5VKuyq5QELlY05+PY8Z5BCtAlGcC7WLwQsyLczqnNTKnVIiLasM77+89Z9dqXJT7LWVkApE0uysYbejTtrCANK4ZPirDntliW7i/gdfCI02EP2QnweKeWehBb37JqY7dApIJx3Bzm/ZQxJOfjTiz28iwf89vMgxT+meQ0mcx3ZossnM70eb4zo+ZHXugz4micGiPhe0Mhl3yQbawTmP7kxcyApiamNI3N4sco/nu9lamVy68SrNkPCArqvfnf1f95bcU/CYZsEry035doDhprEvFp/RDWyElElSlRNGGhU4dlkZ4afzgXUgRmVeFqydoQ3dZA+k/wrMlI6grU6ohzWIVBcBHLQ5HlKkbmVoTP8fR/BvjPs/HgV617U3p+O8K6Z5tl1SzInOSZKl0NV6lYQQmubP5C7eFPmdGpyng==", "PUNKDDUF": "02ab9cfba6-09e1-43JunnEDKAvnnDr_up1YJopB-SYszidiGqq83MgBtbc-8uWJArnIs79NrTy8T6YJmL1x0", "bm_sv": "1F7C9198E5A3649A57B7FFD88998A9B9~YAAQz4MsMagiSZmOAQAAuOAX0Re7rZLNDldD7B1RjAVxHQmXGtkvUaaqZn5dLPSkY+ELEGJSfG9nbTK70g/RDvdixce9XLRrG29l/tUpFAEeCDQ1pArQa6vVeeUbsohxPzZz2qu+/kiRIxVm/QKY6ExLTPjTEBzcXk+HPgW10qjNQgCnBzpHvYq4FL8vBOzZVntVr+lU7vM91q4K3kodg1zL9swcHKW0x8ZfJ3WjLC7Rm6zAAj9GJDPKnm/K~1"}
    dodnow_headers = {"Cache-Control": "no-cache", "Sec-Ch-Ua": "\"Chromium\";v=\"123\", \"Not:A-Brand\";v=\"8\"", "Pragma": "no-cache", "Userbrowserid": "GSbuQUTUE6Y/0o9548PZ2A==", "Sec-Ch-Ua-Mobile": "?0", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.6312.88 Safari/537.36", "Authtoken": "rcnKf5MB9mbTB3TIYinSaA==", "Accept": "application/json, text/plain, */*", "If-Modified-Since": "Mon, 26 Jul 1997 05:00:00 GMT", "Sec-Ch-Ua-Platform": "\"Linux\"", "Sec-Fetch-Site": "same-origin", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Dest": "empty", "Referer": "https://a810-dobnow.nyc.gov/publish/Index.html", "Accept-Encoding": "gzip, deflate, br", "Accept-Language": "en-US,en;q=0.9", "Priority": "u=1, i"}
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

def getGrade( Bbl, Bin):

    url = f"https://a810-dobnow.nyc.gov:443/Publish/WrapperPP/PublicPortal.svc/GetEnergyStarComplience/{Bin}/{Bbl}"
    cookie = {"_gid": "GA1.2.1832189801.1712661164", "_abck": "959995977197097D415C93950939B293~0~YAAQz4MsMfWjSJmOAQAANSeJ0AvE9bmSo6kKqDlJl4gLpkmS43TJbXNOecHGPwxlaFEEXA261H4+ewJ1eSn/VKjt/vidcAwZuZ+CG4EwV3z/MWHmBEgq+XspAkDTX/d6A8LHCel5OQbo2Ww7kHB61UnfQjNT22nhMk51PdSKC3V+ZoV097ciyhM86xQ0/6cKE5WHCsPMYElLV0+99BNPh3tlRNq7knosuTyH2nPycWcbCwtzsKvr7f9UpwG4p8+uKVivD1DigGoPuMQxxkbqveQLt7dsNnj0Dk7rvEAJO7Ik+aS2swq7M06xaY3D63VSLTVJqlFmY8WQFoqPF88Bd3FweJYskf+0UR4hQRbEc5MBLgNpcfM2lUI9Gk/3kINSpCKhojt9an5sA9NSXPqgT8eSfAX8~-1~-1~-1", "bm_sz": "7152039AFBB2FB8E8D57A6423E4BAB43~YAAQz4MsMWwiSZmOAQAA6ZwX0Rf9I2AToClaw5MQMZsFP2rhZYVtAo37se9ctY64vFaIphNVmTfS25BJxwyEeHzCIhkyZE6YeHGv4C7Ld5/vIybTpR9veZz0muxtf9ReuEVzP54U8iJOf4YFX7XE2+mMsvHME14WiRgYOHgsACXo39r4/8LZIOCIgws77GupqlEm6d+z9azsvHDsZExm8ehrNxt1oJYAojF4c8h2Lgz+k/7Ch0j1EuxWO7kNhHe0ldnSLWzrmFm1aNdGDzb1L8z0AbtOAJbTechhQw3gIVQ4Nv8RuAlOLM1gTM92O2274tyU5o78AulqVE9eVR1YSfe4vtMLJvdZjasqoK2F3ORJoRuLDEAezihanqMD7wUad+V38SDAfoPXDFNXvq8IQ7ztDMra~4468784~3551793", "_ga_863DM8YSJL": "GS1.1.1712904971.13.0.1712904971.0.0.0", "_ga": "GA1.2.792185897.1710760621", "_gat_gtag_UA_128025137_1": "1", "bm_mi": "62999D8ECE4142449096C2403B3BF5CE~YAAQz4MsMX8iSZmOAQAARKsX0RdBJ42PD5k9n9alKnnmXMgMB5dFOeQmCh8o+AE8a2pCY3s5ezpY+Fi+ZxaUA9asadE7UTSW58BgdO2v24MsbEgH/8nwOb0Gpvt657ysszY6sqU8BS/+/Wcfch5PqnN/1l4wPAo6b40DEL5H7gUNU0dwvoY4sklxfwDd3QdevK361teajuPk0SBywS/txCnGnQGYAWAn++vrhCg6Ip5+16N8VceLl+6mI+6sSCTsJN0+Q8ej8O90PMpsghtMJqqj1GUPkwdGLa8YrCgn9kS92W3pMbqYUjHNOp4B4Y2oOKcaOMHYfJqYULiKDb3oCg==~1", "ASP.NET_SessionId": "abew5adcqw2i5ac43li13ybw", "ak_bmsc": "DAE85DE99DFD6CF6B8A6EF97FF74F6FB~000000000000000000000000000000~YAAQz4MsMZUiSZmOAQAASrAX0RendUSns5vBxKjCqlLlR3JLTGUKyd9pHEW2wscN/ONCOd5Xm6e4PrY1Olo+VbhsnRsBbWqAKQ5VKuyq5QELlY05+PY8Z5BCtAlGcC7WLwQsyLczqnNTKnVIiLasM77+89Z9dqXJT7LWVkApE0uysYbejTtrCANK4ZPirDntliW7i/gdfCI02EP2QnweKeWehBb37JqY7dApIJx3Bzm/ZQxJOfjTiz28iwf89vMgxT+meQ0mcx3ZossnM70eb4zo+ZHXugz4micGiPhe0Mhl3yQbawTmP7kxcyApiamNI3N4sco/nu9lamVy68SrNkPCArqvfnf1f95bcU/CYZsEry035doDhprEvFp/RDWyElElSlRNGGhU4dlkZ4afzgXUgRmVeFqydoQ3dZA+k/wrMlI6grU6ohzWIVBcBHLQ5HlKkbmVoTP8fR/BvjPs/HgV617U3p+O8K6Z5tl1SzInOSZKl0NV6lYQQmubP5C7eFPmdGpyng==", "PUNKDDUF": "02ab9cfba6-09e1-43JunnEDKAvnnDr_up1YJopB-SYszidiGqq83MgBtbc-8uWJArnIs79NrTy8T6YJmL1x0", "bm_sv": "1F7C9198E5A3649A57B7FFD88998A9B9~YAAQz4MsMagiSZmOAQAAuOAX0Re7rZLNDldD7B1RjAVxHQmXGtkvUaaqZn5dLPSkY+ELEGJSfG9nbTK70g/RDvdixce9XLRrG29l/tUpFAEeCDQ1pArQa6vVeeUbsohxPzZz2qu+/kiRIxVm/QKY6ExLTPjTEBzcXk+HPgW10qjNQgCnBzpHvYq4FL8vBOzZVntVr+lU7vM91q4K3kodg1zL9swcHKW0x8ZfJ3WjLC7Rm6zAAj9GJDPKnm/K~1"}
    header = {"Cache-Control": "no-cache", "Sec-Ch-Ua": "\"Chromium\";v=\"123\", \"Not:A-Brand\";v=\"8\"", "Pragma": "no-cache", "Userbrowserid": "GSbuQUTUE6Y/0o9548PZ2A==", "Sec-Ch-Ua-Mobile": "?0", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.6312.88 Safari/537.36", "Authtoken": "rcnKf5MB9mbTB3TIYinSaA==", "Accept": "application/json, text/plain, */*", "If-Modified-Since": "Mon, 26 Jul 1997 05:00:00 GMT", "Sec-Ch-Ua-Platform": "\"Linux\"", "Sec-Fetch-Site": "same-origin", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Dest": "empty", "Referer": "https://a810-dobnow.nyc.gov/publish/Index.html", "Accept-Encoding": "gzip, deflate, br", "Accept-Language": "en-US,en;q=0.9", "Priority": "u=1, i"}
    res = get(url, cookies=cookie, headers=header).json()

    select_energyStart  = res["EnergyStar"]
    grade = select_energyStart["Grade"]
    score = select_energyStart["Score"]


    return {"grade": grade, "score": score}

    # return {"grade": grade, "score": score}
# def takeScreenshot(driver):


def takeImage(string, dir, fileName):
        
    imge_bytes = b64decode(string)
    image_stream = io.BytesIO(imge_bytes)
    img = Image.open(image_stream)


    path = Path(dir)
    path.mkdir(parents=True, exist_ok=True) 
    img.save(f'./{dir}/{fileName}.png')




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
                dic[select_div[0]] = select_div[-1]

            
            
            Bbl =  dic["NYC BBL"].strip().replace("-", "")
            Bin = dic["NYC BIN"].strip().replace("-", "")
          
            res =  getGrade(Bin, Bbl)
            
            
            next_button =  driver.find_element(By.CSS_SELECTOR, '.sc-iveFHk')
            
            next_button.click()

            sleep(5)

            table_data =  driver.find_element(By.CSS_SELECTOR, ".table-g")

            html =  table_data.get_attribute("innerHTML")
            est_dic =   estpenalty(html)


            carbon = driver.find_element(By.CSS_SELECTOR,'.sc-kgTSHT.cmoktC').screenshot_as_base64

            takeImage(carbon, name.lower(), "carbon")

            sleep(1)


            cost_page = driver.find_element(By.CSS_SELECTOR, ".fClbry")
            cost_page.click()

            sleep(1)

            cost = driver.find_element(By.CSS_SELECTOR,'.sc-kgTSHT.cmoktC').screenshot_as_base64

            takeImage(cost, name.lower(), "cost")

            # print(png)



    sleep(10)
    driver.close()

    return True
    

sheet =  load_workbook('./data.xlsx').active

for num in range(5, 40):

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
           value = selenium_chrome(str(Bin).strip(), property_address)
        else: 
            print(str(property_address).strip())
            print(property_address)
            value = selenium_chrome(str(property_address).strip(), property_address)