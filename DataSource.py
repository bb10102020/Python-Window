#資料來源：政府資料開放平台 - https://data.gov.tw/dataset/33649

import requests

AREA = ["澎湖","望安","金門","七美","花蓮"]
DATA = None

def download():
    global DATA
    url = "https://www.kia.gov.tw/API/InstantSchedule.ashx?AirFlyLine=2&AirFlyIO=2"

    response = requests.get(url)
    if response.status_code == 200:
        print("下載成功")
        DATA = response.json()

download()
