# from openpyxl import load_workbook
# from requests import get
# from bs4 import BeautifulSoup
# from time import sleep
# from base64 import b64decode

# from webdriver_manager.chrome import ChromeDriverManager
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service as ChromeService
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By

# from PIL import Image
# import io
# import binascii

# from pathlib import Path


# def getDobnow(address):
#     dobnow_url = "https://a810-dobnow.nyc.gov:443/Publish/WrapperPP/PublicPortal.svc/getPublicPortalPropertyDetailsGet/" + address
#     dobnow_cookies = {"_gid": "GA1.2.1832189801.1712661164", "_abck": "959995977197097D415C93950939B293~0~YAAQz4MsMfWjSJmOAQAANSeJ0AvE9bmSo6kKqDlJl4gLpkmS43TJbXNOecHGPwxlaFEEXA261H4+ewJ1eSn/VKjt/vidcAwZuZ+CG4EwV3z/MWHmBEgq+XspAkDTX/d6A8LHCel5OQbo2Ww7kHB61UnfQjNT22nhMk51PdSKC3V+ZoV097ciyhM86xQ0/6cKE5WHCsPMYElLV0+99BNPh3tlRNq7knosuTyH2nPycWcbCwtzsKvr7f9UpwG4p8+uKVivD1DigGoPuMQxxkbqveQLt7dsNnj0Dk7rvEAJO7Ik+aS2swq7M06xaY3D63VSLTVJqlFmY8WQFoqPF88Bd3FweJYskf+0UR4hQRbEc5MBLgNpcfM2lUI9Gk/3kINSpCKhojt9an5sA9NSXPqgT8eSfAX8~-1~-1~-1", "bm_sz": "7152039AFBB2FB8E8D57A6423E4BAB43~YAAQz4MsMWwiSZmOAQAA6ZwX0Rf9I2AToClaw5MQMZsFP2rhZYVtAo37se9ctY64vFaIphNVmTfS25BJxwyEeHzCIhkyZE6YeHGv4C7Ld5/vIybTpR9veZz0muxtf9ReuEVzP54U8iJOf4YFX7XE2+mMsvHME14WiRgYOHgsACXo39r4/8LZIOCIgws77GupqlEm6d+z9azsvHDsZExm8ehrNxt1oJYAojF4c8h2Lgz+k/7Ch0j1EuxWO7kNhHe0ldnSLWzrmFm1aNdGDzb1L8z0AbtOAJbTechhQw3gIVQ4Nv8RuAlOLM1gTM92O2274tyU5o78AulqVE9eVR1YSfe4vtMLJvdZjasqoK2F3ORJoRuLDEAezihanqMD7wUad+V38SDAfoPXDFNXvq8IQ7ztDMra~4468784~3551793", "_ga_863DM8YSJL": "GS1.1.1712904971.13.0.1712904971.0.0.0", "_ga": "GA1.2.792185897.1710760621", "_gat_gtag_UA_128025137_1": "1", "bm_mi": "62999D8ECE4142449096C2403B3BF5CE~YAAQz4MsMX8iSZmOAQAARKsX0RdBJ42PD5k9n9alKnnmXMgMB5dFOeQmCh8o+AE8a2pCY3s5ezpY+Fi+ZxaUA9asadE7UTSW58BgdO2v24MsbEgH/8nwOb0Gpvt657ysszY6sqU8BS/+/Wcfch5PqnN/1l4wPAo6b40DEL5H7gUNU0dwvoY4sklxfwDd3QdevK361teajuPk0SBywS/txCnGnQGYAWAn++vrhCg6Ip5+16N8VceLl+6mI+6sSCTsJN0+Q8ej8O90PMpsghtMJqqj1GUPkwdGLa8YrCgn9kS92W3pMbqYUjHNOp4B4Y2oOKcaOMHYfJqYULiKDb3oCg==~1", "ASP.NET_SessionId": "abew5adcqw2i5ac43li13ybw", "ak_bmsc": "DAE85DE99DFD6CF6B8A6EF97FF74F6FB~000000000000000000000000000000~YAAQz4MsMZUiSZmOAQAASrAX0RendUSns5vBxKjCqlLlR3JLTGUKyd9pHEW2wscN/ONCOd5Xm6e4PrY1Olo+VbhsnRsBbWqAKQ5VKuyq5QELlY05+PY8Z5BCtAlGcC7WLwQsyLczqnNTKnVIiLasM77+89Z9dqXJT7LWVkApE0uysYbejTtrCANK4ZPirDntliW7i/gdfCI02EP2QnweKeWehBb37JqY7dApIJx3Bzm/ZQxJOfjTiz28iwf89vMgxT+meQ0mcx3ZossnM70eb4zo+ZHXugz4micGiPhe0Mhl3yQbawTmP7kxcyApiamNI3N4sco/nu9lamVy68SrNkPCArqvfnf1f95bcU/CYZsEry035doDhprEvFp/RDWyElElSlRNGGhU4dlkZ4afzgXUgRmVeFqydoQ3dZA+k/wrMlI6grU6ohzWIVBcBHLQ5HlKkbmVoTP8fR/BvjPs/HgV617U3p+O8K6Z5tl1SzInOSZKl0NV6lYQQmubP5C7eFPmdGpyng==", "PUNKDDUF": "02ab9cfba6-09e1-43JunnEDKAvnnDr_up1YJopB-SYszidiGqq83MgBtbc-8uWJArnIs79NrTy8T6YJmL1x0", "bm_sv": "1F7C9198E5A3649A57B7FFD88998A9B9~YAAQz4MsMagiSZmOAQAAuOAX0Re7rZLNDldD7B1RjAVxHQmXGtkvUaaqZn5dLPSkY+ELEGJSfG9nbTK70g/RDvdixce9XLRrG29l/tUpFAEeCDQ1pArQa6vVeeUbsohxPzZz2qu+/kiRIxVm/QKY6ExLTPjTEBzcXk+HPgW10qjNQgCnBzpHvYq4FL8vBOzZVntVr+lU7vM91q4K3kodg1zL9swcHKW0x8ZfJ3WjLC7Rm6zAAj9GJDPKnm/K~1"}
#     dodnow_headers = {"Cache-Control": "no-cache", "Sec-Ch-Ua": "\"Chromium\";v=\"123\", \"Not:A-Brand\";v=\"8\"", "Pragma": "no-cache", "Userbrowserid": "GSbuQUTUE6Y/0o9548PZ2A==", "Sec-Ch-Ua-Mobile": "?0", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.6312.88 Safari/537.36", "Authtoken": "rcnKf5MB9mbTB3TIYinSaA==", "Accept": "application/json, text/plain, */*", "If-Modified-Since": "Mon, 26 Jul 1997 05:00:00 GMT", "Sec-Ch-Ua-Platform": "\"Linux\"", "Sec-Fetch-Site": "same-origin", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Dest": "empty", "Referer": "https://a810-dobnow.nyc.gov/publish/Index.html", "Accept-Encoding": "gzip, deflate, br", "Accept-Language": "en-US,en;q=0.9", "Priority": "u=1, i"}
#     dobnow_res = get(dobnow_url, cookies=dobnow_cookies, headers=dodnow_headers).json()
#     PropertyDetails = dobnow_res["PropertyDetails"]
#     return PropertyDetails

