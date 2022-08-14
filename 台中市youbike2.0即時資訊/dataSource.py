import requests

AREA = ["大里區", "清水區", "南區", "西屯區", "潭子區", "梧棲區", "西區", "大里區", "北屯區", "豐原區", "外埔區", "沙鹿區", "神岡區"]
DATA = None

def download():
    global DATA
    url = "https://datacenter.taichung.gov.tw/swagger/OpenData/9af00e84-473a-4f3d-99be-b875d8e86256"
    response = requests.get(url)
    if response.status_code == 200:
        print("下載成功")
        DATA = response.json()

download()
