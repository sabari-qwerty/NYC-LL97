from webdriver_manager.chrome import ChromeDriverManager 
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By

from PIL import Image
import io
from requests import get

from pathlib import Path
from time import sleep
from base64 import b64decode
from bs4 import BeautifulSoup
from openpyxl import load_workbook


def getDobnow(address):
    dobnow_url = "https://a810-dobnow.nyc.gov:443/Publish/WrapperPP/PublicPortal.svc/getPublicPortalPropertyDetailsGet/" + address
    dobnow_cookies = {"_gid": "GA1.2.689702731.1712843572", "_abck": "7B9BD723430B39615EB182E1B879774C~0~YAAQB7xWaBlRHpqOAQAA7UY81gv2HHHvALC0PydAt7cTfk23QwRSJrMlvyfN7CdyztrV8NmPWDrz9sXJtrHAZoG6FYkiknfyi1YdYY5/cyFkMsyUredXo2cRhpQTwKDJxSQz4UqvaXY/0NF5U+Oz1y9dZW0soowggeZmMcDKsPTIlTo5LwAIHOT/Gq/iQOcN/xGx3ZnrYtUKGOr8NpndbtqFTMohhBTn4rTSDpRLb/yCuSq2089GS7FgWRlZ2hA+9HKr0KE+3GWAejLwBl61O7ioOzQn5nePdvrzi8/6cOIsuCzfGLGtbIgjJNFTY56hzBKh8vPTudR+PLJtcn5/2Mtcx878Esvhb2kO24XxQUQMFJeOTEkOECP+ZOuuvzbr0tkxWh07dhm8lS+hnXqTUXGz+R+H~-1~-1~-1", "RT": "\"z=1&dm=a810-dobnow.nyc.gov&si=e577c804-bfa4-4a11-b664-c04d7b66cc3b&ss=luxqrlny&sl=0&tt=0\"", "PUNKDDUF": "02ab9cfba6-09e1-43u_Fnmlq4ZleIeHjX2HzwAyBLZsl0MExL5x4xuE30LaoCbvVt-YaxoeaRohEEIulxySU", "bm_mi": "A80D6F4A12AC0019E15668796D02CBB6~YAAQz4MsMZPCUZmOAQAA7fCv1hephG+OsywR9HC+xWHNe2VqcZUnXKz3wmE+5B2YzKLwWEwSK+C7VD4Y33NrtLPpZpmZeqAZHd/MYSyOVp+tXN9F4SqtV6qqnxZlMPKshwvI8A+5si0J5j4MOejZpUqcqkZ5E3O1PgyDJQMCqYGpJEpFvSW6Plwhgr19WNzfErHum5hHw8nLdAH2fGAE3Eeo6R4XBtZgPNnO7adnwtP62Y32u64kDpUC1BbykLjz27cCP6o5ulNJalvFRbDNGYckZXeOOO3U7zF6oXJ8U4uvq43nEDzvX0QMH6DqlceHUtqBeSg1/4fh5nljbj0/e4u5Bw2OX9l+1Q==~1", "ASP.NET_SessionId": "4hniii33xfzoez033kbcknz1", "ak_bmsc": "B1FF7651ACC44F0961EF873AB26EEF6F~000000000000000000000000000000~YAAQz4MsMZjCUZmOAQAA6fWv1hd3F+YCtVKMJsRIiOwvDokQphGm2pjhXrZdqlkuuCc+9rPkqhfGl0Md1av1GsqDDHTUPXastJDSOICIqiTrmt/Is9tKrb2m6kwYkNtU+36Klk6BUQMHPA89mbHuRjmbhw8KJGPaaICF1DQATRC/dhx7WNq3w27CVh4lQ6pgYIaLWzcLBgoSZ4E/PMamMexrAJFVH/sA2mVofKYVKOn5yZ7YbMGwvBulZxoF7baM7KTWMZXWUL6PND8g21rzcySfayI4MDh7YQYgilQ6ZPIJKHHLItLCsSR2tO6D11GN4VsxDsaLjxhuv0RwbbPtHL5HZrilyC/0aSL+BcT6G/jgx4xFbBthboqxGncDw5qkGwvTDPOqHKQ3UGmY2sepOaoi0MmcxxdcgA9NqA8TYpKbF7Ckxu20T9pbkDRrQlXQly9N/jJJyeuhfbpFAMZYwtkysO2Zimu8VzNo5ICzZqKj61+lasFIB8+aFaFHtA==", "bm_sz": "3135608BDD8B554AEAA7A5F599FF2EB9~YAAQz4MsMQnvUZmOAQAANeD31hc/O20vPXMzT4Bw5TLpsY0fmqOmQzMxanBbDmyXDUGL4oWQ5dM9XfJHLn66X71T1Nel2SY+myo1D5foZrlI0MqyJw9PQgLARy6uCZQBBUa1lfR/+wXflX4+IX0xyd8brog39vfC6rSB+8bPKhz2iKWWUJ7smwTHga/TBfkOWA4+sjdmRIPUokLj5PctOvuT7M41c78c+0VpPlnXizKK5ftJ44hY1nH8p0EUPcl3Qi8gkZ69d4Fll/wDpkfLs/0PGTcPiTdWzYUw3hEAsQKGrryX/t2NqlHr8u7ZKG4W5u789K3V9dKMDh77oiR5Ww5jI+9F7ReVLvR2BiZNTuzhMUWrLAZ/6OG3MY8pJee32I62okr7bHB/0S1eFfaU2hB0S5elX5Ko+bWx9prA0Y8ol2OT~4601156~3359041", "_gat_gtag_UA_128025137_1": "1", "_ga_863DM8YSJL": "GS1.1.1713002702.8.1.1713003554.0.0.0", "_ga": "GA1.1.1937995955.1712671894", "bm_sv": "398EF06C9B0F71B04FFD9BAFF58F0198~YAAQz4MsMXHvUZmOAQAAYUH41hfRPk0cMgYDe79Dor9NPemp3agFIcTnCFDMYthMmaRnypBxyKK1VjbX+1cRTC3Ywfjo8+TKYUPP++IBytKC7Lb5zY7mVo75BQvppdG0UlkZSS/HTmkwl7n0qFnHyWMFaRdzbAXk8w4YaNfTAlUhI5DqUhOX6WoH7O2yHrAG6v9r6FbZXMd33vjfMzqkFp04HMZPm20RfrK6mGum5q0PLj3iyUEdTzDBSD/nnw==~1"}
    dodnow_headers = {"Cache-Control": "no-cache", "Sec-Ch-Ua": "\"Chromium\";v=\"123\", \"Not:A-Brand\";v=\"8\"", "Pragma": "no-cache", "Userbrowserid": "4KwOJuWx21eVxXg47FAzGw==", "Sec-Ch-Ua-Mobile": "?0", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.6312.88 Safari/537.36", "Authtoken": "GYY4OIwhJswa+183VzU26g==", "Accept": "application/json, text/plain, */*", "If-Modified-Since": "Mon, 26 Jul 1997 05:00:00 GMT", "Sec-Ch-Ua-Platform": "\"Windows\"", "Sec-Fetch-Site": "same-origin", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Dest": "empty", "Referer": "https://a810-dobnow.nyc.gov/publish/Index.html", "Accept-Encoding": "gzip, deflate, br", "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8", "Priority": "u=1, i"}
    dobnow_res = get(dobnow_url, cookies=dobnow_cookies, headers=dodnow_headers).json()
    PropertyDetails = dobnow_res["PropertyDetails"]
    return PropertyDetails

def getGrade(bin,  bbl):
    
    url = f"https://a810-dobnow.nyc.gov:443/Publish/WrapperPP/PublicPortal.svc/GetEnergyStarComplience/{bbl}/{bin}"
    cookies = {"_gid": "GA1.2.689702731.1712843572", "_abck": "7B9BD723430B39615EB182E1B879774C~0~YAAQB7xWaBlRHpqOAQAA7UY81gv2HHHvALC0PydAt7cTfk23QwRSJrMlvyfN7CdyztrV8NmPWDrz9sXJtrHAZoG6FYkiknfyi1YdYY5/cyFkMsyUredXo2cRhpQTwKDJxSQz4UqvaXY/0NF5U+Oz1y9dZW0soowggeZmMcDKsPTIlTo5LwAIHOT/Gq/iQOcN/xGx3ZnrYtUKGOr8NpndbtqFTMohhBTn4rTSDpRLb/yCuSq2089GS7FgWRlZ2hA+9HKr0KE+3GWAejLwBl61O7ioOzQn5nePdvrzi8/6cOIsuCzfGLGtbIgjJNFTY56hzBKh8vPTudR+PLJtcn5/2Mtcx878Esvhb2kO24XxQUQMFJeOTEkOECP+ZOuuvzbr0tkxWh07dhm8lS+hnXqTUXGz+R+H~-1~-1~-1", "RT": "\"z=1&dm=a810-dobnow.nyc.gov&si=e577c804-bfa4-4a11-b664-c04d7b66cc3b&ss=luxqrlny&sl=0&tt=0\"", "PUNKDDUF": "02ab9cfba6-09e1-43u_Fnmlq4ZleIeHjX2HzwAyBLZsl0MExL5x4xuE30LaoCbvVt-YaxoeaRohEEIulxySU", "bm_mi": "A80D6F4A12AC0019E15668796D02CBB6~YAAQz4MsMZPCUZmOAQAA7fCv1hephG+OsywR9HC+xWHNe2VqcZUnXKz3wmE+5B2YzKLwWEwSK+C7VD4Y33NrtLPpZpmZeqAZHd/MYSyOVp+tXN9F4SqtV6qqnxZlMPKshwvI8A+5si0J5j4MOejZpUqcqkZ5E3O1PgyDJQMCqYGpJEpFvSW6Plwhgr19WNzfErHum5hHw8nLdAH2fGAE3Eeo6R4XBtZgPNnO7adnwtP62Y32u64kDpUC1BbykLjz27cCP6o5ulNJalvFRbDNGYckZXeOOO3U7zF6oXJ8U4uvq43nEDzvX0QMH6DqlceHUtqBeSg1/4fh5nljbj0/e4u5Bw2OX9l+1Q==~1", "ASP.NET_SessionId": "4hniii33xfzoez033kbcknz1", "ak_bmsc": "B1FF7651ACC44F0961EF873AB26EEF6F~000000000000000000000000000000~YAAQz4MsMZjCUZmOAQAA6fWv1hd3F+YCtVKMJsRIiOwvDokQphGm2pjhXrZdqlkuuCc+9rPkqhfGl0Md1av1GsqDDHTUPXastJDSOICIqiTrmt/Is9tKrb2m6kwYkNtU+36Klk6BUQMHPA89mbHuRjmbhw8KJGPaaICF1DQATRC/dhx7WNq3w27CVh4lQ6pgYIaLWzcLBgoSZ4E/PMamMexrAJFVH/sA2mVofKYVKOn5yZ7YbMGwvBulZxoF7baM7KTWMZXWUL6PND8g21rzcySfayI4MDh7YQYgilQ6ZPIJKHHLItLCsSR2tO6D11GN4VsxDsaLjxhuv0RwbbPtHL5HZrilyC/0aSL+BcT6G/jgx4xFbBthboqxGncDw5qkGwvTDPOqHKQ3UGmY2sepOaoi0MmcxxdcgA9NqA8TYpKbF7Ckxu20T9pbkDRrQlXQly9N/jJJyeuhfbpFAMZYwtkysO2Zimu8VzNo5ICzZqKj61+lasFIB8+aFaFHtA==", "bm_sz": "3135608BDD8B554AEAA7A5F599FF2EB9~YAAQz4MsMQHkUZmOAQAAy+Tq1hcQsKPmaNXDgznGbgKUuF/gwHtozbS+LrvvqJGgK/FQSLBjSi2FyAZBP81rMhvqZ2BzigNJTLb2s56OQjtR1gY6zuFA+pH6xYqNg/Ga15D3hMoaobFPiydOIzK8RD6zJEYf7vYXtygD+ATpo2N1ZUQPJ760Uvi/NSuQpaeldXy6ALtmjDLppcLljT1/z2KSjBOgtlwUusbkk24NnPHtnl8LEXu26Za5QVhk6b58agC8OinuSHVQFhpZZ5kPBaO9x2w/Yr9iMP6m7zqYsZtfgdNSLu5ayUR7EY3LtNdv+UFY5L59PncJS7V3j7dVTVqISOdZ5TiThN7QvJ+mxpQfivrXY8iXPqM1pwjBDeQTuwtprp8shX+mIg5HGhBmjZ+N5UHlux1zp2ir7Mg=~4601156~3359041", "_gat_gtag_UA_128025137_1": "1", "_ga_863DM8YSJL": "GS1.1.1713002702.8.1.1713002703.0.0.0", "_ga": "GA1.1.1937995955.1712671894", "bm_sv": "398EF06C9B0F71B04FFD9BAFF58F0198~YAAQz4MsMQ7kUZmOAQAAiO7q1hd8cufeAD8PvyRxADQkC8dOHeDkYc42eQQqQoIAPbV+KFHZfcSBD6ahQ3YTUlW9rPaKNI2C1eVvocHk+cdLyFPLPHmCDmUPWOYt6JgWcpuRr5xyNA/dWxUXZIQaA4YdXwn4346ZKM5TE1iWcfhS49xQrS5uxXijeZTavr/96UpfDjUnXXT02nB9KyZWOAqvLCX0NotOHKofUOqusMlSy3WWTDP5T0KLDqwV~1"}
    headers = {"Cache-Control": "no-cache", "Sec-Ch-Ua": "\"Chromium\";v=\"123\", \"Not:A-Brand\";v=\"8\"", "Pragma": "no-cache", "Userbrowserid": "ApkI6bf3NX2qIcbmsSvLvQ==", "Sec-Ch-Ua-Mobile": "?0", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.6312.88 Safari/537.36", "Authtoken": "GYY4OIwhJswa+183VzU26g==", "Accept": "application/json, text/plain, */*", "If-Modified-Since": "Mon, 26 Jul 1997 05:00:00 GMT", "Sec-Ch-Ua-Platform": "\"Windows\"", "Sec-Fetch-Site": "same-origin", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Dest": "empty", "Referer": "https://a810-dobnow.nyc.gov/publish/Index.html", "Accept-Encoding": "gzip, deflate, br", "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8", "Priority": "u=1, i"}

    res = get(url, headers=headers, cookies=cookies).json()

    return res["EnergyStar"]["Gradescore"]

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

def selenium_chrome(id, value, folderName):

    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get("https://www.be-exchange.org/calculator/")

    sleep(10)

    cal_page = driver.find_element(By.CSS_SELECTOR, ".sc-gswNZR.sc-hLBbgP.fkJIIU.hFTahi")
    cal_page.click()
    
    sleep(5)

    input_tag = driver.find_element(By.CSS_SELECTOR, ".MuiInputBase-input.MuiOutlinedInput-input.css-1x5jdmq")
    input_tag.send_keys(id)

    sleep(25)


    select_table = driver.find_element(By.CSS_SELECTOR, ".MuiTable-stickyHeader")
    select_table_all_tr = select_table.find_elements(By.CSS_SELECTOR, ".MuiTableRow-root.css-18rv9fi")

    if len(select_table_all_tr) == 1:
        driver.close()
        return False 

    for tr in select_table_all_tr:


        _data = str(tr.get_attribute("innerText")).lower()

        if value.lower() in _data  or id in _data:

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
          
            grade =  getGrade(Bin, Bbl)

            dic["grade"] = grade
            
            
            next_button =  driver.find_element(By.CSS_SELECTOR, '.sc-iveFHk')
            
            next_button.click()

            sleep(5)

            table_data =  driver.find_element(By.CSS_SELECTOR, ".table-g")

            html =  table_data.get_attribute("innerHTML")
            # est_dic =   estpenalty(html)




            carbon = driver.find_element(By.CSS_SELECTOR,'.sc-kgTSHT.cmoktC').screenshot_as_base64

            carbon_path = takeImage(string=carbon, dir=value.lower(), fileName="carbon")

            sleep(1)


            cost_page = driver.find_element(By.CSS_SELECTOR, ".fClbry")
            cost_page.click()

            sleep(1)

            cost = driver.find_element(By.CSS_SELECTOR,'.sc-kgTSHT.cmoktC').screenshot_as_base64

            # print(carbon, cost)
            cost_path =  takeImage(string=cost, dir=value.lower(), fileName="cost")

            res = estpenalty(html)



            return {
                "dic": dic,
                "res": res,
                "cost_path": cost_path,
                "carbon_path": carbon_path
            }




ls = load_workbook('data.xlsx').active



for num in range(2, len(ls["A"])):
    value = [data.value for data in ls[num:num]]

    property_address = value[1]
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



    print(property_address)





    selenium_chrome(Bin, value[1], folderName=value[1])
    # print()

    