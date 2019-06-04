#Good Info (2012~2018)
co_id = input("輸入四位數股票代號: ") #輸入四位數股票代號

from selenium import webdriver
from selenium.webdriver.common.keys import Keys #模擬鍵盤操作
browser = webdriver.Chrome()
url = "https://goodinfo.tw/StockInfo/StockBzPerformance.asp?STOCK_ID="
url += co_id
browser.get(url)
import time
time.sleep(4)

#找指標
index = dict() #以指標為key的dict, 裡面放不同年份的資料
year = ["2012","2013","2014","2015","2016","2017","2018"]


from bs4 import BeautifulSoup
soup = BeautifulSoup(browser.page_source, 'html.parser')
a_tags = soup.select('div#divFinDetail table.solid_1_padding_4_0_tbl tbody tr td')  #標籤名稱.class / 標籤名稱#id屬性

#毛利率
index['毛利率'] = []
for i in range(0, len(a_tags)):
	if a_tags[i].text in year:
		try:
			tmp = float(a_tags[i+12].text)
		except Exception as inst:
			tmp = a_tags[i+12].text
		index['毛利率'].append(tmp)

#淨利率
index['淨利率'] = []
for i in range(0, len(a_tags)):
	if a_tags[i].text in year:
		try:
			tmp = float(a_tags[i+15].text)
		except Exception as inst:
			tmp = a_tags[i+15].text
		index['淨利率'].append(tmp)


#殖利率
index['殖利率'] = []
from selenium.webdriver.common.keys import Keys #模擬鍵盤操作
browser.find_element_by_xpath("//input[@value='股利統計'][@type='button']").click()
time.sleep(2)
soup = BeautifulSoup(browser.page_source, 'html.parser')
b_tags = soup.select('div#divFinDetail table.solid_1_padding_4_0_tbl tbody tr td')  #標籤名稱.class / 標籤名稱#id屬性

for i in range(0, len(b_tags)):
	if b_tags[i].text in year:
		try:
			tmp = float(b_tags[i+15].text)
		except Exception as inst:
			tmp = b_tags[i+15].text
		index['殖利率'].append(tmp)

#盈餘分配率
index['盈餘分配率'] = []
for i in range(0, len(b_tags)):
	if b_tags[i].text in year:
		try:
			tmp = float(b_tags[i+18].text)
		except Exception as inst:
			tmp = b_tags[i+18].text
		index['盈餘分配率'].append(tmp)

#淨值比(PBR)
browser.find_element_by_xpath("//input[@value='PER/PBR'][@type='button']").click()
time.sleep(2)
soup = BeautifulSoup(browser.page_source, 'html.parser')
c_tags = soup.select('div#divFinDetail table.solid_1_padding_4_0_tbl tbody tr td')  #標籤名稱.class / 標籤名稱#id屬性
index['淨值比(PBR)'] = []
for i in range(0, len(c_tags)):
	if c_tags[i].text in year:
		try:
			tmp = float(c_tags[i+16].text)
		except Exception as inst:
			tmp = c_tags[i+16].text
		index['淨值比(PBR)'].append(tmp)

#本益比(PER)
index['本益比(PER)'] = []
for i in range(0, len(c_tags)):
	if c_tags[i].text in year:
		try:
			tmp = float(c_tags[i+12].text)
		except Exception as inst:
			tmp = c_tags[i+12].text
		index['本益比(PER)'].append(tmp)


for key in index:
	print(key, index[key])



# browser.close()