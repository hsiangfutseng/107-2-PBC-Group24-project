from selenium import webdriver
from bs4 import BeautifulSoup

driver = webdriver.Chrome(r"C:\Users\User\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Python 3.7\chromedriver.exe")
#用'驅動器'打開Chrome瀏覽器，驅動器位置在(....)
driver.maximize_window()#driver.fullscreen_window()
#網頁全螢幕
driver.get(r"http://mops.twse.com.tw/mops/web/t51sb02")
#打開(網址)之網頁

driver.find_element_by_xpath("//input[@id='year']").send_keys('101') 
#用id找到(...)#點擊  #send_keys()輸入...
#換行\n 有按Enter鍵功能

driver.find_element_by_xpath("//form[@id='form1']/table/tbody/tr/td[4]/table//tr/td[2]/div/div[@class='search']/input[@value=' 查詢 ']").click() 
