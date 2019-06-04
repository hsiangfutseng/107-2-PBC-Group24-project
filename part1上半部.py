#Good Info (只抓2018的)
co_id = input("輸入四位數股票代號: ") #輸入四位數股票代號
#先預設比較另外3家公司
# compare_company = []
# com1 = input("輸入第一家要比較的股票代號: ")
# compare_company.append(com1)
# com2 = input("輸入第二家要比較的股票代號: ")
# compare_company.append(com2)
# com3 = input("輸入第三家要比較的股票代號: ")
# compare_company.append(com3)

index = dict() #以指標為key的dict, 裡面放不同公司的資料


from selenium import webdriver
from selenium.webdriver.common.keys import Keys #模擬鍵盤操作
browser = webdriver.Chrome()
url = "https://goodinfo.tw/StockInfo/StockBzPerformance.asp?STOCK_ID="
url += co_id
browser.get(url)

#等待頁面加載
import time
time.sleep(4)

#找想要的
from bs4 import BeautifulSoup
soup = BeautifulSoup(browser.page_source, 'html.parser')


#找指標
a_tags = soup.select('div#divFinDetail table.solid_1_padding_4_0_tbl tbody tr td')  #標籤名稱.class / 標籤名稱#id屬性

#毛利率
index['毛利率'] = []
for i in range(0, len(a_tags)):
	if a_tags[i].text== "2018":
		try:
			tmp = float(a_tags[i+12].text)
		except Exception as inst:
			tmp = a_tags[i+12].text
		index['毛利率'].append(tmp)
		break

#淨利率
index['淨利率'] = []
for i in range(0, len(a_tags)):
	if a_tags[i].text== "2018":
		try:
			tmp = float(a_tags[i+15].text)
		except Exception as inst:
			tmp = a_tags[i+15].text
		index['淨利率'].append(tmp)
		break

#殖利率
index['殖利率'] = []
from selenium.webdriver.common.keys import Keys #模擬鍵盤操作
browser.find_element_by_xpath("//input[@value='股利統計'][@type='button']").click()
time.sleep(2)
soup = BeautifulSoup(browser.page_source, 'html.parser')
b_tags = soup.select('div#divFinDetail table.solid_1_padding_4_0_tbl tbody tr td')  #標籤名稱.class / 標籤名稱#id屬性

for i in range(0, len(b_tags)):
	if b_tags[i].text== "2018":
		try:
			tmp = float(b_tags[i+15].text)
		except Exception as inst:
			tmp = b_tags[i+15].text
		index['殖利率'].append(tmp)
		break

#盈餘分配率
index['盈餘分配率'] = []
for i in range(0, len(b_tags)):
	if b_tags[i].text== "2018":
		try:
			tmp = float(b_tags[i+18].text)
		except Exception as inst:
			tmp = b_tags[i+18].text
		index['盈餘分配率'].append(tmp)
		break

#股利發放穩定性(2012~2018年"有發放股利年數")
index['股利發放穩定性'] = []
yes = 0
year = ["2012","2013","2014","2015","2016","2017","2018"]
for i in range(0, len(b_tags)):
	if b_tags[i].text in year:
		try:
			tmp = float(b_tags[i+12].text)
			if tmp != 0:
				yes += 1
		except Exception as inst:
			pass

index['股利發放穩定性'].append(yes)


#淨值比(PBR)
browser.find_element_by_xpath("//input[@value='PER/PBR'][@type='button']").click()
time.sleep(2)
soup = BeautifulSoup(browser.page_source, 'html.parser')
c_tags = soup.select('div#divFinDetail table.solid_1_padding_4_0_tbl tbody tr td')  #標籤名稱.class / 標籤名稱#id屬性
index['淨值比(PBR)'] = []
for i in range(0, len(c_tags)):
	if c_tags[i].text== "2018":
		try:
			tmp = float(c_tags[i+16].text)
		except Exception as inst:
			tmp = c_tags[i+16].text
		index['淨值比(PBR)'].append(tmp)
		break

#本益比(PER)
index['本益比(PER)'] = []
for i in range(0, len(c_tags)):
	if c_tags[i].text== "2018":
		try:
			tmp = float(c_tags[i+12].text)
		except Exception as inst:
			tmp = c_tags[i+12].text
		index['本益比(PER)'].append(tmp)
		break



print(index)




# browser.close()