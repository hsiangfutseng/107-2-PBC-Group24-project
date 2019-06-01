from selenium import webdriver
import time
com_num = input('股票代碼：')
print('===')
driver = webdriver.Chrome('/Users/chanpohung/Desktop/chromedriver')


class Foreigncapital:  # 外資持股比率的Class

    def __init__(self, com_num, period):

        self.com_num = com_num
        self.period = period

    def get_fcdriver(self):  # 得到該時期該股號的資料頁面

        self.get_fcdriver = driver.get("https://goodinfo.tw/StockInfo/ShowK_Chart.asp?STOCK_ID="
                                 + str(self.com_num) + "&CHT_CAT2=" + str(self.period) + "")
        self.history_num = []

    def get_fc(self):  # 抓到對應的值

        for j in range(119):
            try:
                if self.period == 'MONTH' or 'WEEK':
                    table_text = driver.find_element_by_xpath('//*[@id="row' + str(j) + '"]/td[17]/nobr').text

                if self.period == 'DATE':
                    table_text = driver.find_element_by_xpath('//*[@id="row' + str(j) + '"]/td[16]/nobr').text

                if table_text != '':
                    self.history_num.append(float(table_text))
            except:
                pass

        self.latest_num = self.history_num[0]  # 得到最新的資料以便之後排名用
        self.history_num.sort()  # 把獲取的資料排序
        self.history_num.reverse()  # 反轉函數讓排名變正確的

    def print_fc(self):  # 抓到最新資料在list裡面的排名然後印出

        print('現在外資持股比率：' + str(self.latest_num) + ' %')

        if self.period == 'DATE':
            print('短期外資持股排名：' + str(self.history_num.index(self.latest_num) + 1) + '/'
                  + str(len(self.history_num)))

        elif self.period == 'WEEK':
            print('中期外資持股排名：' + str(self.history_num.index(self.latest_num) + 1) + '/'
                  + str(len(self.history_num)))

        elif self.period == 'MONTH':
            print('長期外資持股排名：' + str(self.history_num.index(self.latest_num) + 1) + '/'
                  + str(len(self.history_num)))


def fc_fuc_all():  # 定義一個函數一次執行三個period

    sf = Foreigncapital(com_num,'DATE')
    sf.get_fcdriver()
    sf.get_fc()
    sf.print_fc()
    print('===')

    mf = Foreigncapital(com_num,'WEEK')
    mf.get_fcdriver()
    mf.get_fc()
    mf.print_fc()
    print('===')

    lf = Foreigncapital(com_num,'MONTH')
    lf.get_fcdriver()
    lf.get_fc()
    lf.print_fc()


class Cashflow:  # 抓到現金流量的class

    def __init__(self, com_num):

        self.com_num = com_num

    def get_cashflow(self):  # 抓到我要的值

        self.get_cashflow_web = driver.get('https://goodinfo.tw/StockInfo/StockDetail.asp?STOCK_ID=' + str(self.com_num))

        time.sleep(3)

        self.business_cashflow = driver.find_element_by_xpath('//*[@id="FINANCE_CF_M"]/tbody/tr[5]/td[2]').text
        self.investment_cashflow = driver.find_element_by_xpath('//*[@id="FINANCE_CF_M"]/tbody/tr[5]/td[3]').text
        self.credit_cashflow = driver.find_element_by_xpath('//*[@id="FINANCE_CF_M"]/tbody/tr[5]/td[4]').text


    def print_cashflow(self):  # 把資料如果超過千億會有的逗號移掉並印出對應意義

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

            print('公司手頭現金很多')

  # 執行上面的class
fc_fuc_all()
c = Cashflow(com_num)
c.get_cashflow()
c.print_cashflow()
  # 下面還有要排蟲的話就不要執行，不然會error
driver.close()