from selenium import webdriver
import time

#Good Info (2012~2018)
co_id = input("輸入四位數股票代號: ")  # 輸入四位數股票代號

from selenium.webdriver.common.keys import Keys #模擬鍵盤操作
browser = webdriver.Chrome('/Users/chanpohung/Desktop/chromedriver')
url = "https://goodinfo.tw/StockInfo/StockBzPerformance.asp?STOCK_ID="
url += co_id
browser.get(url)

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

#整理排序
p2_up_rank = []
for key in index:
    while '-' in index[key]:
        index[key].remove('-')
    if index[key] != []:
        p2_up_targetstock = index[key][0]  # 得到最新的資料以便之後排名用
        index[key].sort()  # 把獲取的資料排序
        if key == '淨值比(PBR)' or key == '本益比(PER)':
            pass
        else:
            index[key].reverse()
        p2_up_rank.append(str(index[key].index(p2_up_targetstock) + 1) + '/' + str(len(index[key])))
    else:
        print('無資料：' + str(key))
print('===第二部分上半部照順序的排名===')
print(p2_up_rank)
print('======')

#driver = webdriver.Chrome('/Users/chanpohung/Documents/chromedriver')

class Foreigncapital:  # 外資持股比率的Class

    def __init__(self, com_num, period):

        self.com_num = com_num
        self.period = period

    def get_fcdriver(self):  # 得到該時期該股號的資料頁面

        self.get_fcdriver = browser.get("https://goodinfo.tw/StockInfo/ShowK_Chart.asp?STOCK_ID="
                                 + str(self.com_num) + "&CHT_CAT2=" + str(self.period) + "")
        self.history_num = []
        self.p3_rank = str()


    def get_fc(self):  # 抓到對應的值

        for j in range(119):
            try:
                if self.period == 'MONTH' or 'WEEK':
                    table_text = browser.find_element_by_xpath('//*[@id="row' + str(j) + '"]/td[17]/nobr').text

                if self.period == 'DATE':
                    table_text = browser.find_element_by_xpath('//*[@id="row' + str(j) + '"]/td[16]/nobr').text

                if table_text != '':
                    self.history_num.append(float(table_text))
            except:
                pass

        self.latest_num = self.history_num[0]  # 得到最新的資料以便之後排名用
        self.history_num.sort()  # 把獲取的資料排序
        self.history_num.reverse()  # 反轉函數讓排名變正確的

    def print_fc(self):  # 抓到最新資料在list裡面的排名然後印出

        if self.period == 'DATE':
            p3d_rank = (str(self.history_num.index(self.latest_num) + 1) + '/'+ str(len(self.history_num)))
            self.p3_rank += (p3d_rank)

        elif self.period == 'WEEK':
            p3w_rank = (str(self.history_num.index(self.latest_num) + 1) + '/' + str(len(self.history_num)))
            self.p3_rank += (p3w_rank)

        elif self.period == 'MONTH':
            p3m_rank = (str(self.history_num.index(self.latest_num) + 1) + '/' + str(len(self.history_num)))
            self.p3_rank += (p3m_rank)


def fc_fuc_all():  # 定義一個函數一次執行三個period

    p3_rank = []

    sf = Foreigncapital(co_id,'DATE')
    sf.get_fcdriver()
    sf.get_fc()
    sf.print_fc()
    p3_rank.append(sf.p3_rank)

    mf = Foreigncapital(co_id,'WEEK')
    mf.get_fcdriver()
    mf.get_fc()
    mf.print_fc()
    p3_rank.append(mf.p3_rank)

    lf = Foreigncapital(co_id,'MONTH')
    lf.get_fcdriver()
    lf.get_fc()
    lf.print_fc()
    p3_rank.append(lf.p3_rank)

    print('===第三部分短中長排名===')
    print(p3_rank)
    print('======')


class Cashflow:  # 抓到現金流量的class

    def __init__(self, com_num):

        self.com_num = com_num

    def get_cashflow(self):  # 抓到我要的值

        self.get_cashflow_web = browser.get('https://goodinfo.tw/StockInfo/StockDetail.asp?STOCK_ID=' + str(self.com_num))

        time.sleep(3)

        self.revenue = browser.find_element_by_xpath('//*[@id="FINANCE_INCOME_M"]/tbody/tr[5]/td[2]').text
        self.industry = browser.find_element_by_xpath('/html/body/table[2]/tbody/tr/td[3]/table/tbody/tr[2]/td[3]'
                                                     '/table[1]/tbody/tr[3]/td[2]').text
        self.capitalamount = browser.find_element_by_xpath('/html/body/table[2]/tbody/tr/td[3]/table/tbody/tr[2]'
                                                          '/td[3]/table[1]/tbody/tr[5]/td[2]/nobr').text
        self.business_cashflow = browser.find_element_by_xpath('//*[@id="FINANCE_CF_M"]/tbody/tr[5]/td[2]').text
        self.investment_cashflow = browser.find_element_by_xpath('//*[@id="FINANCE_CF_M"]/tbody/tr[5]/td[3]').text
        self.credit_cashflow = browser.find_element_by_xpath('//*[@id="FINANCE_CF_M"]/tbody/tr[5]/td[4]').text


    def print_cashflow(self):  # 把資料如果超過千億會有的逗號移掉並印出對應意義

        print('===')
        print('產業別：' + self.industry)
        print('資本額：' + self.capitalamount)
        print('營業額：' + self.revenue + '億')
        print('===')

        if len(self.business_cashflow) > 4:
            business = self.business_cashflow.replace(',', '')
        else:
            business = self.business_cashflow

        if len(self.investment_cashflow) > 4:
            investment = self.investment_cashflow.replace(',', '')
        else:
            investment = self.investment_cashflow

        if len(self.credit_cashflow) > 4:
            credit = self.credit_cashflow.replace(',', '')
        else:
            credit = self.credit_cashflow

        business = float(business)
        investment = float(investment)
        credit = float(credit)

        if business >= 0 and investment >= 0 and credit >= 0:

            print('準備未來大規模投資')

        elif business >= 0 and investment >= 0 and credit < 0:

            print('正在改善財務狀況')

        elif business >= 0 and investment < 0 and credit >= 0:

            print('正在積極擴張')

        elif business >= 0 and investment < 0 and credit < 0:

            print('目前賺很多')

        elif business < 0 and investment >= 0 and credit >= 0:

            print('公司出狀況了')

        if business < 0 and investment >= 0 and credit < 0:

            print('公司以前可能有很多資產')

        if business < 0 and investment < 0 and credit >= 0:

            print('公司很看好自己的未來')

        if business < 0 and investment < 0 and credit < 0:

            print('公司手頭現金可能很多')

  # 執行上面的class
fc_fuc_all()
c = Cashflow(co_id)
c.get_cashflow()
c.print_cashflow()
browser.close()
