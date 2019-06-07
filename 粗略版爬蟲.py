from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time

companys = [] #用來存放個間公司代碼的list
co_id = input("輸入四位數股票代號: ") 
companys.append(co_id)
#假設要比較另外5家公司
com1 = input("輸入第一家要比較的股票代號: ")
companys.append(com1)
com2 = input("輸入第二家要比較的股票代號: ")
companys.append(com2)
com3 = input("輸入第三家要比較的股票代號: ")
companys.append(com3)
com4 = input("輸入第四家要比較的股票代號: ")
companys.append(com4)
com5 = input("輸入第五家要比較的股票代號: ")
companys.append(com5)                        #用戶輸入之各家公司代號  #之後要限制指定輸入格式

driver = webdriver.Chrome("C:\\Users\\User\\Desktop\\商管程設\\chromedriver.exe")           #"注意"絕對路徑
driver.maximize_window()          #網頁全螢幕
driver.get(r"http://mops.twse.com.tw/mops/web/t05st22_q1")
years_data_dict = dict()     
#目標公司各年的指標資料 {"公司代碼":{107:["負債佔資產比率","長期資金佔不動產廠房及設備比率","流動比率"...], 106:[同前]...., 102:[同前]}...}
files_name = ["負債佔資產比率", "長期資金佔不動產廠房及設備比率", "流動比率", "速動比率", "利息保障倍數", "應收款項週轉率", "平均收現日數", "存貨週轉率", "平均銷貨日數", "不動產廠房及設備週轉率", "總資產週轉率", "資產報酬率", "權益報酬率", "稅前純益佔實收資本比率", "純益率", "每股盈餘", "現金流量比率", "現金流量允當比率", "現金再投資比率"]

#爬資料
for i in companys:
    s = Select(driver.find_element_by_id('isnew'))     #選取滾輪
    s.select_by_visible_text("歷史資料")
    #選取滾輪標籤中的(...)
    driver_input = driver.find_element_by_xpath('//*[@id="co_id"]')
    driver_input.send_keys(i)     #輸入公司代號
    driver.find_element_by_xpath("//input[@id='year']").send_keys("107")     #"年分"輸入104年(因為一次只能獲取前3年的資料)
    driver.find_element_by_xpath("//td[@class='bar01b']//td[2]//div[1]//div[1]//input[1]").click()     #點擊搜尋鍵
    time.sleep(1)
    years_data_dict[i] = dict()
    for j in range(1, 4):
        years_data_dict[i][j+2015] = []
        for k in range(2, 21):
            information = driver.find_element_by_xpath("//div[@id='zoom']/div/center[2]/table/tbody/tr[" + str(k) + "]/td[" + str(j) + "]").text
            if information != "NA":
                try:
                    years_data_dict[i][j+2015] += [float("".join(information.strip().split(',')))]     #整理資料並轉換成float
                except Exception as inst:
                    years_data_dict[i][j+2015] += ["".join(information.strip().split(','))]
    #字串元素：float
    driver.find_element_by_xpath('//*[@id="co_id"]').click()     #點擊"輸入公司代號之輸入格" -> 消除原先輸入的值

    s = Select(driver.find_element_by_id('isnew'))     #選取滾輪
    s.select_by_visible_text("歷史資料")
    #選取滾輪標籤中的(...)
    driver_input.send_keys(i)
    driver.find_element_by_xpath("//input[@id='year']").send_keys("104")     #"年分"輸入104年(因為一次只能獲取前3年的資料)
    driver.find_element_by_xpath("//td[@class='bar01b']//td[2]//div[1]//div[1]//input[1]").click()
    time.sleep(1)
    for j in range(1, 4):
        years_data_dict[i][j+2012] = [] 
        for k in range(2, 21):
            information = driver.find_element_by_xpath("//div[@id='zoom']/div/center[2]/table/tbody/tr[" + str(k) + "]/td[" + str(j) + "]").text
            if information != "NA":
                try:
                    years_data_dict[i][j+2012] += [float("".join(information.strip().split(',')))]
                except Exception as inst:
                    years_data_dict[i][j+2012] += ["".join(information.strip().split(','))]
    #字串元素：float
    driver.find_element_by_xpath('//*[@id="co_id"]').click()

#第一部分下半部
p1_down_rank = []
objective_company = companys[0]
for files in range(19):     #files = "負債佔資產比率","長期資金佔不動產廠房及設備比率","流動比率"...
    if isinstance(years_data_dict[objective_company][2018][files],float):
        p1_down_targetstock = years_data_dict[objective_company][2018][files]     #得到最新的各資料以便之後排名用
    else:
        print('無資料：' + files_name[files])
        p1_down_rank.append("NA")
        continue

    the_flie = []
    
    for company in companys:     #107年各公司資料
        if isinstance(years_data_dict[company][2018][files],float):
            the_flie.append(years_data_dict[company][2018][files])
    organized_the_flie = sorted(the_flie)    #把獲取的資料排序
    
    if files == 7 or files == 9:     #"平均收現日數" 和 "平均銷貨日數" 越低越好
        pass
    else:
        organized_the_flie.reverse()

    p1_down_rank.append(str(organized_the_flie.index(p1_down_targetstock) + 1) + '/' + str(len(organized_the_flie)))

print('===第一部分下半部照順序的排名===')
print(p1_down_rank)
print('======')

#第二部分下半部
p2_down_rank = []
objective_company = companys[0]
for files in range(19):     #files = "負債佔資產比率","長期資金佔不動產廠房及設備比率","流動比率"...
    if isinstance(years_data_dict[objective_company][2018][files],float):
        p2_down_targetstock = years_data_dict[objective_company][2018][files]     #得到最新的各資料以便之後排名用
    the_flie = []
    for over_the_years in range(2013, 2019):     #over_the_years = 102年 到 107年
        if isinstance(years_data_dict[objective_company][over_the_years][files],float):
            the_flie.append(years_data_dict[objective_company][over_the_years][files])
    organized_the_flie = sorted(the_flie)    #把獲取的資料排序
    if files == 7 or files == 9:     #"平均收現日數" 和 "平均銷貨日數" 越低越好
        pass
    else:
        organized_the_flie.reverse()
    if organized_the_flie == []:
        print('無資料：' + files_name[files])
        p2_down_rank.append("NA")
    else:
        p2_down_rank.append(str(organized_the_flie.index(p2_down_targetstock) + 1) + '/' + str(len(organized_the_flie)))

print('===第二部分下半部照順序的排名===')
print(p2_down_rank)
print('======')

driver.close()