# def seleniumChrom(value):

#     return value

# sheet =  load_workbook('./data.xlsx').active


# for num in range(2, 40):

#     select_data = [data.value for data in sheet[num:num]]

#     property_address = select_data[1]
#     door_num = ""
#     street_address = ""

#     for str_ in property_address.split(" "):

#         if str(str_).isnumeric() or str(str_).split("-")[0].isnumeric():
#              door_num =  str_.split("-")[0]
#         else:
#             street_address += str_ + " "

#     suffix_url = "1|" +  door_num + "|" + street_address.strip() + "|1"
#     url_encode_data = suffix_url.replace("|", "%7C").replace(" ", "%20")
#     donow_res =  getDobnow(url_encode_data)
#     Bin =  donow_res["BIN"]
#     sleep(1)

#     for iter in range(0, 4):

#       if iter % 2:
#         seleniumChrom(property_address)
#       else:
#         seleniumChrom(Bin)
#     break


# for num in range(len(data)):
# from os import listdir
# from openpyxl import load_workbook


# for num in range(2, len(ls["A"])):

#     value = [data.value for data in ls[num:num]]

#     print(str(value[1]).strip())
#     print(listdir('./'))

# if str(value[1]) in  listdir('./'):

#     print(value[1])


# load_workbook('./')


# print(data)


import requests
from bs4 import BeautifulSoup
from execjs import compile, eval
from json import dump

# burp0_url = "https://app.dnbhoovers.com:443/api/search/typeAheadQuery"
# burp0_cookies = {"apt.uid": "AP-9APX3RS6VUQK-2-1713015149839-81689821.0.2.60d22e54-36fb-4b36-8774-79ca0dd23452", "OSMACH": "95", "OSPWD": "\"7GMElLPOL4bwNWF1xsN/OouhFNU=\"", "LOGONID": "hsetty@zerocircle.eco", "SITE": "174118818", "USERID": "AV_t7tQp5H7LbIBvpfH", "JSESSIONID": "17EDC06331120623B6B386DA0FEB2409.prd1-l-app04", "GCILB": "\"80596d6da9b2333e\"", "ak_bmsc": "288CEA8DE03C226FBE23B64A778121C8~000000000000000000000000000000~YAAQ7ulUuIKq98uOAQAAN3Kq2hco/a20zeHdjRQdwYSYOyeKiGHPR6wRYcqXb+RcR73KcvZZjNqO6ZvYyHRXbK201+RuPm/mI9epYuhiBwTtnRbom1DKUP9Eoy9CF7DdNJsUERnWCGe5mpvQzd/VM8/enhQy/0TT3gGDm30A3RCRZhbOmqqCMaQ+FzBk48edEQiFor51mcd84v86w3jU2ylUOP97sn2hLFoyniZj+H6X3Jyc1AhvbOodEO4v7lr6jOFzcEuYk2Wjoari/87rPMqF1QO8Tbk9OTy5/3q6pRiVJVOmAB349hsQO6tIkm/YqWsLdEfd2wEMf0jMwfGO216muGVg6XSGTRVkRpSpbqR61ffhHsrLdt9Sw1WaxSdbRbUk5OvFDqS27dCvRA==",
#                  "bm_sv": "DE3E0561ACBD786AC94A765D3BF5C563~YAAQ7ulUuIK998uOAQAA+ZOu2hdRSyF5b3mPTehSuMkdHFEdTv3IQy8RSMBBDUT+hz1m0AYkttR0ia/TD+AgUiH7VkYSKtxB0JYLusNWzRZOPqkQH6EiocQaNgAsV5ePQrI+UmEuNSAHR471zBQ3bchc8ByBix2U2VaImn/W/S0/wA8qWbkTQlS+VtRe9J+e4YAye+Ycuv7q3IN3b4EdkQaf2BED/KnG1SgmgfqTSeiGBCOMpDRTDFUCZQgfDCMqVhySNQA=~1", "apt.sid": "AP-9APX3RS6VUQK-2-1713065589987-86658321", "ext_id": "EIHUXI3JXNZNYO5QC3VRJHI1MP5PPGYZ"}
# burp0_headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:124.0) Gecko/20100101 Firefox/124.0", "Accept": "*/*", "Accept-Language": "en-US,en;q=0.5", "Accept-Encoding": "gzip, deflate, br",
#                  "Referer": "https://app.dnbhoovers.com/company/d5278353-e7a0-3020-ae7f-bc5ae6f5a036", "Content-Type": "application/json", "Origin": "https://app.dnbhoovers.com", "Sec-Fetch-Dest": "empty", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Site": "same-origin", "Te": "trailers"}
# burp0_json = {"primitives": ["company"], "query": "HRC Corporation"}
# data = requests.post(burp0_url, headers=burp0_headers,
#                      cookies=burp0_cookies, json=burp0_json).json()

# id = data['company']['searchResults']['results'][0]['id']


