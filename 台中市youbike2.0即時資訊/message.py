import requests

AREA = ["大里區", "清水區", "南區", "西屯區", "潭子區", "梧棲區", "西區", "大里區", "北屯區", "豐原區", "外埔區", "沙鹿區", "神岡區"]
from tkinter.simpledialog import Dialog
import tkintermapview as tkmap
import tkinter as tk

class MapDialog(Dialog):
    def __init__(self, parent, title = None,info=None):
        self.info = info
        super().__init__(parent,title=title)

    def getCenter(self):
        lat_l,lat_s,lng_l,lng_s = -10000,100000,-100000,100000
        for site in self.info:
            lat = float(site["lat"])
            lng = float(site["lng"])
            if lat_l < lat:
                lat_l = lat
            if lat_s > lat:
                lat_s = lat
            if lng_l < lng:
                lng_l = lng
            if lng_s > lng:
                lng_s = lng

        lat_cen = lat_s + ((lat_l - lat_s) / 2)
        lng_cen = lng_s + ((lng_l - lng_s) / 2)
        print(lat_cen)
        print(lng_cen)
        return lat_cen, lng_cen

    def body(self, master):
        self.map_widget = tkmap.TkinterMapView(master, width=800,height=600,corner_radius=0)
        centerLat,centerLong = self.getCenter()
        self.map_widget.set_position(centerLat, centerLong)  # 位置
        self.map_widget.set_zoom(15)  # 設定顯示大小
        self.map_widget.pack()
        #建立marker
        for site in self.info:
            lat = float(site["lat"])
            lng = float(site["lng"])
            sbi = float(site["sbi"])
            bemp = float(site["bemp"])
            marker = self.map_widget.set_marker(lat,lng,marker_color_outside='white',font=('arial',10),text=f"{site['sna']}\n可借:{sbi}\n可還:{bemp}")
            marker.data = site

    def buttonbox(self):
        bottomFrame = tk.Frame(self)
        tk.Button(bottomFrame,text="關閉"+self.title()+"地圖",command=self.ok,padx=10,pady=10).pack(padx=10,pady=20)
        bottomFrame.pack()

    def ok(self, event=None):
        super().ok()