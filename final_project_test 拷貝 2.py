import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome('/Users/chanpohung/Desktop/chromedriver')
driver.get("http://mops.twse.com.tw/mops/web/t05st22_q1")
driver_input = driver.find_element_by_xpath('//*[@id="co_id"]')
driver_input.send_keys('2330')
driver.execute_script("doAction();ajax1(document.form1,'table01');")

time.sleep(2)

driver.find_element_by_xpath('//*[@id="search_bar1"]/div/input').click()
a_list = []


#for i in range(2,21):
for j in range(1,4):
    a = driver.find_element_by_xpath('//*[@id="table01"]/center[2]/table/tbody/tr[2]/td[' + str(j) + ']').text
    a_list.append(a)

if float(a_list[0]) > float(a_list[1]):
    if float(a_list[2]) > float(a_list[0]):
        print('107 is the best')
    else:
        print('105 is the best')
else:
    if float(a_list[2]) > float(a_list[1]):
        print('107 is the best')
    else:
        print('106 is the best')

        # 往上是時間分析
    #  -------------------------------------------
        # 往下是個股分析

import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

com_num = input("company number :")
com_num = com_num.split(' ')
driver = webdriver.Chrome('D:\download\chromedriver_win32\chromedriver')
driver.get("http://mops.twse.com.tw/mops/web/t05st22_q1")
#driver_input = driver.find_element_by_xpath('//*[@id="co_id"]')
#driver_input.send_keys(1101)
#driver.execute_script("doAction();ajax1(document.form1,'table01');")
#time.sleep(2)
a_list = []
for i in com_num:
    print(i)
    driver_input = driver.find_element_by_xpath('//*[@id="co_id"]')  #
    driver_input.send_keys(i)
    driver.execute_script("doAction();ajax1(document.form1,'table01');")
    time.sleep(5)
    a_list.append(driver.find_element_by_xpath('//*[@id="table01"]/center[2]/table/tbody/tr[15]/td[1]').text)
    print(driver.find_element_by_xpath('//*[@id="table01"]/center[2]/table/tbody/tr[15]/td[1]').text)
    time.sleep(2)
    driver_input = driver.find_element_by_xpath('//*[@id="co_id"]').click()

    #    ----------------------------------------
         #   往下是另一個可以抓全部股票同時期值

import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome('/Users/chanpohung/Desktop/chromedriver')
driver.get("http://mops.twse.com.tw/mops/web/t51sb02_q1")
driver.find_element_by_xpath('//*[@id="TYPEK"]').find_element_by_xpath('//*[@id="TYPEK"]/option[4]').click()
driver_input = driver.find_element_by_xpath('//*[@id="year"]')
driver_input.send_keys('106')
driver_input.send_keys(Keys.ENTER)

time.sleep(10)
a_list = []

for i in range(110):
    for j in range(15):
        if 3 + 17*i + j <= 1068:
            table_text = driver_input.find_element_by_xpath('//*[@id="table01"]/table[3]/tbody/tr[' + str(3 + 17*i + j) + ']').text
            a_list.append(table_text)
        else:
            break
print(a_list)
driver.close()