# burp0_url = "https://app.dnbhoovers.com:443/company/" + id
# burp0_cookies = {"apt.uid": "AP-9APX3RS6VUQK-2-1713015149839-81689821.0.2.60d22e54-36fb-4b36-8774-79ca0dd23452", "OSMACH": "95", "OSPWD": "\"7GMElLPOL4bwNWF1xsN/OouhFNU=\"", "LOGONID": "hsetty@zerocircle.eco", "SITE": "174118818", "USERID": "AV_t7tQp5H7LbIBvpfH", "JSESSIONID": "17EDC06331120623B6B386DA0FEB2409.prd1-l-app04", "GCILB": "\"80596d6da9b2333e\"", "ak_bmsc": "288CEA8DE03C226FBE23B64A778121C8~000000000000000000000000000000~YAAQ7ulUuIKq98uOAQAAN3Kq2hco/a20zeHdjRQdwYSYOyeKiGHPR6wRYcqXb+RcR73KcvZZjNqO6ZvYyHRXbK201+RuPm/mI9epYuhiBwTtnRbom1DKUP9Eoy9CF7DdNJsUERnWCGe5mpvQzd/VM8/enhQy/0TT3gGDm30A3RCRZhbOmqqCMaQ+FzBk48edEQiFor51mcd84v86w3jU2ylUOP97sn2hLFoyniZj+H6X3Jyc1AhvbOodEO4v7lr6jOFzcEuYk2Wjoari/87rPMqF1QO8Tbk9OTy5/3q6pRiVJVOmAB349hsQO6tIkm/YqWsLdEfd2wEMf0jMwfGO216muGVg6XSGTRVkRpSpbqR61ffhHsrLdt9Sw1WaxSdbRbUk5OvFDqS27dCvRA==",
#                  "bm_sv": "DE3E0561ACBD786AC94A765D3BF5C563~YAAQ7ulUuDG/98uOAQAARuWu2hcDpDml74u15hsQZ3s6iJyGPsHLhEB0OmUtSVx2HvpY8BTXZqEe88uL4+mll0lXzMz5/vbj4Tn8F78ifctqF/jIGSXPBGsy+qzczWZ5ewpnYMTtVFA2BtySOpmX1M96NbYl3956MNdoXn02wYQXchb1jua7E7hvloJ0dt3B9kgiimzbTQ8UvdHmofRSKOoHjFvKtyqQpuLdPXtrmYbG05/KFB57GCFC673jMFNhxdqXKFc=~1", "apt.sid": "AP-9APX3RS6VUQK-2-1713065589987-86658321", "ext_id": "EIHUXI3JXNZNYO5QC3VRJHI1MP5PPGYZ"}
# burp0_headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:124.0) Gecko/20100101 Firefox/124.0", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8", "Accept-Language": "en-US,en;q=0.5", "Accept-Encoding": "gzip, deflate, br",
#                  "Referer": "https://app.dnbhoovers.com/company/d5278353-e7a0-3020-ae7f-bc5ae6f5a036", "Upgrade-Insecure-Requests": "1", "Sec-Fetch-Dest": "document", "Sec-Fetch-Mode": "navigate", "Sec-Fetch-Site": "same-origin", "Sec-Fetch-User": "?1", "Te": "trailers"}
# data = requests.get(burp0_url, headers=burp0_headers,
#                     cookies=burp0_cookies).text

# soup = BeautifulSoup(data, 'html.parser').find(
#     'script', {'id': "PrimitiveJson"})
# ctx = compile(soup.text)
# res = ctx.eval("initialLoad")

# with open('data.json', 'w') as f:
#     dump(res, f)


# burp0_url = "https://app.dnbhoovers.com:443/api/search"
# burp0_cookies = {"apt.uid": "AP-9APX3RS6VUQK-2-1713015149839-81689821.0.2.60d22e54-36fb-4b36-8774-79ca0dd23452", "OSMACH": "95", "OSPWD": "\"7GMElLPOL4bwNWF1xsN/OouhFNU=\"", "LOGONID": "hsetty@zerocircle.eco", "SITE": "174118818", "USERID": "AV_t7tQp5H7LbIBvpfH", "JSESSIONID": "17EDC06331120623B6B386DA0FEB2409.prd1-l-app04", "GCILB": "\"80596d6da9b2333e\"", "ak_bmsc": "288CEA8DE03C226FBE23B64A778121C8~000000000000000000000000000000~YAAQ7ulUuIKq98uOAQAAN3Kq2hco/a20zeHdjRQdwYSYOyeKiGHPR6wRYcqXb+RcR73KcvZZjNqO6ZvYyHRXbK201+RuPm/mI9epYuhiBwTtnRbom1DKUP9Eoy9CF7DdNJsUERnWCGe5mpvQzd/VM8/enhQy/0TT3gGDm30A3RCRZhbOmqqCMaQ+FzBk48edEQiFor51mcd84v86w3jU2ylUOP97sn2hLFoyniZj+H6X3Jyc1AhvbOodEO4v7lr6jOFzcEuYk2Wjoari/87rPMqF1QO8Tbk9OTy5/3q6pRiVJVOmAB349hsQO6tIkm/YqWsLdEfd2wEMf0jMwfGO216muGVg6XSGTRVkRpSpbqR61ffhHsrLdt9Sw1WaxSdbRbUk5OvFDqS27dCvRA==",
#                  "bm_sv": "DE3E0561ACBD786AC94A765D3BF5C563~YAAQ7ulUuCz898uOAQAAzSy42hfXaOIfaNhkYORW8k3DoXQEXMEN/Ow1SYgSXHnC2UAqnaQAI53F7pm2fX8vPhYqAokwNsYh2kaD1mQA67MzgT2rqwjHn1BYEHrs/r8UvOOGR9X1VYTVPOBnY7bbY+XLeRnieVM/PTy79sz7+O+SpwUdn/c8YC/nl5azW0e4K5leYV0A3hJecH4ZNkoepgnt0zrZUYYnceBMR5oI26m6r8umkksNY7kPQ0m1S3GJeh67xxc=~1", "apt.sid": "AP-9APX3RS6VUQK-2-1713065589987-86658321", "ext_id": "EIHUXI3JXNZNYO5QC3VRJHI1MP5PPGYZ"}
# burp0_headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:124.0) Gecko/20100101 Firefox/124.0", "Accept": "*/*", "Accept-Language": "en-US,en;q=0.5", "Accept-Encoding": "gzip, deflate, br",
#                  "Referer": "https://app.dnbhoovers.com/company/d5278353-e7a0-3020-ae7f-bc5ae6f5a036", "Content-Type": "application/json", "Origin": "https://app.dnbhoovers.com", "Sec-Fetch-Dest": "empty", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Site": "same-origin", "Te": "trailers"}
# burp0_json = {"aggs": {"contactCompanyCount": {}}, "filters": [{"contactCompanyIdFacet": {"exclude": False, "label": "Contact Companies", "type": "", "valueLabels": ["HRC Corporation"], "values": [
#     "d5278353-e7a0-3020-ae7f-bc5ae6f5a036"]}}], "from": 0, "query": "", "searchWeight": 0, "size": 25, "sortBy": [{"contact": [{"CONTACT_LEVEL": "asc"}]}], "types": ["contact"], "valueLabels": {id: "HRC Corporation"}, "version": 2}
# res = requests.post(burp0_url, headers=burp0_headers,
#                     cookies=burp0_cookies, json=burp0_json).json()


