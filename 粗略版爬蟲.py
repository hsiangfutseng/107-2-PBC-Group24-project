import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time

company_num = [2542]     #先設定1家
#company_num = input("company number :")
#company_num = company_num.split(' ')          #用戶輸入之各家公司代號  #之後要限制指定輸入格式
driver = webdriver.Chrome(r"C:\Users\User\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Python 3.7\chromedriver.exe")           #"注意"絕對路徑
driver.maximize_window()          #網頁全螢幕
driver.get(r"http://mops.twse.com.tw/mops/web/t05st22_q1")
years_data_dict = dict()

for i in company_num:
    print(i)
    driver_input = driver.find_element_by_xpath('//*[@id="co_id"]')
    driver_input.send_keys(i)     #輸入公司代號
    driver.find_element_by_xpath("//td[@class='bar01b']//td[2]//div[1]//div[1]//input[1]").click()     #點擊搜尋鍵
    time.sleep(5)
    years_data_dict[105] = [driver.find_element_by_xpath("//div[@id='zoom']/div/center[2]/table/tbody/tr[2]/td[1]").text]
    years_data_dict[105] += [driver.find_element_by_xpath("//div[@id='zoom']/div/center[2]/table/tbody/tr[3]/td[1]").text]
    years_data_dict[105] += [driver.find_element_by_xpath("//div[@id='zoom']/div/center[2]/table/tbody/tr[4]/td[1]").text]
    years_data_dict[105] += [driver.find_element_by_xpath("//div[@id='zoom']/div/center[2]/table/tbody/tr[5]/td[1]").text]
    years_data_dict[105] += [driver.find_element_by_xpath("//div[@id='zoom']/div/center[2]/table/tbody/tr[6]/td[1]").text]
    years_data_dict[105] += [driver.find_element_by_xpath("//div[@id='zoom']/div/center[2]/table/tbody/tr[7]/td[1]").text]
    years_data_dict[105] += [driver.find_element_by_xpath("//div[@id='zoom']/div/center[2]/table/tbody/tr[8]/td[1]").text]
    years_data_dict[105] += [driver.find_element_by_xpath("//div[@id='zoom']/div/center[2]/table/tbody/tr[9]/td[1]").text]
    years_data_dict[105] += [driver.find_element_by_xpath("//div[@id='zoom']/div/center[2]/table/tbody/tr[10]/td[1]").text]
    years_data_dict[105] += [driver.find_element_by_xpath("//div[@id='zoom']/div/center[2]/table/tbody/tr[11]/td[1]").text]
    years_data_dict[105] += [driver.find_element_by_xpath("//div[@id='zoom']/div/center[2]/table/tbody/tr[12]/td[1]").text]
    years_data_dict[105] += [driver.find_element_by_xpath("//div[@id='zoom']/div/center[2]/table/tbody/tr[13]/td[1]").text]
    years_data_dict[105] += [driver.find_element_by_xpath("//div[@id='zoom']/div/center[2]/table/tbody/tr[14]/td[1]").text]
    years_data_dict[105] += [driver.find_element_by_xpath("//div[@id='zoom']/div/center[2]/table/tbody/tr[15]/td[1]").text]
    years_data_dict[105] += [driver.find_element_by_xpath("//div[@id='zoom']/div/center[2]/table/tbody/tr[16]/td[1]").text]
    years_data_dict[105] += [driver.find_element_by_xpath("//div[@id='zoom']/div/center[2]/table/tbody/tr[17]/td[1]").text]
    years_data_dict[105] += [driver.find_element_by_xpath("//div[@id='zoom']/div/center[2]/table/tbody/tr[18]/td[1]").text]
    years_data_dict[105] += [driver.find_element_by_xpath("//div[@id='zoom']/div/center[2]/table/tbody/tr[19]/td[1]").text]
    years_data_dict[105] += [driver.find_element_by_xpath("//div[@id='zoom']/div/center[2]/table/tbody/tr[20]/td[1]").text]	
    years_data_dict[106] = [driver.find_element_by_xpath("//div[@id='zoom']/div/center[2]/table/tbody/tr[2]/td[2]").text]
    years_data_dict[106] += [driver.find_element_by_xpath("//div[@id='zoom']/div/center[2]/table/tbody/tr[3]/td[2]").text]
    years_data_dict[106] += [driver.find_element_by_xpath("//div[@id='zoom']/div/center[2]/table/tbody/tr[4]/td[2]").text]
    years_data_dict[106] += [driver.find_element_by_xpath("//div[@id='zoom']/div/center[2]/table/tbody/tr[5]/td[2]").text]
    years_data_dict[106] += [driver.find_element_by_xpath("//div[@id='zoom']/div/center[2]/table/tbody/tr[6]/td[2]").text]
    years_data_dict[106] += [driver.find_element_by_xpath("//div[@id='zoom']/div/center[2]/table/tbody/tr[7]/td[2]").text]
    years_data_dict[106] += [driver.find_element_by_xpath("//div[@id='zoom']/div/center[2]/table/tbody/tr[8]/td[2]").text]
    years_data_dict[106] += [driver.find_element_by_xpath("//div[@id='zoom']/div/center[2]/table/tbody/tr[9]/td[2]").text]
    years_data_dict[106] += [driver.find_element_by_xpath("//div[@id='zoom']/div/center[2]/table/tbody/tr[10]/td[2]").text]
    years_data_dict[106] += [driver.find_element_by_xpath("//div[@id='zoom']/div/center[2]/table/tbody/tr[11]/td[2]").text]
    years_data_dict[106] += [driver.find_element_by_xpath("//div[@id='zoom']/div/center[2]/table/tbody/tr[12]/td[2]").text]
    years_data_dict[106] += [driver.find_element_by_xpath("//div[@id='zoom']/div/center[2]/table/tbody/tr[13]/td[2]").text]
    years_data_dict[106] += [driver.find_element_by_xpath("//div[@id='zoom']/div/center[2]/table/tbody/tr[14]/td[2]").text]
    years_data_dict[106] += [driver.find_element_by_xpath("//div[@id='zoom']/div/center[2]/table/tbody/tr[15]/td[2]").text]
    years_data_dict[106] += [driver.find_element_by_xpath("//div[@id='zoom']/div/center[2]/table/tbody/tr[16]/td[2]").text]
    years_data_dict[106] += [driver.find_element_by_xpath("//div[@id='zoom']/div/center[2]/table/tbody/tr[17]/td[2]").text]
    years_data_dict[106] += [driver.find_element_by_xpath("//div[@id='zoom']/div/center[2]/table/tbody/tr[18]/td[2]").text]
    years_data_dict[106] += [driver.find_element_by_xpath("//div[@id='zoom']/div/center[2]/table/tbody/tr[19]/td[2]").text]
    years_data_dict[106] += [driver.find_element_by_xpath("//div[@id='zoom']/div/center[2]/table/tbody/tr[20]/td[2]").text]
    years_data_dict[107] = [driver.find_element_by_xpath("//div[@id='zoom']/div/center[2]/table/tbody/tr[2]/td[3]").text]
    years_data_dict[107] += [driver.find_element_by_xpath("//div[@id='zoom']/div/center[2]/table/tbody/tr[3]/td[3]").text]
    years_data_dict[107] += [driver.find_element_by_xpath("//div[@id='zoom']/div/center[2]/table/tbody/tr[4]/td[3]").text]
    years_data_dict[107] += [driver.find_element_by_xpath("//div[@id='zoom']/div/center[2]/table/tbody/tr[5]/td[3]").text]
    years_data_dict[107] += [driver.find_element_by_xpath("//div[@id='zoom']/div/center[2]/table/tbody/tr[6]/td[3]").text]
    years_data_dict[107] += [driver.find_element_by_xpath("//div[@id='zoom']/div/center[2]/table/tbody/tr[7]/td[3]").text]
    years_data_dict[107] += [driver.find_element_by_xpath("//div[@id='zoom']/div/center[2]/table/tbody/tr[8]/td[3]").text]
    years_data_dict[107] += [driver.find_element_by_xpath("//div[@id='zoom']/div/center[2]/table/tbody/tr[9]/td[3]").text]
    years_data_dict[107] += [driver.find_element_by_xpath("//div[@id='zoom']/div/center[2]/table/tbody/tr[10]/td[3]").text]
    years_data_dict[107] += [driver.find_element_by_xpath("//div[@id='zoom']/div/center[2]/table/tbody/tr[11]/td[3]").text]
    years_data_dict[107] += [driver.find_element_by_xpath("//div[@id='zoom']/div/center[2]/table/tbody/tr[12]/td[3]").text]
    years_data_dict[107] += [driver.find_element_by_xpath("//div[@id='zoom']/div/center[2]/table/tbody/tr[13]/td[3]").text]
    years_data_dict[107] += [driver.find_element_by_xpath("//div[@id='zoom']/div/center[2]/table/tbody/tr[14]/td[3]").text]
    years_data_dict[107] += [driver.find_element_by_xpath("//div[@id='zoom']/div/center[2]/table/tbody/tr[15]/td[3]").text]
    years_data_dict[107] += [driver.find_element_by_xpath("//div[@id='zoom']/div/center[2]/table/tbody/tr[16]/td[3]").text]
    years_data_dict[107] += [driver.find_element_by_xpath("//div[@id='zoom']/div/center[2]/table/tbody/tr[17]/td[3]").text]
    years_data_dict[107] += [driver.find_element_by_xpath("//div[@id='zoom']/div/center[2]/table/tbody/tr[18]/td[3]").text]
    years_data_dict[107] += [driver.find_element_by_xpath("//div[@id='zoom']/div/center[2]/table/tbody/tr[19]/td[3]").text]
    years_data_dict[107] += [driver.find_element_by_xpath("//div[@id='zoom']/div/center[2]/table/tbody/tr[20]/td[3]").text]
	#資料，["負債佔資產比率","長期資金佔不動產廠房及設備比率","流動比率"...]( 字串元素：string )
    years_data_dict.items()
    driver.find_element_by_xpath('//*[@id="co_id"]').click()     #點擊"輸入公司代號之輸入格" -> 消除原先輸入的值

