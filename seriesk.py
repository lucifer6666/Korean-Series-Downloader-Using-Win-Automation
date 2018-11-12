import sys
from tkinter import *
from PyQt4 import QtGui,QtCore
import pyttsx3
import re
from selenium.webdriver import Firefox
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium import webdriver
from pywinauto.application import Application
import pyautogui
from selenium.common.exceptions import NoSuchElementException


class Window(QtGui.QMainWindow):
    def __init__(self, parent=None):
        super(Window,self).__init__(parent)
        self.setGeometry(150,150,400,210)
        self.setWindowTitle('Korean Series Downloader')
        self.nam=QtGui.QLabel('Series Name',self)
        self.nam.setGeometry(10,10,100,30)
        self.name=QtGui.QLineEdit('',self)
        self.name.setGeometry(120,10,210,30)
        self.order=QtGui.QLabel('From - E',self)
        self.order.setGeometry(10,50,100,30)
        self.frm=QtGui.QLineEdit('',self)
        self.frm.setGeometry(120,50,50,30)
        self.order=QtGui.QLabel('To - E',self)
        self.order.setGeometry(180,50,80,30)
        self.to=QtGui.QLineEdit('',self)
        self.to.setGeometry(270,50,50,30)
        self.order1=QtGui.QLabel('Download Links',self)
        self.order1.setGeometry(10,90,150,30)
        self.btn=QtGui.QPushButton('Link 1',self)
        self.btn.setGeometry(50,130,80,30)
        self.btn.clicked.connect(self.down1)
        self.btn1=QtGui.QPushButton('Link 2',self)
        self.btn1.setGeometry(140,130,80,30)
        self.btn1.clicked.connect(self.down2)
        self.output=QtGui.QLabel('',self)
        self.output.setGeometry(10,170,300,30)
        self.show()
    # Link 1 .... Function
    def down1(self):
        self.output.setText("")
        name= self.name.text()
        efrm= self.frm.text()
        eto= self.to.text()
        eto = int(eto) + 1
        self.out=[]
        n1 = name.replace(" ", "-")
        link = "https://www1.ondramanice.co/" + str(n1) + "/watch-" + str(n1) + "-episode-"
        i=10
        k=1
        tab=1
        flag=0
        opts = Options()
        opts.add_extension("I:/projects/py/AdBlock_v3.34.0.crx")
        opts.add_extension("Pop-up-blocker-for-Chrome™-Poper-Blocker_v4.0.8.crx")
        driver = webdriver.Chrome(options=opts)
        for a in range(int(efrm),int(eto)):
            x=a
            driver.get(link+str(a)+"-online")
            try:
                driver.find_element_by_link_text("Download")
            except NoSuchElementException:
                if a>=efrm & flag==0:
                    driver.quit()
                    self.output.setText("Error - Check Series Name")
                else:
                    self.output.setText("Error - Episode " + str(a) + " Not Present")
                    continue
            else:
                el = driver.find_element_by_link_text("Download").get_attribute("href")
                driver.get(el)
            try:
                driver.find_element_by_partial_link_text("DOWNLOAD (360P -")
            except NoSuchElementException:
                try:
                    driver.find_element_by_partial_link_text("DOWNLOAD (")
                except NoSuchElementException:
                    try:
                        driver.find_element_by_partial_link_text("DOWNLOAD RAPIDVIDEO")
                    except NoSuchElementException:
                        i=2
                        if(a==x):
                            self.out.append(a)
                            continue
                    else:
                        d=driver.find_element_by_partial_link_text("DOWNLOAD RAPIDVIDEO").get_attribute("href")
                        driver.get(d)
                    try:
                        driver.find_element_by_partial_link_text("Download")
                    except NoSuchElementException:
                        if(a==x):
                            self.out.append(a)
                            continue
                    else:
                        i=1
                        down=driver.find_element_by_partial_link_text("Download").get_attribute("href")
                else:
                    i=1
                    down=driver.find_element_by_partial_link_text("DOWNLOAD (").get_attribute("href")
            else:
                i=1
                down=driver.find_element_by_partial_link_text("DOWNLOAD (360P -").get_attribute("href")
            if tab==1:
                pyautogui.hotkey('ctrl' , '1')
                tab=2
            if(i==1):
                app = Application().start("C:/Program Files (x86)/Internet Download Manager/IDMan.exe")
                # app = Application().start("C:/Program Files (x86)/Internet Download Manager/IDMan.exe")
                pyautogui.press('alt')
                pyautogui.press('enter')
                pyautogui.press('enter')
                pyautogui.typewrite(down)
                pyautogui.press('enter')
                pyautogui.press('tab')
                pyautogui.press('tab')
                pyautogui.press('tab')
                pyautogui.press('tab')
                pyautogui.press('tab')
                pyautogui.press('tab')
                pyautogui.press('enter')
                pyautogui.typewrite(str(name)+" Episode "+str(a)+".mp4",interval=0.05)
                pyautogui.press('enter')
                pyautogui.press('tab')
                pyautogui.press('enter')
                flag=1
            else:
                driver.quit()
                self.output.setText("No Link Found")
        driver.quit()
        if len(self.out)!=0:
            out1=""
            for i in self.out:
                out1 = str(out1)+ str(i) + ","
            self.output.setText("Error Episodes - " + str(out1))
        else:
            self.output.setText("Downloads Sucessfully Added..")

    # Link 2 .... Function
    def down2(self):
        self.output.setText("")
        name= self.name.text()
        efrm= self.frm.text()
        eto= self.to.text()
        self.out=[]
        eto= int(eto) + 1
        n1 = name.replace(" ", "-")
        link = "http://kissdrama.club/" + str(n1) + "/"
        i=3
        opts.add_extension("I:/projects/py/AdBlock_v3.34.0.crx")
        opts.add_extension("Pop-up-blocker-for-Chrome™-Poper-Blocker_v4.0.8.crx")
        assert opts.headless
        driver = webdriver.Chrome(options=opts)
        driver.get(link)
        try:
            driver.find_element_by_partial_link_text("Download")
        except NoSuchElementException:
            driver.quit()
            self.output.setText("Wrong Name Check Name")
        else:
            d=driver.find_element_by_partial_link_text("Download").get_attribute("href")
            driver.get(d)
        for a in range(int(efrm),int(eto)):
            x=a
            if a << 10:
                de = driver.find_element_by_partial_link_text("Download Episode 0" + str(a))
                de.click()
                driver.get(de.get_attribute("href"))
                print(de)
            else:
                de = driver.find_element_by_partial_link_text("Download Episode " + str(a)).get_attribute("href")
                driver.get(de)
            try:
                driver.find_element_by_partial_link_text("Rapid")
            except NoSuchElementException:
                i=2
                if(a==x):
                    self.out.append(a)
                    continue
            else:
                ra = driver.find_element_by_link_text("Rapid").get_attribute("href")
                driver.get(ra)
                try:
                    driver.find_element_by_partial_link_text("DOWNLOAD")
                except NoSuchElementException:
                    if(a==x):
                        self.out.append(a)
                        continue
                else:
                    down=driver.find_element_by_partial_link_text("DOWNLOAD").get_attribute("href")
                    i=1
            if(i==1):
                app = Application().start("C:/Program Files (x86)/Internet Download Manager/IDMan.exe")
                # app = Application().start("C:/Program Files (x86)/Internet Download Manager/IDMan.exe")
                pyautogui.press('alt')
                pyautogui.press('enter')
                pyautogui.press('enter')
                pyautogui.typewrite(down)
                pyautogui.press('enter')
                pyautogui.press('tab')
                pyautogui.press('tab')
                pyautogui.press('tab')
                pyautogui.press('tab')
                pyautogui.press('tab')
                pyautogui.press('tab')
                pyautogui.press('enter')
                pyautogui.typewrite(str(name)+" Episode "+str(a)+".mp4",interval=0.05)
                pyautogui.press('enter')
                pyautogui.press('tab')
                pyautogui.press('enter')
            else:
                driver.quit()
                self.output.setText("No Link Found")
            driver.get(d)
        driver.quit()
        if len(self.out)!=0:
            out1=""
            for i in self.out:
                out1 = str(out1) + str(i) + ","
            self.output.setText("Error Episodes - " + str(out1))
        else:
            self.output.setText("Downloads Sucessfully Added..")


app=QtGui.QApplication(sys.argv)
GUI=Window()
sys.exit(app.exec_())