# with open('response.json', 'w') as f:
#     dump(res, f)

# import requests

# burp0_url = "https://app.dnbhoovers.com:443/api/search/typeAheadQuery"
# burp0_cookies = {"apt.uid": "AP-9APX3RS6VUQK-2-1713015149839-81689821.0.2.60d22e54-36fb-4b36-8774-79ca0dd23452", "OSMACH": "95", "OSPWD": "\"7GMElLPOL4bwNWF1xsN/OouhFNU=\"", "LOGONID": "hsetty@zerocircle.eco", "SITE": "174118818", "USERID": "AV_t7tQp5H7LbIBvpfH", "ak_bmsc": "288CEA8DE03C226FBE23B64A778121C8~000000000000000000000000000000~YAAQ7ulUuIKq98uOAQAAN3Kq2hco/a20zeHdjRQdwYSYOyeKiGHPR6wRYcqXb+RcR73KcvZZjNqO6ZvYyHRXbK201+RuPm/mI9epYuhiBwTtnRbom1DKUP9Eoy9CF7DdNJsUERnWCGe5mpvQzd/VM8/enhQy/0TT3gGDm30A3RCRZhbOmqqCMaQ+FzBk48edEQiFor51mcd84v86w3jU2ylUOP97sn2hLFoyniZj+H6X3Jyc1AhvbOodEO4v7lr6jOFzcEuYk2Wjoari/87rPMqF1QO8Tbk9OTy5/3q6pRiVJVOmAB349hsQO6tIkm/YqWsLdEfd2wEMf0jMwfGO216muGVg6XSGTRVkRpSpbqR61ffhHsrLdt9Sw1WaxSdbRbUk5OvFDqS27dCvRA==",
#                  "bm_sv": "DE3E0561ACBD786AC94A765D3BF5C563~YAAQpi3fF8/ytMqOAQAAus8X2xfBXUWUfZsjI/kVKRBOn624DZjFZaommzjRor6HYzOIT7jp4X7lBGA3pIffbJ9vpTXJpBe5VZW4Bbz/SafBuVGaRThRehsLIGOKSv+14q0wVyBY73firLHxZ/7I0H3wWBRrvJ2sWFuJ6+g7t+wP7EIiu7nLhDDnMG07KP+fdS71bWzAOIWGZzLcEiPiZiqCvwd2XIPh+PERFatsi4AhYPkt/65alMI6UZzv9d85m3IQNJs=~1", "ext_id": "H4UKRSYIS2F3DHEMZZBMYAET4LNEXZAW", "GCILB": "\"0c9a142d7f887454\"", "JSESSIONID": "F8DFE9CF3D67F5A29C3F1D1564D248C6.prd1-l-app01", "apt.sid": "AP-9APX3RS6VUQK-2-1713072713281-97596691"}
# burp0_headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:124.0) Gecko/20100101 Firefox/124.0", "Accept": "*/*", "Accept-Language": "en-US,en;q=0.5", "Accept-Encoding": "gzip, deflate, br",
#                  "Referer": "https://app.dnbhoovers.com/company/a72f0578-f414-3042-ae6c-9c988c020c70", "Content-Type": "application/json", "Origin": "https://app.dnbhoovers.com", "Sec-Fetch-Dest": "empty", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Site": "same-origin", "Te": "trailers"}
# burp0_json = {"primitives": ["company"], "query": "Walter & Samuels, Inc."}
# data = requests.post(burp0_url, headers=burp0_headers,
#                      cookies=burp0_cookies, json=burp0_json).json()
# id = data['company']['searchResults']['results'][0]['id']