for i in company_num:
    s = Select(driver.find_element_by_id('isnew'))     #選取滾輪
    s.select_by_visible_text("歷史資料")
    #選取滾輪標籤中的(...)
    driver_input.send_keys(i)
    driver.find_element_by_xpath("//input[@id='year']").send_keys("104")     #"年分"輸入104年(因為一次只能獲取前3年的資料)
    driver.find_element_by_xpath("//td[@class='bar01b']//td[2]//div[1]//div[1]//input[1]").click()
    time.sleep(5)
    years_data_dict[102] = [driver.find_element_by_xpath("//div[@id='zoom']/div/center[2]/table/tbody/tr[2]/td[1]").text]
    years_data_dict[102] += [driver.find_element_by_xpath("//div[@id='zoom']/div/center[2]/table/tbody/tr[3]/td[1]").text]
    years_data_dict[102] += [driver.find_element_by_xpath("//div[@id='zoom']/div/center[2]/table/tbody/tr[4]/td[1]").text]
    years_data_dict[102] += [driver.find_element_by_xpath("//div[@id='zoom']/div/center[2]/table/tbody/tr[5]/td[1]").text]
    years_data_dict[102] += [driver.find_element_by_xpath("//div[@id='zoom']/div/center[2]/table/tbody/tr[6]/td[1]").text]
    years_data_dict[102] += [driver.find_element_by_xpath("//div[@id='zoom']/div/center[2]/table/tbody/tr[7]/td[1]").text]
    years_data_dict[102] += [driver.find_element_by_xpath("//div[@id='zoom']/div/center[2]/table/tbody/tr[8]/td[1]").text]
    years_data_dict[102] += [driver.find_element_by_xpath("//div[@id='zoom']/div/center[2]/table/tbody/tr[9]/td[1]").text]
    years_data_dict[102] += [driver.find_element_by_xpath("//div[@id='zoom']/div/center[2]/table/tbody/tr[10]/td[1]").text]
    years_data_dict[102] += [driver.find_element_by_xpath("//div[@id='zoom']/div/center[2]/table/tbody/tr[11]/td[1]").text]
    years_data_dict[102] += [driver.find_element_by_xpath("//div[@id='zoom']/div/center[2]/table/tbody/tr[12]/td[1]").text]
    years_data_dict[102] += [driver.find_element_by_xpath("//div[@id='zoom']/div/center[2]/table/tbody/tr[13]/td[1]").text]
    years_data_dict[102] += [driver.find_element_by_xpath("//div[@id='zoom']/div/center[2]/table/tbody/tr[14]/td[1]").text]
    years_data_dict[102] += [driver.find_element_by_xpath("//div[@id='zoom']/div/center[2]/table/tbody/tr[15]/td[1]").text]
    years_data_dict[102] += [driver.find_element_by_xpath("//div[@id='zoom']/div/center[2]/table/tbody/tr[16]/td[1]").text]
    years_data_dict[102] += [driver.find_element_by_xpath("//div[@id='zoom']/div/center[2]/table/tbody/tr[17]/td[1]").text]
    years_data_dict[102] += [driver.find_element_by_xpath("//div[@id='zoom']/div/center[2]/table/tbody/tr[18]/td[1]").text]
    years_data_dict[102] += [driver.find_element_by_xpath("//div[@id='zoom']/div/center[2]/table/tbody/tr[19]/td[1]").text]
    years_data_dict[102] += [driver.find_element_by_xpath("//div[@id='zoom']/div/center[2]/table/tbody/tr[20]/td[1]").text]
    years_data_dict[103] = [driver.find_element_by_xpath("//div[@id='zoom']/div/center[2]/table/tbody/tr[2]/td[2]").text]
    years_data_dict[103] += [driver.find_element_by_xpath("//div[@id='zoom']/div/center[2]/table/tbody/tr[3]/td[2]").text]
    years_data_dict[103] += [driver.find_element_by_xpath("//div[@id='zoom']/div/center[2]/table/tbody/tr[4]/td[2]").text]
    years_data_dict[103] += [driver.find_element_by_xpath("//div[@id='zoom']/div/center[2]/table/tbody/tr[5]/td[2]").text]
    years_data_dict[103] += [driver.find_element_by_xpath("//div[@id='zoom']/div/center[2]/table/tbody/tr[6]/td[2]").text]
    years_data_dict[103] += [driver.find_element_by_xpath("//div[@id='zoom']/div/center[2]/table/tbody/tr[7]/td[2]").text]
    years_data_dict[103] += [driver.find_element_by_xpath("//div[@id='zoom']/div/center[2]/table/tbody/tr[8]/td[2]").text]
    years_data_dict[103] += [driver.find_element_by_xpath("//div[@id='zoom']/div/center[2]/table/tbody/tr[9]/td[2]").text]
    years_data_dict[103] += [driver.find_element_by_xpath("//div[@id='zoom']/div/center[2]/table/tbody/tr[10]/td[2]").text]
    years_data_dict[103] += [driver.find_element_by_xpath("//div[@id='zoom']/div/center[2]/table/tbody/tr[11]/td[2]").text]
    years_data_dict[103] += [driver.find_element_by_xpath("//div[@id='zoom']/div/center[2]/table/tbody/tr[12]/td[2]").text]
    years_data_dict[103] += [driver.find_element_by_xpath("//div[@id='zoom']/div/center[2]/table/tbody/tr[13]/td[2]").text]
    years_data_dict[103] += [driver.find_element_by_xpath("//div[@id='zoom']/div/center[2]/table/tbody/tr[14]/td[2]").text]
    years_data_dict[103] += [driver.find_element_by_xpath("//div[@id='zoom']/div/center[2]/table/tbody/tr[15]/td[2]").text]
    years_data_dict[103] += [driver.find_element_by_xpath("//div[@id='zoom']/div/center[2]/table/tbody/tr[16]/td[2]").text]
    years_data_dict[103] += [driver.find_element_by_xpath("//div[@id='zoom']/div/center[2]/table/tbody/tr[17]/td[2]").text]
    years_data_dict[103] += [driver.find_element_by_xpath("//div[@id='zoom']/div/center[2]/table/tbody/tr[18]/td[2]").text]
    years_data_dict[103] += [driver.find_element_by_xpath("//div[@id='zoom']/div/center[2]/table/tbody/tr[19]/td[2]").text]
    years_data_dict[103] += [driver.find_element_by_xpath("//div[@id='zoom']/div/center[2]/table/tbody/tr[20]/td[2]").text]
    years_data_dict[104] = [driver.find_element_by_xpath("//div[@id='zoom']/div/center[2]/table/tbody/tr[2]/td[3]").text]
    years_data_dict[104] += [driver.find_element_by_xpath("//div[@id='zoom']/div/center[2]/table/tbody/tr[3]/td[3]").text]
    years_data_dict[104] += [driver.find_element_by_xpath("//div[@id='zoom']/div/center[2]/table/tbody/tr[4]/td[3]").text]
    years_data_dict[104] += [driver.find_element_by_xpath("//div[@id='zoom']/div/center[2]/table/tbody/tr[5]/td[3]").text]
    years_data_dict[104] += [driver.find_element_by_xpath("//div[@id='zoom']/div/center[2]/table/tbody/tr[6]/td[3]").text]
    years_data_dict[104] += [driver.find_element_by_xpath("//div[@id='zoom']/div/center[2]/table/tbody/tr[7]/td[3]").text]
    years_data_dict[104] += [driver.find_element_by_xpath("//div[@id='zoom']/div/center[2]/table/tbody/tr[8]/td[3]").text]
    years_data_dict[104] += [driver.find_element_by_xpath("//div[@id='zoom']/div/center[2]/table/tbody/tr[9]/td[3]").text]
    years_data_dict[104] += [driver.find_element_by_xpath("//div[@id='zoom']/div/center[2]/table/tbody/tr[10]/td[3]").text]
    years_data_dict[104] += [driver.find_element_by_xpath("//div[@id='zoom']/div/center[2]/table/tbody/tr[11]/td[3]").text]
    years_data_dict[104] += [driver.find_element_by_xpath("//div[@id='zoom']/div/center[2]/table/tbody/tr[12]/td[3]").text]
    years_data_dict[104] += [driver.find_element_by_xpath("//div[@id='zoom']/div/center[2]/table/tbody/tr[13]/td[3]").text]
    years_data_dict[104] += [driver.find_element_by_xpath("//div[@id='zoom']/div/center[2]/table/tbody/tr[14]/td[3]").text]
    years_data_dict[104] += [driver.find_element_by_xpath("//div[@id='zoom']/div/center[2]/table/tbody/tr[15]/td[3]").text]
    years_data_dict[104] += [driver.find_element_by_xpath("//div[@id='zoom']/div/center[2]/table/tbody/tr[16]/td[3]").text]
    years_data_dict[104] += [driver.find_element_by_xpath("//div[@id='zoom']/div/center[2]/table/tbody/tr[17]/td[3]").text]
    years_data_dict[104] += [driver.find_element_by_xpath("//div[@id='zoom']/div/center[2]/table/tbody/tr[18]/td[3]").text]
    years_data_dict[104] += [driver.find_element_by_xpath("//div[@id='zoom']/div/center[2]/table/tbody/tr[19]/td[3]").text]
    years_data_dict[104] += [driver.find_element_by_xpath("//div[@id='zoom']/div/center[2]/table/tbody/tr[20]/td[3]").text]
	#取2018年各資料，["負債佔資產比率","長期資金佔不動產廠房及設備比率","流動比率"...]( 字串元素：string )
    driver.find_element_by_xpath('//*[@id="co_id"]').click()

for i in [102,103,104,105,106,107]:
    for j in range(19):
        print(float("".join(years_data_dict[i][j].strip().split(','))), end = " ")

driver.close()