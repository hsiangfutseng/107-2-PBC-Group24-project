from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time

company_num = [2542]     #先設定1家
#company_num = input("company number :")
#company_num = company_num.split(' ')          #用戶輸入之各家公司代號  #之後要限制指定輸入格式
driver = webdriver.Chrome("C:\\Users\\User\\Desktop\\商管程設\\chromedriver.exe")           #"注意"絕對路徑
driver.maximize_window()          #網頁全螢幕
driver.get(r"http://mops.twse.com.tw/mops/web/t05st22_q1")
years_data_dict = dict()

#爬資料
for i in company_num:
    print(i)
    driver_input = driver.find_element_by_xpath('//*[@id="co_id"]')
    driver_input.send_keys(i)     #輸入公司代號
    driver.find_element_by_xpath("//td[@class='bar01b']//td[2]//div[1]//div[1]//input[1]").click()     #點擊搜尋鍵
    time.sleep(2)
    for j in range(1, 4):
        years_data_dict[j+104] = []
        for k in range(2, 21):
            information = driver.find_element_by_xpath("//div[@id='zoom']/div/center[2]/table/tbody/tr[" + str(k) + "]/td[" + str(j) + "]").text
            years_data_dict[j+104] += [float("".join(information.strip().split(',')))]     #整理資料並轉換成float
    #資料，["負債佔資產比率","長期資金佔不動產廠房及設備比率","流動比率"...]( 字串元素：float )
    years_data_dict.items()
    driver.find_element_by_xpath('//*[@id="co_id"]').click()     #點擊"輸入公司代號之輸入格" -> 消除原先輸入的值

for i in company_num:
    s = Select(driver.find_element_by_id('isnew'))     #選取滾輪
    s.select_by_visible_text("歷史資料")
    #選取滾輪標籤中的(...)
    driver_input.send_keys(i)
    driver.find_element_by_xpath("//input[@id='year']").send_keys("104")     #"年分"輸入104年(因為一次只能獲取前3年的資料)
    driver.find_element_by_xpath("//td[@class='bar01b']//td[2]//div[1]//div[1]//input[1]").click()
    time.sleep(2)
    for j in range(1, 4):
        years_data_dict[j+101] = [] 
        for k in range(2, 21):
            information = driver.find_element_by_xpath("//div[@id='zoom']/div/center[2]/table/tbody/tr[" + str(k) + "]/td[" + str(j) + "]").text
            years_data_dict[j+101] += [float("".join(information.strip().split(',')))]
    #取2018年各資料，["負債佔資產比率","長期資金佔不動產廠房及設備比率","流動比率"...]( 字串元素：float )
    driver.find_element_by_xpath('//*[@id="co_id"]').click()

#第二部分下半部
p2_down_rank = []
for files in range(19):     #files = "負債佔資產比率","長期資金佔不動產廠房及設備比率","流動比率"...
    p2_down_targetstock = years_data_dict[107][files]     #得到最新的各資料以便之後排名用
    the_flie = []
    for over_the_years in range(102, 108):     #over_the_years = 102年 到 107年
        the_flie.append(years_data_dict[over_the_years][files])
    organized_the_flie = sorted(the_flie)    #把獲取的資料排序
    if files == 7 or files == 9:     #"平均收現日數" 和 "平均銷貨日數" 越低越好
        pass
    else:
        organized_the_flie.reverse()
    p2_down_rank.append(str(organized_the_flie.index(p2_down_targetstock) + 1) + '/' + str(len(organized_the_flie)))

print('===第二部分下半部照順序的排名===')
print(p2_down_rank)
print('======')

driver.close()