# burp0_url = "https://app.dnbhoovers.com:443/company/" + id
# burp0_cookies = {"apt.uid": "AP-9APX3RS6VUQK-2-1713015149839-81689821.0.2.60d22e54-36fb-4b36-8774-79ca0dd23452", "OSMACH": "95", "OSPWD": "\"7GMElLPOL4bwNWF1xsN/OouhFNU=\"", "LOGONID": "hsetty@zerocircle.eco", "SITE": "174118818", "USERID": "AV_t7tQp5H7LbIBvpfH", "ak_bmsc": "288CEA8DE03C226FBE23B64A778121C8~000000000000000000000000000000~YAAQ7ulUuIKq98uOAQAAN3Kq2hco/a20zeHdjRQdwYSYOyeKiGHPR6wRYcqXb+RcR73KcvZZjNqO6ZvYyHRXbK201+RuPm/mI9epYuhiBwTtnRbom1DKUP9Eoy9CF7DdNJsUERnWCGe5mpvQzd/VM8/enhQy/0TT3gGDm30A3RCRZhbOmqqCMaQ+FzBk48edEQiFor51mcd84v86w3jU2ylUOP97sn2hLFoyniZj+H6X3Jyc1AhvbOodEO4v7lr6jOFzcEuYk2Wjoari/87rPMqF1QO8Tbk9OTy5/3q6pRiVJVOmAB349hsQO6tIkm/YqWsLdEfd2wEMf0jMwfGO216muGVg6XSGTRVkRpSpbqR61ffhHsrLdt9Sw1WaxSdbRbUk5OvFDqS27dCvRA==",
#                  "bm_sv": "DE3E0561ACBD786AC94A765D3BF5C563~YAAQpi3fFxL1tMqOAQAAj/wX2xcnnaHN6hnbpIiLg4+PnCPJ224Tm5csI7mnVcYIeOf8FDKSdLR+iv2kDLVSRTNnA1vP8b12SWcsrh0lb68f4y/9LlRJWJLsL1ohMEWYPzx5vbAFq8mVaM9ebEJGxR+cikjzahD69s7eueJKA6YDqDMGC6JqA9gn7Ju3rcQcr2STDYxXMQOJcCCcGMAMbY8mQ763wnyZuSnqj3r0daDIoSugyh9sEROAWTnidpAUC9yVLpY=~1", "ext_id": "H4UKRSYIS2F3DHEMZZBMYAET4LNEXZAW", "GCILB": "\"0c9a142d7f887454\"", "JSESSIONID": "F8DFE9CF3D67F5A29C3F1D1564D248C6.prd1-l-app01", "apt.sid": "AP-9APX3RS6VUQK-2-1713072713281-97596691"}
# burp0_headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:124.0) Gecko/20100101 Firefox/124.0", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8", "Accept-Language": "en-US,en;q=0.5", "Accept-Encoding": "gzip, deflate, br",
#                  "Referer": "https://app.dnbhoovers.com/company/a72f0578-f414-3042-ae6c-9c988c020c70", "Upgrade-Insecure-Requests": "1", "Sec-Fetch-Dest": "document", "Sec-Fetch-Mode": "navigate", "Sec-Fetch-Site": "same-origin", "Sec-Fetch-User": "?1", "Te": "trailers"}
# data = requests.get(burp0_url, headers=burp0_headers,
#                     cookies=burp0_cookies).text

# soup = BeautifulSoup(data, 'html.parser').find(
#     'script', {'id': "PrimitiveJson"})
# ctx = compile(soup.text)
# res = ctx.eval("initialLoad")


# with open('res_data.json', 'w') as f:
#     dump(res, f)


# soup = BeautifulSoup(data, 'html.parser').find(
#     'script', {'id': "PrimitiveJson"})
# ctx = compile(soup.text)
# res = ctx.eval("initialLoad")

from json import load

# f = open('data.json')

# data = load(f)

# selectd_data = data["primitiveDetails"]['primitive']

# company = selectd_data["companyName"]
# phone = selectd_data["phone"]
# address = selectd_data["addresses"][0]
# res_address = address["address1"] + ", " + \
#     address["city"] + ", " + address["postalCode"]
# ultimateParentDunsNumber = selectd_data["ultimateParentDunsNumber"]
# latitude = address["latitude"]
# longitude = address["longitude"]
# industries = selectd_data["industries"]
# yearFounded = selectd_data["yearFounded"]


# for data in industries:

#     if data["industry"]:

#         print(data["industry"]["source"])
#         print(data["industry"]["code"] + data["industry"]["shortDescription"])

# county = address["county"]["name"]
# ultimateParentDunsNumber = selectd_data["ultimateParentDunsNumber"]
# domesticUltimateParent = selectd_data["domesticUltimateParent"]['dunsNumber']
# print(selectd_data)

# f = open('response.json')
# data = load(f)

# selectd_data = data["searchResults"]["results"]

# for data in selectd_data:

#     print(data["firstName"])
#     print(data["lastName"])
#     print(data["title"])
#     print(data["linkedInPublicProfileUrl"])
#     print(data["company"]["phone"])

