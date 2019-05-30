# #(1) Yahoo搜尋
# from selenium import webdriver

# url ='https://tw.yahoo.com/'

# #打開瀏覽器,確保你已經有chromedriver在你的目錄下
# browser=webdriver.Chrome('./chromedriver')
# #在瀏覽器打上網址連入
# browser.get(url) 

# #這時候就可以分析網頁裡面的元素
# element = browser.find_element_by_id('UHSearchBox')
# element.send_keys('Hello World')

# sumbit = browser.find_element_by_id('UHSearchWeb').click() 

#-------------------------------------------------------------
# #(2) 模擬鍵盤操作
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys #模擬鍵盤操作

# driver = webdriver.Chrome()
# driver.get("http://www.python.org")
# assert "Python" in driver.title
# elem = driver.find_element_by_name("q")
# elem.clear()
# elem.send_keys("pycon") #模擬鍵盤操作，輸入"pycon"
# elem.send_keys(Keys.ENTER) #就像是按下ENTER
# assert "No results found." not in driver.page_source
# driver.close()

#------------------------------------------------------------
# #(3)select 下拉框(https://huilansame.github.io/huilansame.github.io/archivers/drop-down-select)
# from selenium import webdriver
# from selenium.webdriver.support.ui import Select
# driver = webdriver.Chrome()
# driver.get('http://sahitest.com/demo/selectTest.htm')

# # Select类提供了三种选择某一选项的方法：
# # select_by_index(index)
# # select_by_value(value)
# # select_by_visible_text(text)

# #第一個select框
# s1 = Select(driver.find_element_by_id('s1Id')) 
# s1.select_by_index(1)  # 选择第二项选项：o1
# s1.select_by_value("o2")  # 选择value="o2"的项
# s1.select_by_visible_text("o3")  # 选择text="o3"的值，即在下拉时我们可以看到的文本

# # driver.quit()

#------------------------------------------------------------
#(4)BeutifulSoup (https://www.crummy.com/software/BeautifulSoup/bs4/doc.zh/)
# from selenium import webdriver
# browser = webdriver.Chrome()
# browser.get('http://mops.twse.com.tw/mops/web/t51sb02')

# from bs4 import BeautifulSoup
# soup = BeautifulSoup(browser.page_source, 'html.parser')
# a_tags = soup.select('table.hasBorder tbody')  #標籤名稱.class / 標籤名稱#id屬性
# for t in a_tags:
# 	print(t.text)

# browser.close()
#-----------------------------------------------------------------
# #https://ithelp.ithome.com.tw/articles/10204390?sc=iThelpR
# from selenium import webdriver
# browser = webdriver.Chrome()
# browser.get('http://mops.twse.com.tw/mops/web/t163sb04')

# from selenium.webdriver.common.keys import Keys #模擬鍵盤操作
# #輸入年度
# elem = browser.find_element_by_id("year")
# elem.clear()
# elem.send_keys("106") #模擬鍵盤操作，輸入要打的字

# #選擇季度
# from selenium.webdriver.support.ui import Select
# s1 = Select(browser.find_element_by_id('season')) 
# s1.select_by_visible_text("3")  # 选择text="3"的值，即在下拉时我们可以看到的文本

# #按下查詢
# browser.find_element_by_xpath("//input[@value=' 查詢 '][@type='button']").click()

# #等待頁面加載
# import time
# time.sleep(10)

# #找想要的
# from bs4 import BeautifulSoup
# soup = BeautifulSoup(browser.page_source, 'html.parser')
# a_tags = soup.select('table.hasBorder tbody')  #標籤名稱.class / 標籤名稱#id屬性
# for t in a_tags:
# 	print(t.text)

# # browser.close()

#-----------------------------------------------------------------
# #淨利(改制後)
# from selenium import webdriver
# browser = webdriver.Chrome()
# browser.get('http://mops.twse.com.tw/mops/web/t164sb04')

# from selenium.webdriver.common.keys import Keys #模擬鍵盤操作
# #選擇"歷史資料"
# from selenium.webdriver.support.ui import Select
# s1 = Select(browser.find_element_by_id('isnew')) 
# s1.select_by_visible_text("歷史資料")  # 选择text="歷史資料"的值，即在下拉时我们可以看到

# #輸入公司代號
# elem = browser.find_element_by_id("co_id")
# elem.clear()
# elem.send_keys("2509") #模擬鍵盤操作，輸入要打的字

# #輸入年度
# elem = browser.find_element_by_id("year")
# elem.clear()
# elem.send_keys("104") #模擬鍵盤操作，輸入要打的字

# #選擇季度
# from selenium.webdriver.support.ui import Select
# s1 = Select(browser.find_element_by_id('season')) 
# s1.select_by_visible_text("2")  # 选择text="3"的值，即在下拉时我们可以看到的文本

# #按下查詢
# browser.find_element_by_xpath("//input[@value=' 查詢 '][@type='button']").click()

# #等待頁面加載
# import time
# time.sleep(5)

# #找想要的
# from bs4 import BeautifulSoup
# soup = BeautifulSoup(browser.page_source, 'html.parser')
# a_tags = soup.select('div#table01 center table.hasBorder tbody tr td.even')  #標籤名稱.class / 標籤名稱#id屬性

# # for t in a_tags: #印全部
# # 	print(t.text)
# ans = ""
# i = 0
# for t in a_tags: #只印第82個東西
# 	if t.text == "本期淨利（淨損）":
# 		i = 10000
# 		print(t.text)
# 	if i == 10001:
# 		print(t.text.strip())
# 		break
# 	i += 1
# browser.close()

#-----------------------------------------------------------------
#EPS
from selenium import webdriver
browser = webdriver.Chrome()
browser.get('http://mops.twse.com.tw/mops/web/t163sb19')

from selenium.webdriver.common.keys import Keys #模擬鍵盤操作
#選擇"建材營造"
from selenium.webdriver.support.ui import Select
s1 = Select(browser.find_element_by_name('code')) 
s1.select_by_visible_text("建材營造")  # 选择text="歷史資料"的值

#輸入年度
elem = browser.find_element_by_id("year")
elem.clear()
elem.send_keys("104") #模擬鍵盤操作，輸入要打的字

#選擇季度
from selenium.webdriver.support.ui import Select
s1 = Select(browser.find_element_by_id('season')) 
s1.select_by_visible_text("2")  # 选择text="2"的值

#按下查詢
browser.find_element_by_xpath("//input[@value=' 查詢 '][@type='button']").click()

#等待頁面加載
import time
time.sleep(5)

#找想要的
from bs4 import BeautifulSoup
soup = BeautifulSoup(browser.page_source, 'html.parser')
a_tags = soup.select('div#table01 table.hasBorder tbody tr td')  #標籤名稱.class / 標籤名稱#id屬性

for t in a_tags: #印全部
	print(t.text)


print("------------------")
ans = ""

i = 0
for t in a_tags: #只印該公司的EPS
	if t.text.strip() == "2511":
		i = 100000000
		print(t.text)

	if i == 100000001:
		print(t.text.strip())

	if i == 100000003:
		print(t.text.strip())
		break
	i += 1
browser.close()