data = [['compnay name', 'Walter & Samuels, Incorporated'], ['phone', '+1-212-696-7100'], ['addrss', '419 Park Ave S FL 15, New York, 10016-8437', 'Walter & Samuels, Incorporated'], ['ultimateParentDunsNumber', '968338525'], ['latitude', 40.743727], ['longitude', -73.98355], ['industries', [{'isPrimary': True, 'industry': {}}, {'isPrimary': False, 'industry': {'id': '0cb13de4-9dde-35b6-98cc-e68153aaa0c9', 'source': 'ANZSIC', 'code': '3020', 'sicCodeId': 4666000, 'shortDescription': 'Non-Residential Building Construction', 'reportsAvailable': {'industry_analysts': '1', 'industry_latest_news_stories': '1', 'industry_firstresearch': '0', 'industry_related': '0', 'industry_family': '0', 'industry_market_share': '0', 'industry_activities': '1', 'industry_summary': '1', 'industry_all_market_research': '1', 'industry_peer': '1', 'industry_stat_usa': '1', 'industry_related_sites': '1', 'industry_freedonia_focus': '1', 'industry_bmi': '1', 'industry_snapshot': '0', 'industry_euromonitor': '0', 'industry_emd_industry': '0', 'industry_rma_norms': '0', 'industry_market_line_profile': '1'}}}, {'isPrimary': False, 'industry': {'id': 'effdedb6-bf90-3755-af0a-91e6c8a24da5', 'source': 'GDSSIC', 'code': '15420000', 'sicCodeId': 95001519, 'shortDescription': 'Nonresidential construction, nec', 'reportsAvailable': {'industry_analysts': '1', 'industry_latest_news_stories': '1', 'industry_firstresearch': '1', 'industry_related': '0', 'industry_family': '0', 'industry_market_share': '0', 'industry_activities': '0', 'industry_summary': '1', 'industry_all_market_research': '0', 'industry_peer': '1', 'industry_stat_usa': '0', 'industry_related_sites': '1', 'industry_freedonia_focus': '0', 'industry_bmi': '0', 'industry_snapshot': '0', 'industry_euromonitor': '0', 'industry_emd_industry': '0', 'industry_rma_norms': '0', 'industry_market_line_profile': '0'}}}, {'isPrimary': False, 'industry': {}}, {'isPrimary': False, 'industry': {}}, {'isPrimary': False, 'industry': {'id': 'c428574f-fbde-3937-a3a7-bd7f02ca3f63', 'source': 'NAICS2017', 'code': '236220', 'sicCodeId': 96000217, 'shortDescription': 'Commercial and Institutional Building Construction', 'reportsAvailable': {'industry_analysts': '1', 'industry_latest_news_stories': '1', 'industry_firstresearch': '0', 'industry_related': '0', 'industry_family': '0', 'industry_market_share': '0', 'industry_activities': '0', 'industry_summary': '1', 'industry_all_market_research': '1', 'industry_peer': '1', 'industry_stat_usa': '0', 'industry_related_sites': '1', 'industry_freedonia_focus': '1', 'industry_bmi': '1', 'industry_snapshot': '0', 'industry_euromonitor': '0', 'industry_emd_industry': '0', 'industry_rma_norms': '1', 'industry_market_line_profile': '0'}}}, {'isPrimary': False, 'industry': {'id': 'a97c5944-53ed-39e8-98a1-605244b97394', 'source': 'NAICS2022', 'code': '236220', 'sicCodeId': 96030209, 'shortDescription': 'Commercial and Institutional Building Construction', 'reportsAvailable': {'industry_analysts': '0', 'industry_latest_news_stories': '0', 'industry_firstresearch': '0', 'industry_related': '0', 'industry_family': '0', 'industry_market_share': '0', 'industry_activities': '1', 'industry_summary': '1', 'industry_all_market_research': '1', 'industry_peer': '0', 'industry_stat_usa': '1', 'industry_related_sites': '0', 'industry_freedonia_focus': '1', 'industry_bmi': '0', 'industry_snapshot': '0', 'industry_euromonitor': '0', 'industry_emd_industry': '0', 'industry_rma_norms': '1', 'industry_market_line_profile': '1'}}}, {'isPrimary': False, 'industry': {'id': '0c824eef-8c00-34ac-a601-a322f5215f2a', 'source': 'UK2007', 'code': '41201', 'sicCodeId': 60000525, 'shortDescription': 'Construction of commercial buildings', 'reportsAvailable': {'industry_analysts': '1', 'industry_latest_news_stories': '1', 'industry_firstresearch': '0', 'industry_related': '0', 'industry_family': '0', 'industry_market_share': '0', 'industry_activities': '1', 'industry_summary': '1', 'industry_all_market_research': '1', 'industry_peer': '1', 'industry_stat_usa': '1', 'industry_related_sites': '1', 'industry_freedonia_focus': '1', 'industry_bmi': '1', 'industry_snapshot': '0', 'industry_euromonitor': '0', 'industry_emd_industry': '0', 'industry_rma_norms': '0', 'industry_market_line_profile': '1'}}}, {'isPrimary': False, 'industry': {'id': 'a6eafef8-dc20-30dc-ab53-960329cc3039', 'source': 'US87', 'code': '1542', 'sicCodeId': 194727, 'shortDescription': 'General Contractors-Nonresidential Buildings, Other than Industrial Buildings and Warehouses', 'reportsAvailable': {'industry_analysts': '1', 'industry_latest_news_stories': '1', 'industry_firstresearch': '0', 'industry_related': '0', 'industry_family': '0', 'industry_market_share': '0', 'industry_activities': '1', 'industry_summary': '1', 'industry_all_market_research': '1', 'industry_peer': '1', 'industry_stat_usa': '0', 'industry_related_sites': '1', 'industry_freedonia_focus': '1', 'industry_bmi': '1', 'industry_snapshot': '0', 'industry_euromonitor': '0', 'industry_emd_industry': '0', 'industry_rma_norms': '1', 'industry_market_line_profile': '1'}}}, {'isPrimary': True, 'industry': {'id': '317cea18-16aa-3045-9553-9213c59c1752', 'source': 'ANZSIC', 'code': '3019', 'sicCodeId': 4665800, 'shortDescription': 'Other Residential Building Construction', 'reportsAvailable': {'industry_analysts': '1', 'industry_latest_news_stories': '1', 'industry_firstresearch': '0', 'industry_related': '0', 'industry_family': '0', 'industry_market_share': '0', 'industry_activities': '1', 'industry_summary': '1', 'industry_all_market_research': '1', 'industry_peer': '1', 'industry_stat_usa': '1', 'industry_related_sites': '1', 'industry_freedonia_focus': '1', 'industry_bmi': '1', 'industry_snapshot': '0', 'industry_euromonitor': '0', 'industry_emd_industry': '0', 'industry_rma_norms': '0', 'industry_market_line_profile': '1'}}}, {'isPrimary': True, 'industry': {'id': '89031c07-2bcf-3247-89e7-a98ea7317813', 'source': 'GDSSIC', 'code': '15220000', 'sicCodeId': 95001472, 'shortDescription': 'Residential construction, nec', 'reportsAvailable': {'industry_analysts': '1', 'industry_latest_news_stories': '1', 'industry_firstresearch': '1', 'industry_related': '0', 'industry_family': '0', 'industry_market_share': '0', 'industry_activities': '0', 'industry_summary': '1', 'industry_all_market_research': '0', 'industry_peer': '1', 'industry_stat_usa': '0', 'industry_related_sites': '1', 'industry_freedonia_focus': '0', 'industry_bmi': '0', 'industry_snapshot': '0', 'industry_euromonitor': '0', 'industry_emd_industry': '0', 'industry_rma_norms': '0', 'industry_market_line_profile': '0'}}}, {'isPrimary': True, 'industry': {'id': '09748b18-3a1d-39fa-b543-91dd5c4b3de1', 'source': 'ISICRev4', 'code': '4100', 'sicCodeId': 92000342, 'shortDescription': 'Construction of buildings', 'reportsAvailable': {'industry_analysts': '1', 'industry_latest_news_stories': '1', 'industry_firstresearch': '0', 'industry_related': '0', 'industry_family': '0', 'industry_market_share': '0', 'industry_activities': '1', 'industry_summary': '1', 'industry_all_market_research': '1', 'industry_peer': '1', 'industry_stat_usa': '1', 'industry_related_sites': '1', 'industry_freedonia_focus': '1', 'industry_bmi': '1', 'industry_snapshot': '0', 'industry_euromonitor': '0', 'industry_emd_industry': '0', 'industry_rma_norms': '0', 'industry_market_line_profile': '1'}}}, {'isPrimary': True, 'industry': {}}, {'isPrimary': True, 'industry': {'id': '60340612-a7fc-3ab3-a445-2908cdacfa3e', 'source': 'NACERev2', 'code': '4120', 'sicCodeId': 93000469, 'shortDescription': 'Construction of buildings', 'reportsAvailable': {'industry_analysts': '1', 'industry_latest_news_stories': '1', 'industry_firstresearch': '0', 'industry_related': '0', 'industry_family': '0', 'industry_market_share': '0', 'industry_activities': '1', 'industry_summary': '1', 'industry_all_market_research': '1', 'industry_peer': '1', 'industry_stat_usa': '1', 'industry_related_sites': '1', 'industry_freedonia_focus': '1', 'industry_bmi': '1', 'industry_snapshot': '0', 'industry_euromonitor': '0', 'industry_emd_industry': '0', 'industry_rma_norms': '0', 'industry_market_line_profile': '1'}}}, {'isPrimary': True, 'industry': {}}, {'isPrimary': True, 'industry': {}}, {'isPrimary': True, 'industry': {
    'id': '2de29ce2-59be-3c2f-8410-50a5c090f7ad', 'source': 'NAICS2017', 'code': '236116', 'sicCodeId': 96000210, 'shortDescription': 'New Multifamily Housing Construction (except For-Sale Builders)', 'reportsAvailable': {'industry_analysts': '1', 'industry_latest_news_stories': '1', 'industry_firstresearch': '0', 'industry_related': '0', 'industry_family': '0', 'industry_market_share': '0', 'industry_activities': '0', 'industry_summary': '1', 'industry_all_market_research': '1', 'industry_peer': '1', 'industry_stat_usa': '1', 'industry_related_sites': '1', 'industry_freedonia_focus': '1', 'industry_bmi': '1', 'industry_snapshot': '0', 'industry_euromonitor': '0', 'industry_emd_industry': '0', 'industry_rma_norms': '1', 'industry_market_line_profile': '1'}}}, {'isPrimary': True, 'industry': {'id': 'a5a2dcae-58fd-3b57-aa27-2f210aa65beb', 'source': 'NAICS2022', 'code': '236116', 'sicCodeId': 96030202, 'shortDescription': 'New Multifamily Housing Construction (except For-Sale Builders)', 'reportsAvailable': {'industry_analysts': '0', 'industry_latest_news_stories': '0', 'industry_firstresearch': '0', 'industry_related': '0', 'industry_family': '0', 'industry_market_share': '0', 'industry_activities': '1', 'industry_summary': '1', 'industry_all_market_research': '1', 'industry_peer': '0', 'industry_stat_usa': '1', 'industry_related_sites': '0', 'industry_freedonia_focus': '1', 'industry_bmi': '0', 'industry_snapshot': '0', 'industry_euromonitor': '0', 'industry_emd_industry': '0', 'industry_rma_norms': '1', 'industry_market_line_profile': '1'}}}, {'isPrimary': True, 'industry': {'id': '8f1f30d8-1753-31df-86a8-da1ec1ca9c1f', 'source': 'UK2003', 'code': '45212', 'sicCodeId': 51458634, 'shortDescription': 'Construction of domestic buildings', 'reportsAvailable': {'industry_analysts': '1', 'industry_latest_news_stories': '1', 'industry_firstresearch': '0', 'industry_related': '0', 'industry_family': '0', 'industry_market_share': '0', 'industry_activities': '1', 'industry_summary': '1', 'industry_all_market_research': '1', 'industry_peer': '1', 'industry_stat_usa': '1', 'industry_related_sites': '1', 'industry_freedonia_focus': '1', 'industry_bmi': '1', 'industry_snapshot': '0', 'industry_euromonitor': '0', 'industry_emd_industry': '0', 'industry_rma_norms': '0', 'industry_market_line_profile': '1'}}}, {'isPrimary': True, 'industry': {'id': '4fc7fb81-f173-3a33-97d7-f76e089af3f2', 'source': 'UK2007', 'code': '41202', 'sicCodeId': 60000526, 'shortDescription': 'Construction of domestic buildings', 'reportsAvailable': {'industry_analysts': '1', 'industry_latest_news_stories': '1', 'industry_firstresearch': '0', 'industry_related': '0', 'industry_family': '0', 'industry_market_share': '0', 'industry_activities': '1', 'industry_summary': '1', 'industry_all_market_research': '1', 'industry_peer': '1', 'industry_stat_usa': '1', 'industry_related_sites': '1', 'industry_freedonia_focus': '1', 'industry_bmi': '1', 'industry_snapshot': '0', 'industry_euromonitor': '0', 'industry_emd_industry': '0', 'industry_rma_norms': '0', 'industry_market_line_profile': '1'}}}, {'isPrimary': True, 'industry': {'id': 'ca9a038c-51a7-3591-86fd-dd479e88c007', 'source': 'US87', 'code': '1522', 'sicCodeId': 194724, 'shortDescription': 'General Contractors-Residential Buildings, Other Than Single-Family', 'reportsAvailable': {'industry_analysts': '1', 'industry_latest_news_stories': '1', 'industry_firstresearch': '0', 'industry_related': '0', 'industry_family': '0', 'industry_market_share': '0', 'industry_activities': '1', 'industry_summary': '1', 'industry_all_market_research': '1', 'industry_peer': '1', 'industry_stat_usa': '1', 'industry_related_sites': '1', 'industry_freedonia_focus': '1', 'industry_bmi': '1', 'industry_snapshot': '0', 'industry_euromonitor': '0', 'industry_emd_industry': '0', 'industry_rma_norms': '1', 'industry_market_line_profile': '1'}}}]], ['yearFounded', 1933], ['ANZSIC', '3020Non-Residential Building Construction'], ['GDSSIC', '15420000Nonresidential construction, nec'], ['NAICS2017', '236220Commercial and Institutional Building Construction'], ['NAICS2022', '236220Commercial and Institutional Building Construction'], ['UK2007', '41201Construction of commercial buildings'], ['US87', '1542General Contractors-Nonresidential Buildings, Other than Industrial Buildings and Warehouses'], ['ANZSIC', '3019Other Residential Building Construction'], ['GDSSIC', '15220000Residential construction, nec'], ['ISICRev4', '4100Construction of buildings'], ['NACERev2', '4120Construction of buildings'], ['NAICS2017', '236116New Multifamily Housing Construction (except For-Sale Builders)'], ['NAICS2022', '236116New Multifamily Housing Construction (except For-Sale Builders)'], ['UK2003', '45212Construction of domestic buildings'], ['UK2007', '41202Construction of domestic buildings'], ['US87', '1522General Contractors-Residential Buildings, Other Than Single-Family'], ['county', 'New York'], ['ultimateParentDunsNumber', '968338525'], ['domesticUltimateParent', '968338525']] + [['fullName', 'Anthony Builder'], ['job title', 'Managing Director'], ['linked url', 'https://www.linkedin.com/in/anthony-builder-64768683'], ['phone', '+1-212-696-7100'], ['fullName', 'Justin Gentile'], ['job title', 'Director Of Leasing'], ['linked url', 'https://www.linkedin.com/in/justin-gentile-0a0126189'], ['phone', '+1-212-696-7100'], ['fullName', 'Mark Torre'], ['job title', 'Co-Director of Management'], ['linked url', 'https://www.linkedin.com/in/mark-torre-3654434a'], ['phone', '+1-212-696-7100'], ['fullName', 'Joseph Friedman'], ['job title', 'Senior Managing Director'], ['linked url', 'https://www.linkedin.com/in/joseph-friedman-91a28823a'], ['phone', '+1-212-696-7100'], ['fullName', 'Annette Patane'], ['job title', 'Office Manager'], ['linked url', 'https://www.linkedin.com/in/annette-patane-48380abb'], ['phone', '+1-212-696-7100'], ['fullName', 'Francisco Marquez'], ['job title', 'Marketing Coordinator Associate'], ['linked url', 'https://www.linkedin.com/in/francisco-marquez-b2733632'], ['phone', '+1-212-696-7100'], ['fullName', 'Leslie Croft'], ['job title', 'Executive Assistant To The Chairman'], ['linked url', 'https://www.linkedin.com/in/leslie-croft-b7b5108'], ['phone', '+1-212-696-7100'], ['fullName', 'Colette Dublin'], ['job title', 'Lease Administrator'], ['linked url', 'https://www.linkedin.com/in/colette-dublin-89258a64'], ['phone', '+1-212-696-7100'], ['fullName', 'Francesco Rando'], ['job title', 'Chief Engineer'], ['linked url', 'https://www.linkedin.com/in/francesco-g-rando-6a6614b'], ['phone', '+1-212-696-7100'], ['fullName', 'Matthew Lombardi'], ['job title', 'Real Estate Financial Analyst'], ['linked url', 'https://www.linkedin.com/in/matthew-l-lombardi'], ['phone', '+1-212-696-7100'], ['fullName', 'Joseph Urban'], ['job title', 'Operations Mgr'], ['linked url', 'https://www.linkedin.com/in/joseph-urban-550a3a82'], ['phone', '+1-212-696-7100'], ['fullName', 'Greg Sandler'], ['job title', 'Associate Director Of Leasing'], ['linked url', 'https://www.linkedin.com/in/greg-sandler-59152954'], ['phone', '+1-212-696-7100'], ['fullName', 'Brian Sobie'], ['job title', 'Property Supervisor'], ['linked url', 'https://www.linkedin.com/in/brian-sobie-59b7bba'], ['phone', '+1-212-696-7100'], ['fullName', 'Yesenia Mantuano'], ['job title', 'Payroll Administrator'], ['linked url', 'https://www.linkedin.com/in/yesenia-mantuano-301363b0'], ['phone', '+1-212-696-7100'], ['fullName', 'Anacarmen Opran'], ['job title', 'Controller'], ['linked url', 'https://www.linkedin.com/in/ana-carmen-opran-8a747933'], ['phone', '+1-212-696-7100'], ['fullName', 'Jeremiah Griffin'], ['job title', 'Vice President'], ['linked url', 'https://www.linkedin.com/in/jeremiah-griffin-561878186'], ['phone', '+1-212-696-7100'], ['fullName', 'Grzegorz Budny'], ['job title', 'Building Superintendent'], ['linked url', 'https://www.linkedin.com/in/grzegorz-budny-607a815a'], ['phone', '+1-212-696-7100'], ['fullName', 'Gigi Goranic'], ['job title', 'Vp Residential Sales & Rentals'], ['linked url', ''], ['phone', '+1-212-696-7100'], ['fullName', 'Steven Forest'], ['job title', 'Senior Executive Managing Director'], ['linked url', ''], ['phone', '+1-212-696-7100'], ['fullName', 'Mel Farrell'], ['job title', 'Co-Director of Management'], ['linked url', ''], ['phone', '+1-212-696-7100'], ['fullName', 'Helen Cosme'], ['job title', 'Management Supervisor'], ['linked url', ''], ['phone', '+1-212-696-7100'], ['fullName', 'Bill Bottorff'], ['job title', 'Marketing And Sales Manager'], ['linked url', ''], ['phone', '+1-212-696-7100'], ['fullName', 'Alexander Mccarty'], ['job title', 'Management Supervisor'], ['linked url', ''], ['phone', '+1-212-696-7100'], ['fullName', 'Beulah Babulal'], ['job title', 'Transportation Executive'], ['linked url', ''], ['phone', '+1-212-696-7100'], ['fullName', 'Sauda Briganti'], ['job title', 'Management Coordinator'], ['linked url', 'https://www.linkedin.com/in/suada-briganti-51432312'], ['phone', '+1-212-696-7100']]

for d in data:

    if "industries" in d:
        for data in d[1]:
            if data["industry"]:
                print([data["industry"]["source"],
                      data["industry"]["shortDescription"]])
                print()
    else:
        print(d)
