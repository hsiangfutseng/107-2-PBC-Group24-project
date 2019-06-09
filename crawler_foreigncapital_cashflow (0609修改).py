#from selenium import webdriver
#import time
#from selenium.webdriver.common.keys import Keys #模擬鍵盤操作
#from selenium.webdriver.support.ui import Select


class Crawel():
    def __init__(self):
        pass

    def get_crawler(self):
        from selenium import webdriver
        import time
        from selenium.webdriver.common.keys import Keys  # 模擬鍵盤操作
        from selenium.webdriver.support.ui import Select
        #Good Info (只抓2018的)
        companys = [] #用來存放個間公司代碼的list

        co_id = mainpage.co_id
        com = mainpage.com
        companys.append(co_id)
        for i in range(len(com)):
            companys.append(com[i])

        index = dict() #以指標為key的dict, 裡面放不同公司的資料
        #樣子會是：{'毛利率':[co_id, com1, com2, com3, com4, com5], '淨利率':[同前], '殖利率':[同前], '盈餘分配率':[同前], '股利發放穩定性':[同前], '淨值比(PBR)':[同前], '本益比(PER)':[同前]}

        browser = webdriver.Chrome('/Users/chanpohung/Desktop/chromedriver')
        from bs4 import BeautifulSoup
        url = "https://goodinfo.tw/StockInfo/StockBzPerformance.asp?STOCK_ID="
        index['毛利率'] = []
        index['淨利率'] = []
        index['殖利率'] = []
        index['盈餘分配率'] = []
        index['股利發放穩定性'] = []
        index['淨值比(PBR)'] = []
        index['本益比(PER)'] = []

        for company in companys:
            url1 = url + company
            browser.get(url1)
            #等待頁面加載
            #import time
            time.sleep(4)
            #找想要的
            # bs4 import BeautifulSoup
            soup = BeautifulSoup(browser.page_source, 'html.parser')
            #找指標
            a_tags = soup.select('div#divFinDetail table.solid_1_padding_4_0_tbl tbody tr td')  #標籤名稱.class / 標籤名稱#id屬性

            #毛利率
            for i in range(0, len(a_tags)):
                if a_tags[i].text == "2018":
                    try:
                        tmp = float(a_tags[i+12].text)
                    except Exception as inst:
                        tmp = a_tags[i+12].text
                    index['毛利率'].append(tmp)
                    continue

            #淨利率
            for i in range(0, len(a_tags)):
                if a_tags[i].text == "2018":
                    try:
                        tmp = float(a_tags[i+15].text)
                    except Exception as inst:
                        tmp = a_tags[i+15].text
                    index['淨利率'].append(tmp)
                    continue

            #殖利率
            from selenium.webdriver.common.keys import Keys #模擬鍵盤操作
            browser.find_element_by_xpath("//input[@value='股利統計'][@type='button']").click()
            time.sleep(2)
            soup = BeautifulSoup(browser.page_source, 'html.parser')
            b_tags = soup.select('div#divFinDetail table.solid_1_padding_4_0_tbl tbody tr td')  #標籤名稱.class / 標籤名稱#id屬性

            for i in range(0, len(b_tags)):
                if b_tags[i].text == "2018":
                    try:
                        tmp = float(b_tags[i+15].text)
                    except Exception as inst:
                        tmp = b_tags[i+15].text
                    index['殖利率'].append(tmp)
                    continue

            #盈餘分配率
            for i in range(0, len(b_tags)):
                if b_tags[i].text== "2018":
                    try:
                        tmp = float(b_tags[i+18].text)
                    except Exception as inst:
                        tmp = b_tags[i+18].text
                    index['盈餘分配率'].append(tmp)
                    continue

            #股利發放穩定性(2012~2018年"有發放股利年數")
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

            for i in range(0, len(c_tags)):
                if c_tags[i].text == "2018":
                    try:
                        tmp = float(c_tags[i+16].text)
                    except Exception as inst:
                        tmp = c_tags[i+16].text
                    index['淨值比(PBR)'].append(tmp)
                    break

            #本益比(PER)
            for i in range(0, len(c_tags)):
                if c_tags[i].text== "2018":
                    try:
                        tmp = float(c_tags[i+12].text)
                    except Exception as inst:
                        tmp = c_tags[i+12].text
                    index['本益比(PER)'].append(tmp)
                    break

        #print(companys)
        #print(index)


        #整理排序
        p1_up_rank = []
        for key in index:
            #如果主角是"-", 那個指標就不列入
            if index[key][0] == '-':
                p1_up_rank.append("NA")
                continue

            while '-' in index[key]:
                index[key].remove('-')

            p1_up_targetstock = index[key][0]  # 得到最新的資料以便之後排名用
            index[key].sort()  # 把獲取的資料排序
            if key == '淨值比(PBR)' or key == '本益比(PER)':
                pass
            else:
                index[key].reverse()
            p1_up_rank.append(str(index[key].index(p1_up_targetstock) + 1) + '/' + str(len(index[key])))
        #print('===第一部分上半部照順序的排名===')
        #print(p1_up_rank)
        #print('======')


        #browser = webdriver.Chrome('/Users/chanpohung/Desktop/chromedriver')
        url = "https://goodinfo.tw/StockInfo/StockBzPerformance.asp?STOCK_ID="
        url += co_id
        browser.get(url)
        import time
        time.sleep(4)

        #找指標
        index = dict() #以指標為key的dict, 裡面放不同年份的資料
        year = ["2013","2014","2015","2016","2017","2018"]


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


        #for key in index:
        #    print(key, index[key])


        #整理排序
        p2_up_rank = []
        for key in index:
            #如果主角是"-", 那個指標就不列入
            if index[key][0] == '-':
                p2_up_rank.append("NA")
                continue

            while '-' in index[key]:
                index[key].remove('-')

            p2_up_targetstock = index[key][0]  # 得到最新的資料以便之後排名用
            index[key].sort()  # 把獲取的資料排序
            if key == '淨值比(PBR)' or key == '本益比(PER)':
                pass
            else:
                index[key].reverse()
            p2_up_rank.append(str(index[key].index(p2_up_targetstock) + 1) + '/' + str(len(index[key])))
        #print('===第二部分上半部照順序的排名===')
        #print(p2_up_rank)
        #print('======')

        #browser.maximize_window()  # 網頁全螢幕
        browser.get(r"http://mops.twse.com.tw/mops/web/t05st22_q1")
        years_data_dict = dict()
        # 目標公司各年的指標資料 {"公司代碼":{107:["負債佔資產比率","長期資金佔不動產廠房及設備比率","流動比率"...], 106:[同前]...., 102:[同前]}...}
        files_name = ["負債佔資產比率", "長期資金佔不動產廠房及設備比率", "流動比率", "速動比率", "利息保障倍數", "應收款項週轉率", "平均收現日數", "存貨週轉率", "平均銷貨日數",
                      "不動產廠房及設備週轉率", "總資產週轉率", "資產報酬率", "權益報酬率", "稅前純益佔實收資本比率", "純益率", "每股盈餘", "現金流量比率", "現金流量允當比率", "現金再投資比率"]

        # 爬資料
        for i in companys:
            s = Select(browser.find_element_by_id('isnew'))  # 選取滾輪
            s.select_by_visible_text("歷史資料")
            # 選取滾輪標籤中的(...)
            driver_input = browser.find_element_by_xpath('//*[@id="co_id"]')
            driver_input.send_keys(i)  # 輸入公司代號
            browser.find_element_by_xpath("//input[@id='year']").send_keys("107")  # "年分"輸入104年(因為一次只能獲取前3年的資料)
            browser.find_element_by_xpath("//td[@class='bar01b']//td[2]//div[1]//div[1]//input[1]").click()  # 點擊搜尋鍵
            time.sleep(3)
            years_data_dict[i] = dict()
            for j in range(1, 4):
                years_data_dict[i][j + 2015] = []
                for k in range(2, 21):
                    information = browser.find_element_by_xpath(
                        "//div[@id='zoom']/div/center[2]/table/tbody/tr[" + str(k) + "]/td[" + str(j) + "]").text
                    if information != "NA":
                        try:
                            years_data_dict[i][j + 2015] += [float("".join(information.strip().split(',')))]  # 整理資料並轉換成float
                        except Exception as inst:
                            years_data_dict[i][j + 2015] += ["".join(information.strip().split(','))]
            # 字串元素：float
            browser.find_element_by_xpath('//*[@id="co_id"]').click()  # 點擊"輸入公司代號之輸入格" -> 消除原先輸入的值

            s = Select(browser.find_element_by_id('isnew'))  # 選取滾輪
            s.select_by_visible_text("歷史資料")
            # 選取滾輪標籤中的(...)
            driver_input.send_keys(i)
            browser.find_element_by_xpath("//input[@id='year']").send_keys("104")  # "年分"輸入104年(因為一次只能獲取前3年的資料)
            browser.find_element_by_xpath("//td[@class='bar01b']//td[2]//div[1]//div[1]//input[1]").click()
            time.sleep(3)
            for j in range(1, 4):
                years_data_dict[i][j + 2012] = []
                for k in range(2, 21):
                    information = browser.find_element_by_xpath(
                        "//div[@id='zoom']/div/center[2]/table/tbody/tr[" + str(k) + "]/td[" + str(j) + "]").text
                    if information != "NA":
                        try:
                            years_data_dict[i][j + 2012] += [float("".join(information.strip().split(',')))]
                        except Exception as inst:
                            years_data_dict[i][j + 2012] += ["".join(information.strip().split(','))]
            # 字串元素：float
            browser.find_element_by_xpath('//*[@id="co_id"]').click()

        # 第一部分下半部
        p1_down_rank = []
        objective_company = companys[0]
        for files in range(19):  # files = "負債佔資產比率","長期資金佔不動產廠房及設備比率","流動比率"...
            if isinstance(years_data_dict[objective_company][2018][files], float):
                p1_down_targetstock = years_data_dict[objective_company][2018][files]  # 得到最新的各資料以便之後排名用
            else:
                #print('無資料：' + files_name[files])
                p1_down_rank.append("NA")
                continue

            the_flie = []

            for company in companys:  # 107年各公司資料
                if isinstance(years_data_dict[company][2018][files], float):
                    the_flie.append(years_data_dict[company][2018][files])
            organized_the_flie = sorted(the_flie)  # 把獲取的資料排序

            if files == 7 or files == 9:  # "平均收現日數" 和 "平均銷貨日數" 越低越好
                pass
            else:
                organized_the_flie.reverse()

            p1_down_rank.append(str(organized_the_flie.index(p1_down_targetstock) + 1) + '/' + str(len(organized_the_flie)))

        #print('===第一部分下半部照順序的排名===')
        #print(p1_down_rank)
        #print('======')

        # 第二部分下半部
        p2_down_rank = []
        objective_company = companys[0]
        for files in range(19):  # files = "負債佔資產比率","長期資金佔不動產廠房及設備比率","流動比率"...
            if isinstance(years_data_dict[objective_company][2018][files], float):
                p2_down_targetstock = years_data_dict[objective_company][2018][files]  # 得到最新的各資料以便之後排名用
            the_flie = []
            for over_the_years in range(2013, 2019):  # over_the_years = 102年 到 107年
                if isinstance(years_data_dict[objective_company][over_the_years][files], float):
                    the_flie.append(years_data_dict[objective_company][over_the_years][files])
            organized_the_flie = sorted(the_flie)  # 把獲取的資料排序
            if files == 7 or files == 9:  # "平均收現日數" 和 "平均銷貨日數" 越低越好
                pass
            else:
                organized_the_flie.reverse()
            if organized_the_flie == []:
                #print('無資料：' + files_name[files])
                p2_down_rank.append("NA")
            else:
                p2_down_rank.append(str(organized_the_flie.index(p2_down_targetstock) + 1) + '/' + str(len(organized_the_flie)))

        #print('===第二部分下半部照順序的排名===')
        #print(p2_down_rank)
        #print('======')

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

            #print('===第三部分短中長排名===')
            #print(p3_rank)
            #print('======')


        class Cashflow:  # 抓到現金流量的class

            def __init__(self, com_num):

                self.com_num = com_num

            def get_cashflow(self):  # 抓到我要的值

                self.get_cashflow_web = browser.get('https://goodinfo.tw/StockInfo/StockDetail.asp?STOCK_ID=' + str(self.com_num))

                time.sleep(3)

                self.co_name = browser.find_element_by_xpath('/html/body/table[2]/tbody/tr/td[3]/table/tbody/tr[2]/td[3]'
                                                             '/table[1]/tbody/tr[2]/td[2]').text
                self.revenue = browser.find_element_by_xpath('//*[@id="FINANCE_INCOME_M"]/tbody/tr[5]/td[2]').text
                self.industry = browser.find_element_by_xpath('/html/body/table[2]/tbody/tr/td[3]/table/tbody/tr[2]/td[3]'
                                                             '/table[1]/tbody/tr[3]/td[2]').text
                self.capitalamount = browser.find_element_by_xpath('/html/body/table[2]/tbody/tr/td[3]/table/tbody/tr[2]'
                                                                  '/td[3]/table[1]/tbody/tr[5]/td[2]/nobr').text
                self.business_cashflow = browser.find_element_by_xpath('//*[@id="FINANCE_CF_M"]/tbody/tr[5]/td[2]').text
                self.investment_cashflow = browser.find_element_by_xpath('//*[@id="FINANCE_CF_M"]/tbody/tr[5]/td[3]').text
                self.credit_cashflow = browser.find_element_by_xpath('//*[@id="FINANCE_CF_M"]/tbody/tr[5]/td[4]').text


            def print_cashflow(self):  # 把資料如果超過千億會有的逗號移掉並印出對應意義

                #print('產業別：' + self.industry)
                #print('資本額：' + self.capitalamount)
                #print('營業額：' + self.revenue + '億')

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
                self.company_status = str()

                if business >= 0 and investment >= 0 and credit >= 0:

                    self.company_status += '準備未來大規模投資'

                elif business >= 0 and investment >= 0 and credit < 0:

                    self.company_status += '正在改善財務狀況'

                elif business >= 0 and investment < 0 and credit >= 0:

                    self.company_status += '正在積極擴張'

                elif business >= 0 and investment < 0 and credit < 0:

                    self.company_status += '目前賺很多'

                elif business < 0 and investment >= 0 and credit >= 0:

                    self.company_status += '公司出狀況了'

                if business < 0 and investment >= 0 and credit < 0:

                    self.company_status += '公司以前可能有很多資產'

                if business < 0 and investment < 0 and credit >= 0:

                    self.company_status += '公司很看好自己的未來'

                if business < 0 and investment < 0 and credit < 0:

                    self.company_status += '公司手頭現金可能很多'

        self.p3_rank = []

        for i in ['DATE', 'WEEK', 'MONTH']:
            sf = Foreigncapital(co_id,i)
            sf.get_fcdriver()
            sf.get_fc()
            sf.print_fc()
            self.p3_rank.append(sf.p3_rank)

          # 執行上面的class
        fc_fuc_all()
        c = Cashflow(co_id)
        c.get_cashflow()
        c.print_cashflow()

        self.p1_rank = p1_up_rank + p1_down_rank
        self.p2_rank = p2_up_rank + p2_down_rank

          # ========算總分=======

        self.p1_point = []
        self.p2_point = []
        self.p3_point = []
        w = 0
        section_point = [2, 2, 6]

        for j in [self.p1_rank, self.p2_rank, self.p3_rank]:
            point_list = []
            for i in range(len(j)):
                try:
                    b = j[i].split('/')
                    point_list.append((float(float(b[1]) - float(b[0])) / (float(b[1]) - 1)) * section_point[w])
                except:
                    point_list.append('NA')

            w += 1
            if w == 1:
                self.p1_point += point_list
            elif w == 2:
                self.p2_point += point_list
            elif w == 3:
                self.p3_point += point_list

        self.sum_p1_point = 0
        self.total_p1_point = 0
        self.sum_p2_point = 0
        self.total_p2_point = 0
        self.sum_p3_point = 0
        self.total_p3_point = 0
        self.final_sum_point = 0
        self.adjust_factor = 0
        w_2 = 0

        for k in [self.p1_point, self.p2_point, self.p3_point]:

            sum_point = 0
            total_point = 0
            for i in range(len(k)):
                if k[i] != 'NA':
                    sum_point += k[i]
                    total_point += section_point[w_2]
            w_2 += 1

            if w_2 == 1:
                self.sum_p1_point += sum_point
                self.total_p1_point += total_point
            elif w_2 == 2:
                self.sum_p2_point += sum_point
                self.total_p2_point += total_point
            elif w_2 == 3:
                self.sum_p3_point += sum_point
                self.total_p3_point += total_point
        self.adjust_factor += 100 / (self.total_p1_point+self.total_p2_point+self.total_p3_point)
        self.final_sum_point += (self.sum_p1_point+self.sum_p2_point+self.sum_p3_point) * self.adjust_factor

  # ===========算p1各項總分==========
        # 其他財務指標
        self.p1_other_sum_point = 0
        self.p1_other_total_point = 0
        for i in self.p1_point[0:7]:
            if i != 'NA':
                self.p1_other_sum_point += i * self.adjust_factor
                self.p1_other_total_point += section_point[0] * self.adjust_factor
        # 財務結構指標
        self.p1_finance_sum_point = 0
        self.p1_finance_total_point = 0
        for i in self.p1_point[7:9]:
            if i != 'NA':
                self.p1_finance_sum_point += i * self.adjust_factor
                self.p1_finance_total_point += section_point[0] * self.adjust_factor
        # 償還能力指標
        self.p1_payback_sum_point = 0
        self.p1_payback_total_point = 0
        for i in self.p1_point[9:12]:
            if i != 'NA':
                self.p1_payback_sum_point += i * self.adjust_factor
                self.p1_payback_total_point += section_point[0] * self.adjust_factor
        # 經營能力指標
        self.p1_business_sum_point = 0
        self.p1_business_total_point = 0
        for i in self.p1_point[12:18]:
            if i != 'NA':
                self.p1_business_sum_point += i * self.adjust_factor
                self.p1_business_total_point += section_point[0] * self.adjust_factor
        # 獲利能力指標
        self.p1_earning_sum_point = 0
        self.p1_earning_total_point = 0
        for i in self.p1_point[18:23]:
            if i != 'NA':
                self.p1_earning_sum_point += i * self.adjust_factor
                self.p1_earning_total_point += section_point[0] * self.adjust_factor
        # 現金流量指標
        self.p1_cashflow_sum_point = 0
        self.p1_cashflow_total_point = 0
        for i in self.p1_point[23:26]:
            if i != 'NA':
                self.p1_cashflow_sum_point += i * self.adjust_factor
                self.p1_cashflow_total_point += section_point[0] * self.adjust_factor

  # =========算p2各項總分==========
        # 其他財務指標
        self.p2_other_sum_point = 0
        self.p2_other_total_point = 0
        for i in self.p2_point[0:6]:
            if i != 'NA':
                self.p2_other_sum_point += i * self.adjust_factor
                self.p2_other_total_point += section_point[1] * self.adjust_factor
        # 財務結構指標
        self.p2_finance_sum_point = 0
        self.p2_finance_total_point = 0
        for i in self.p2_point[6:8]:
            if i != 'NA':
                self.p2_finance_sum_point += i * self.adjust_factor
                self.p2_finance_total_point += section_point[1] * self.adjust_factor
        # 償還能力指標
        self.p2_payback_sum_point = 0
        self.p2_payback_total_point = 0
        for i in self.p2_point[8:11]:
            if i != 'NA':
                self.p2_payback_sum_point += i * self.adjust_factor
                self.p2_payback_total_point += section_point[1] * self.adjust_factor
        # 經營能力指標
        self.p2_business_sum_point = 0
        self.p2_business_total_point = 0
        for i in self.p2_point[11:17]:
            if i != 'NA':
                self.p2_business_sum_point += i * self.adjust_factor
                self.p2_business_total_point += section_point[1] * self.adjust_factor
        # 獲利能力指標
        self.p2_earning_sum_point = 0
        self.p2_earning_total_point = 0
        for i in self.p2_point[17:22]:
            if i != 'NA':
                self.p2_earning_sum_point += i * self.adjust_factor
                self.p2_earning_total_point += section_point[1] * self.adjust_factor
        # 現金流量指標
        self.p2_cashflow_sum_point = 0
        self.p2_cashflow_total_point = 0
        for i in self.p2_point[22:25]:
            if i != 'NA':
                self.p2_cashflow_sum_point += i * self.adjust_factor
                self.p2_cashflow_total_point += section_point[1] * self.adjust_factor

        self.co_id_f = co_id
        self.co_name_f = '公司名稱：' + c.co_name
        self.revenue_f = '營業額：' + c.revenue + '億'
        self.capitalamount_f = '資本額：' + c.capitalamount
        self.industry_f = '產業別：' + c.industry
        self.company_status_f = c.company_status

        self.final_sum_point_f = self.final_sum_point
        self.sum_p1_point_f = '%.1f' % (self.sum_p1_point * self.adjust_factor)
        self.sum_p2_point_f = '%.1f' % (self.sum_p2_point * self.adjust_factor)
        self.sum_p3_point_f = '%.1f' % (self.sum_p3_point * self.adjust_factor)

        self.p1_rank_f = self.p1_rank
        self.p2_rank_f = self.p2_rank
        self.p3_rank_f = self.p3_rank

        self.p1_finance_sum_point_f = str('%.1f' % self.p1_finance_sum_point) + '/' + str('%.1f' % self.p1_finance_total_point)
        self.p1_payback_sum_point_f = str('%.1f' % self.p1_payback_sum_point) + '/' + str('%.1f' % self.p1_payback_total_point)
        self.p1_business_sum_point_f = str('%.1f' % self.p1_business_sum_point) + '/' + str('%.1f' % self.p1_business_total_point)
        self.p1_earning_sum_point_f = str('%.1f' % self.p1_earning_sum_point) + '/' + str('%.1f' % self.p1_earning_total_point)
        self.p1_cashflow_sum_point_f = str('%.1f' % self.p1_cashflow_sum_point) + '/' + str('%.1f' % self.p1_cashflow_total_point)
        self.p1_other_sum_point_f = str('%.1f' % self.p1_other_sum_point) + '/' + str('%.1f' % self.p1_other_total_point)

        self.p2_finance_sum_point_f = str('%.1f' % self.p2_finance_sum_point) + '/' + str('%.1f' % self.p2_finance_total_point)
        self.p2_payback_sum_point_f = str('%.1f' % self.p2_payback_sum_point) + '/' + str('%.1f' % self.p2_payback_total_point)
        self.p2_business_sum_point_f = str('%.1f' % self.p2_business_sum_point) + '/' + str('%.1f' % self.p2_business_total_point)
        self.p2_earning_sum_point_f = str('%.1f' % self.p2_earning_sum_point) + '/' + str('%.1f' % self.p2_earning_total_point)
        self.p2_cashflow_sum_point_f = str('%.1f' % self.p2_cashflow_sum_point) + '/' + str('%.1f' % self.p2_cashflow_total_point)
        self.p2_other_sum_point_f = str('%.1f' % self.p2_other_sum_point) + '/' + str('%.1f' % self.p2_other_total_point)

        self.p3_point_s = '%.1f' % (self.p3_point[0] * self.adjust_factor)
        self.p3_point_m = '%.1f' % (self.p3_point[1] * self.adjust_factor)
        self.p3_point_l = '%.1f' % (self.p3_point[2] * self.adjust_factor)

        c.print_cashflow()
        browser.close()

import tkinter as tk
import tkinter.font as tkFont


class Window1(tk.Frame):

    def __init__(self):
        tk.Frame.__init__(self)
        self.grid()
        self.create_widgets1()

    def create_widgets1(self):
        font1 = tkFont.Font(size=24, family= 'CourierNew')
        font2 = tkFont.Font(size=18, family='CourierNew')
    #Build Object/建立物件
        self.stuck_number = tk.Text(self, height = 2, width = 16)
        self.company_name = tk.Label(self, height=4, width=48, bg='lightsteelblue', text="")
        self.blank1 = tk.Label(self, height=2, width=48, text="")
        self.bar_chart = tk.Label(self, height=10, width=48, bg='lightsteelblue', text="")
        self.blank2 = tk.Label(self, height=2, width=48, text="")
        self.profitability = tk.Label(self, height=6, width=58, bg='LightSalmon', text="\t\t獲利能力\n\t\t------------------------------\n\t\t產業              期間\n\n\t\t1/k               3/n")
        self.fin_structure = tk.Label(self, height=6, width=58, bg='LightSalmon', text="\t\t財務結構\n\t\t------------------------------\n\t\t產業              期間\n\n\t\t1/k               3/n")
        self.profitability2 = tk.Label(self, height=6, width=58, bg='LightSalmon', text="\t\t獲利能力\n\t\t------------------------------\n\t\t短\t中\t長\n\n\t\t1/k\t3/k\t1\k")
        self.rank = tk.Label(self, height=11, width=9, bg='lightsteelblue', text="各\n項\n排\n名",font = font1)
        self.total_scores = tk.Label(self, height=2, width=34, bg='LightSalmon', text="\t66",font=font1)
        self.stuck_number2 = tk.Text(self, height=2, width=30)
        self.total_points = tk.Label(self, height=2, width=8, bg='lightsteelblue', text="總分",font = font1)
        self.turnover = tk.Label(self, height=4, width=34, bg='lightsteelblue', text= "營業額:xxx億\n資本額:xxx億\n所屬產業類別:xxx產業",font=font1)
        self.txt = tk.Label(self, height=1, width=34, bg='lightsteelblue', text="文字",font=font1)
        self.management_capacity = tk.Label(self, height=6, width=60, bg='LightSalmon', text="\t\t\t\t   經營能力\n\t\t\t\t   ------------------------------\n\t\t\t\t   產業              期間\n\n\t\t\t\t   1/k               3/n")
        self.debt = tk.Label(self, height=6, width=30, bg='bisque', text="債償能力\n------------------------------\n產業              期間\n\n1/k               3/n")
        self.others = tk.Label(self, height=6, width=60, bg='LightSalmon', text="\t\t\t\t   其他指標\n\t\t\t\t   ------------------------------\n\t\t\t\t   產業              期間\n\n\t\t\t\t   1/k               3/n")
        self.cash_flow = tk.Label(self, height=6, width=30, bg='bisque', text="現金流量\n------------------------------\n產業              期間\n\n1/k               3/n")
        self.final_rank = tk.Label(self, height=6, width=30, bg='bisque', text="總排名\n------------------------------\n產業              期間\n\n1/k               3/n")
        self.btn1 = tk.Button(self, height=4, width=32, text="ENTER",command=self.run_btn1)
        self.btn2 = tk.Button(self, height=3, width=16, text="NEXT PAGE", command= self.run_secondpage) # 觸發視窗
    #Assign Position/指定位置
        self.stuck_number.grid(row=1, column=0, sticky=tk.W)
        self.company_name.grid(row=3, column=0,sticky=tk.W)
        self.blank1.grid(row=4, column=0,sticky=tk.W)
        self.bar_chart.grid(row=5, column=0,sticky=tk.W)
        self.blank2.grid(row=6, column=0,sticky=tk.W)
        self.rank.grid(row=7,column=0,rowspan=5,sticky=tk.W)
        self.fin_structure.grid(row=7, column=0, sticky=tk.NW)
        self.profitability.grid(row=9, column=0,sticky=tk.W)
        self.profitability2.grid(row=11, column=0, sticky=tk.SW)
        self.total_points.grid(row=3, column=2, sticky=tk.W)
        self.total_scores.grid(row=3, column=2, sticky=tk.W)
        self.stuck_number2.grid(row=1, column=2,columnspan=1, sticky=tk.W)
        self.turnover.grid(row=5, column=2, sticky=tk.NW)
        self.txt.grid(row=5, column=2, sticky=tk.SW)
        self.debt.grid(row=7, column=2, sticky=tk.NW)
        self.management_capacity.grid(row=7, column=2, sticky=tk.NW)
        self.cash_flow.grid(row=9, column=2, sticky=tk.W)
        self.others.grid(row=9, column=2, sticky=tk.W)
        self.final_rank.grid(row=11, column=2, sticky=tk.SW)
        self.btn1.grid(row=1, column=3,sticky=tk.S)
        self.btn2.grid(row=12, column=0, sticky=tk.NW)

    """用按鈕觸發新視窗的函數"""
    def run_secondpage(self):
        self.destroy()
        secondpage = Window2()
        secondpage.master.title("secondpage")
        secondpage.mainloop()

    def run_btn1(self):
        self.co_id = self.stuck_number.get('1.0', tk.END)
        com1 = self.stuck_number2.get('1.0', tk.END)
        self.com = com1.split(',')
        self.com[len(self.com) - 1] = self.com[len(self.com) - 1][0:4]
        k = Crawel()
        k.get_crawler()

        font1 = tkFont.Font(size=24, family='CourierNew')
        # Build Object/建立物件
        self.stuck_number = tk.Text(self, height=2, width=16)
        self.company_name = tk.Label(self, height=4, width=48, bg='lightsteelblue', text=self.co_id + k.co_name_f)
        self.blank1 = tk.Label(self, height=2, width=48, text="")
        self.bar_chart = tk.Label(self, height=10, width=48, bg='lightsteelblue', text="")
        self.blank2 = tk.Label(self, height=2, width=48, text="")
        self.profitability = tk.Label(self, height=6, width=58, bg='LightSalmon',
                                      text="\t\t獲利能力\n\t\t------------------------------\n\t\t產業              期間\n\n\t\t"
                                           +k.p1_earning_sum_point_f+"               "+k.p2_earning_sum_point_f)
        self.fin_structure = tk.Label(self, height=6, width=58, bg='LightSalmon',
                                      text="\t\t財務結構\n\t\t------------------------------\n\t\t產業              期間\n\n\t\t"
                                           +k.p1_finance_sum_point_f+"               "+k.p2_finance_sum_point_f)
        self.profitability2 = tk.Label(self, height=6, width=58, bg='LightSalmon',
                                       text="\t\t外資持股比率\n\t\t------------------------------\n\t\t短\t中\t長\n\n\t\t"
                                            +k.p3_point_s+"\t"+k.p3_point_m+"\t"+k.p3_point_l)
        self.rank = tk.Label(self, height=11, width=9, bg='lightsteelblue', text="各\n項\n排\n名", font=font1)
        self.total_scores = tk.Label(self, height=2, width=34, bg='LightSalmon', text="\t"+str(k.final_sum_point_f), font=font1)
        self.stuck_number2 = tk.Text(self, height=2, width=30)
        self.total_points = tk.Label(self, height=2, width=8, bg='lightsteelblue', text="總分", font=font1)
        self.turnover = tk.Label(self, height=4, width=34, bg='LightSalmon', text=k.revenue_f+"\n"+k.capitalamount_f+"\n"+k.industry_f,
                                 font=font1)
        self.txt = tk.Label(self, height=1, width=34, bg='LightSalmon', text=k.company_status_f, font=font1)
        self.management_capacity = tk.Label(self, height=6, width=60, bg='LightSalmon',
                                            text="\t\t\t\t   經營能力\n\t\t\t\t   ------------------------------\n\t\t\t\t   產業              期間\n\n\t\t\t\t   "
                                                 +k.p1_business_sum_point_f+"               "+k.p2_business_sum_point_f)
        self.debt = tk.Label(self, height=6, width=30, bg='bisque',
                             text="債償能力\n------------------------------\n產業              期間\n\n1"
                                  +k.p1_payback_sum_point_f+"               "+k.p2_payback_sum_point_f)
        self.others = tk.Label(self, height=6, width=60, bg='LightSalmon',
                               text="\t\t\t\t   其他指標\n\t\t\t\t   ------------------------------\n\t\t\t\t   產業              期間\n\n\t\t\t\t   "
                                    +k.p1_other_sum_point_f+"               "+k.p2_other_sum_point_f)
        self.cash_flow = tk.Label(self, height=6, width=30, bg='bisque',
                                  text="現金流量\n------------------------------\n產業              期間\n\n"
                                       +k.p1_cashflow_sum_point_f+"               "+k.p2_cashflow_sum_point_f)
        self.final_rank = tk.Label(self, height=6, width=30, bg='bisque',
                                   text="總排名\n------------------------------\n產業              期間\n\n"
                                        +k.sum_p1_point_f+"               "+k.sum_p2_point_f)

        # Assign Position/指定位置
        self.stuck_number.grid(row=1, column=0, sticky=tk.W)
        self.company_name.grid(row=3, column=0, sticky=tk.W)
        self.blank1.grid(row=4, column=0, sticky=tk.W)
        self.bar_chart.grid(row=5, column=0, sticky=tk.W)
        self.blank2.grid(row=6, column=0, sticky=tk.W)
        self.rank.grid(row=7, column=0, rowspan=5, sticky=tk.W)
        self.fin_structure.grid(row=7, column=0, sticky=tk.NW)
        self.profitability.grid(row=9, column=0, sticky=tk.W)
        self.profitability2.grid(row=11, column=0, sticky=tk.SW)
        self.total_points.grid(row=3, column=2, sticky=tk.W)
        self.total_scores.grid(row=3, column=2, sticky=tk.W)
        self.stuck_number2.grid(row=1, column=2, columnspan=1, sticky=tk.W)
        self.turnover.grid(row=5, column=2, sticky=tk.NW)
        self.txt.grid(row=5, column=2, sticky=tk.SW)
        self.debt.grid(row=7, column=2, sticky=tk.NW)
        self.management_capacity.grid(row=7, column=2, sticky=tk.NW)
        self.cash_flow.grid(row=9, column=2, sticky=tk.W)
        self.others.grid(row=9, column=2, sticky=tk.W)
        self.final_rank.grid(row=11, column=2, sticky=tk.SW)


class Window2(tk.Frame):

    def __init__(self):
        tk.Frame.__init__(self)
        self.grid()
        self.create_widgets2()

    def create_widgets2(self):

        """Build Object/建立物件"""
    # 上方標題
        self.block_nmae = tk.Label(self, height=4, width=70, bg='skyblue', text="細項排名")
        self.item_name = tk.Label(self, height=2, width=10, bg='lime', text="項目")
        self.index_name = tk.Label(self, height=2, width=40, bg='blue', text="指標名稱")
        self.industry = tk.Label(self, height=2, width=10, bg='lime', text="產業")
        self.period = tk.Label(self, height=2, width=10, bg='blue', text="期間")

    # 左邊標題
        self.common_item = tk.Label(self, height=6, width=10, bg='lightsteelblue', text="常見\n指標")
        self.financial_structure = tk.Label(self, height=3, width=10, bg='lightsteelblue', text="財務\n結構")
        self.repay_capability = tk.Label(self, height=3, width=10, bg='lightsteelblue', text="償還\n能力")
        self.operate_capability = tk.Label(self, height=6, width=10, bg='lightsteelblue', text="經營\n能力")
        self.profit_capability = tk.Label(self, height=4, width=10, bg='lightsteelblue', text="獲利\n能力")
        self.cashflow = tk.Label(self, height=5, width=10, bg='lightsteelblue', text="現金\n流量")

    # 細項指標
        self.index1 = tk.Label(self, height=1, width=70, bg='green', text="淨利率")
        self.index2 = tk.Label(self, height=1, width=70, bg='green', text="毛利率")
        self.index3 = tk.Label(self, height=1, width=70, bg='green', text="殖利率")
        self.index4 = tk.Label(self, height=1, width=70, bg='green', text="股利發放穩定性")
        self.index5 = tk.Label(self, height=1, width=70, bg='green', text="盈餘分配率")
        self.index6 = tk.Label(self, height=1, width=70, bg='green', text="淨值比")
        self.index7 = tk.Label(self, height=1, width=70, bg='green', text="本益比")
        self.index8 = tk.Label(self, height=1, width=70, bg='green', text="負債占資產比率(%)")
        self.index9 = tk.Label(self, height=1, width=70, bg='green', text="長期資金站不動產廠房及設備比率(%)")
        self.index10 = tk.Label(self, height=1, width=70, bg='green', text="流動比率(%)")
        self.index11 = tk.Label(self, height=1, width=70, bg='green', text="速動比率(%)")
        self.index12 = tk.Label(self, height=1, width=70, bg='green', text="利息保障倍數(%)")
        self.index13 = tk.Label(self, height=1, width=70, bg='green', text="應收款項週轉率(次)")
        self.index14 = tk.Label(self, height=1, width=70, bg='green', text="平均收現日數")
        self.index15 = tk.Label(self, height=1, width=70, bg='green', text="存貨週轉率(次)")
        self.index16 = tk.Label(self, height=1, width=70, bg='green', text="平均銷貨日數")
        self.index17 = tk.Label(self, height=1, width=70, bg='green', text="不動產廠房及設備週轉率(次)")
        self.index18 = tk.Label(self, height=1, width=70, bg='green', text="總資產週轉率(次)")
        self.index19 = tk.Label(self, height=1, width=70, bg='green', text="資產報酬率(%)")
        self.index20 = tk.Label(self, height=1, width=70, bg='green', text="權益報酬率(%)")
        self.index21 = tk.Label(self, height=1, width=70, bg='green', text="稅前純益佔實收資本比率(%)")
        self.index22 = tk.Label(self, height=1, width=70, bg='green', text="純益率(%)")
        self.index23 = tk.Label(self, height=1, width=70, bg='green', text="每股盈餘(元)")
        self.index24 = tk.Label(self, height=1, width=70, bg='green', text="現金流量比率(%)")
        self.index25 = tk.Label(self, height=1, width=70, bg='green', text="現金流量允當比率(%)")
        self.index26 = tk.Label(self, height=1, width=70, bg='green', text="現金再投資比率(%)")

    # 產業細項
        self.industry1 = tk.Label(self, height=1, width=10, bg='green', text="1/k")
        self.industry2 = tk.Label(self, height=1, width=10, bg='green', text="1/k")
        self.industry3 = tk.Label(self, height=1, width=10, bg='green', text="1/k")
        self.industry4 = tk.Label(self, height=1, width=10, bg='green', text="1/k")
        self.industry5 = tk.Label(self, height=1, width=10, bg='green', text="1/k")
        self.industry6 = tk.Label(self, height=1, width=10, bg='green', text="1/k")
        self.industry7 = tk.Label(self, height=1, width=10, bg='green', text="1/k")
        self.industry8 = tk.Label(self, height=1, width=10, bg='green', text="1/k")
        self.industry9 = tk.Label(self, height=1, width=10, bg='green', text="1/k")
        self.industry10 = tk.Label(self, height=1, width=10, bg='green', text="1/k")
        self.industry11 = tk.Label(self, height=1, width=10, bg='green', text="1/k")
        self.industry12 = tk.Label(self, height=1, width=10, bg='green', text="1/k")
        self.industry13 = tk.Label(self, height=1, width=10, bg='green', text="1/k")
        self.industry14 = tk.Label(self, height=1, width=10, bg='green', text="1/k")
        self.industry15 = tk.Label(self, height=1, width=10, bg='green', text="1/k")
        self.industry16 = tk.Label(self, height=1, width=10, bg='green', text="1/k")
        self.industry17 = tk.Label(self, height=1, width=10, bg='green', text="1/k")
        self.industry18 = tk.Label(self, height=1, width=10, bg='green', text="1/k")
        self.industry19 = tk.Label(self, height=1, width=10, bg='green', text="1/k")
        self.industry20 = tk.Label(self, height=1, width=10, bg='green', text="1/k")
        self.industry21 = tk.Label(self, height=1, width=10, bg='green', text="1/k")
        self.industry22 = tk.Label(self, height=1, width=10, bg='green', text="1/k")
        self.industry23 = tk.Label(self, height=1, width=10, bg='green', text="1/k")
        self.industry24 = tk.Label(self, height=1, width=10, bg='green', text="1/k")
        self.industry25 = tk.Label(self, height=1, width=10, bg='green', text="1/k")
        self.industry26 = tk.Label(self, height=1, width=10, bg='green', text="1/k")

    # 期間細項
        self.period1 = tk.Label(self, height=1, width=10, bg='green', text="3/n")
        self.period2 = tk.Label(self, height=1, width=10, bg='green', text="3/n")
        self.period3 = tk.Label(self, height=1, width=10, bg='green', text="3/n")
        self.period4 = tk.Label(self, height=1, width=10, bg='green', text="3/n")
        self.period5 = tk.Label(self, height=1, width=10, bg='green', text="3/n")
        self.period6 = tk.Label(self, height=1, width=10, bg='green', text="3/n")
        self.period7 = tk.Label(self, height=1, width=10, bg='green', text="3/n")
        self.period8 = tk.Label(self, height=1, width=10, bg='green', text="3/n")
        self.period9 = tk.Label(self, height=1, width=10, bg='green', text="3/n")
        self.period10 = tk.Label(self, height=1, width=10, bg='green', text="3/n")
        self.period11 = tk.Label(self, height=1, width=10, bg='green', text="3/n")
        self.period12 = tk.Label(self, height=1, width=10, bg='green', text="3/n")
        self.period13 = tk.Label(self, height=1, width=10, bg='green', text="3/n")
        self.period14 = tk.Label(self, height=1, width=10, bg='green', text="3/n")
        self.period15 = tk.Label(self, height=1, width=10, bg='green', text="3/n")
        self.period16 = tk.Label(self, height=1, width=10, bg='green', text="3/n")
        self.period17 = tk.Label(self, height=1, width=10, bg='green', text="3/n")
        self.period18 = tk.Label(self, height=1, width=10, bg='green', text="3/n")
        self.period19 = tk.Label(self, height=1, width=10, bg='green', text="3/n")
        self.period20 = tk.Label(self, height=1, width=10, bg='green', text="3/n")
        self.period21 = tk.Label(self, height=1, width=10, bg='green', text="3/n")
        self.period22 = tk.Label(self, height=1, width=10, bg='green', text="3/n")
        self.period23 = tk.Label(self, height=1, width=10, bg='green', text="3/n")
        self.period24 = tk.Label(self, height=1, width=10, bg='green', text="3/n")
        self.period25 = tk.Label(self, height=1, width=10, bg='green', text="3/n")
        self.period26 = tk.Label(self, height=1, width=10, bg='green', text="3/n")
        self.btn3 = tk.Button(self, height=3, width=10, text="Btn3", command= self.run_mainpage) # 觸發視窗


        """Assign Position/指定位置"""
    # 上方標題
        self.block_nmae.grid(row=0, column=0, columnspan=7, sticky=tk.SW + tk.NE)
        self.item_name.grid(row=1, column=0,sticky=tk.W)
        self.index_name.grid(row=1, column=1, columnspan=4, sticky=tk.SW + tk. NE)
        self.industry.grid(row=1, column=5,sticky=tk.W)
        self.period.grid(row=1, column=6,sticky=tk.W)

    # 左邊標題
        self.common_item.grid(row=4,column=0,rowspan=7,sticky=tk.NE +tk.SW)
        self.financial_structure.grid(row=10, column=0, rowspan=3, sticky=tk.NE +tk.SW)
        self.repay_capability.grid(row=13, column=0, rowspan=3, sticky=tk.NE +tk.SW)
        self.operate_capability.grid(row=16, column=0, rowspan=6, sticky=tk.NE +tk.SW)
        self.profit_capability.grid(row=22, column=0, rowspan=4, sticky=tk.NE +tk.SW)
        self.cashflow.grid(row=26, column=0, rowspan=5, sticky=tk.NE +tk.SW)

    #細項指標
        self.index1.grid(row=4, column=1, columnspan=4, sticky=tk.W)
        self.index2.grid(row=5, column=1, columnspan=4, sticky=tk.W)
        self.index3.grid(row=6, column=1, columnspan=4, sticky=tk.W)
        self.index4.grid(row=7, column=1, columnspan=4, sticky=tk.W)
        self.index5.grid(row=8, column=1, columnspan=4, sticky=tk.W)
        self.index6.grid(row=9, column=1, columnspan=4, sticky=tk.W)
        self.index7.grid(row=10, column=1, columnspan=4, sticky=tk.W)
        self.index8.grid(row=11, column=1, columnspan=4, sticky=tk.W)
        self.index9.grid(row=12, column=1, columnspan=4, sticky=tk.W)
        self.index10.grid(row=13, column=1, columnspan=4, sticky=tk.W)
        self.index11.grid(row=14, column=1, columnspan=4, sticky=tk.W)
        self.index12.grid(row=15, column=1, columnspan=4, sticky=tk.W)
        self.index13.grid(row=16, column=1, columnspan=4, sticky=tk.W)
        self.index14.grid(row=17, column=1, columnspan=4, sticky=tk.W)
        self.index15.grid(row=18, column=1, columnspan=4, sticky=tk.W)
        self.index16.grid(row=19, column=1, columnspan=4, sticky=tk.W)
        self.index17.grid(row=20, column=1, columnspan=4, sticky=tk.W)
        self.index18.grid(row=21, column=1, columnspan=4, sticky=tk.W)
        self.index19.grid(row=22, column=1, columnspan=4, sticky=tk.W)
        self.index20.grid(row=23, column=1, columnspan=4, sticky=tk.W)
        self.index21.grid(row=24, column=1, columnspan=4, sticky=tk.W)
        self.index22.grid(row=25, column=1, columnspan=4, sticky=tk.W)
        self.index23.grid(row=26, column=1, columnspan=4, sticky=tk.W)
        self.index24.grid(row=27, column=1, columnspan=4, sticky=tk.W)
        self.index25.grid(row=28, column=1, columnspan=4, sticky=tk.W)
        self.index26.grid(row=29, column=1, columnspan=4, sticky=tk.W)

    #產業細項
        self.industry1.grid(row=4, column=5, sticky=tk.W)
        self.industry2.grid(row=5, column=5, sticky=tk.W)
        self.industry3.grid(row=6, column=5, sticky=tk.W)
        self.industry4.grid(row=7, column=5, sticky=tk.W)
        self.industry5.grid(row=8, column=5, sticky=tk.W)
        self.industry6.grid(row=9, column=5, sticky=tk.W)
        self.industry7.grid(row=10, column=5, sticky=tk.W)
        self.industry8.grid(row=11, column=5, sticky=tk.W)
        self.industry9.grid(row=12, column=5, sticky=tk.W)
        self.industry10.grid(row=13, column=5, sticky=tk.W)
        self.industry11.grid(row=14, column=5, sticky=tk.W)
        self.industry12.grid(row=15, column=5, sticky=tk.W)
        self.industry13.grid(row=16, column=5, sticky=tk.W)
        self.industry14.grid(row=17, column=5, sticky=tk.W)
        self.industry15.grid(row=18, column=5, sticky=tk.W)
        self.industry16.grid(row=19, column=5, sticky=tk.W)
        self.industry17.grid(row=20, column=5, sticky=tk.W)
        self.industry18.grid(row=21, column=5, sticky=tk.W)
        self.industry19.grid(row=22, column=5, sticky=tk.W)
        self.industry20.grid(row=23, column=5, sticky=tk.W)
        self.industry21.grid(row=24, column=5, sticky=tk.W)
        self.industry22.grid(row=25, column=5, sticky=tk.W)
        self.industry23.grid(row=26, column=5, sticky=tk.W)
        self.industry24.grid(row=27, column=5, sticky=tk.W)
        self.industry25.grid(row=28, column=5, sticky=tk.W)
        self.industry26.grid(row=29, column=5, sticky=tk.W)

    #期間細項
        self.period1.grid(row=4, column=6, sticky=tk.W)
        self.period2.grid(row=5, column=6, sticky=tk.W)
        self.period3.grid(row=6, column=6, sticky=tk.W)
        self.period4.grid(row=7, column=6, sticky=tk.W)
        self.period5.grid(row=8, column=6, sticky=tk.W)
        self.period6.grid(row=9, column=6, sticky=tk.W)
        self.period7.grid(row=10, column=6, sticky=tk.W)
        self.period8.grid(row=11, column=6, sticky=tk.W)
        self.period9.grid(row=12, column=6, sticky=tk.W)
        self.period10.grid(row=13, column=6, sticky=tk.W)
        self.period11.grid(row=14, column=6, sticky=tk.W)
        self.period12.grid(row=15, column=6, sticky=tk.W)
        self.period13.grid(row=16, column=6, sticky=tk.W)
        self.period14.grid(row=17, column=6, sticky=tk.W)
        self.period15.grid(row=18, column=6, sticky=tk.W)
        self.period16.grid(row=19, column=6, sticky=tk.W)
        self.period17.grid(row=20, column=6, sticky=tk.W)
        self.period18.grid(row=21, column=6, sticky=tk.W)
        self.period19.grid(row=22, column=6, sticky=tk.W)
        self.period20.grid(row=23, column=6, sticky=tk.W)
        self.period21.grid(row=24, column=6, sticky=tk.W)
        self.period22.grid(row=25, column=6, sticky=tk.W)
        self.period23.grid(row=26, column=6, sticky=tk.W)
        self.period24.grid(row=27, column=6, sticky=tk.W)
        self.period25.grid(row=28, column=6, sticky=tk.W)
        self.period26.grid(row=29, column=6, sticky=tk.W)
        self.btn3.grid(row=30, column=0, sticky=tk.S)

    """用按鈕觸發新視窗的函數"""
    def run_mainpage(self):
        self.destroy()
        mainpage = Window1()
        mainpage.master.title("mainpage")
        mainpage.mainloop()


mainpage = Window1()
mainpage.master.title("mainpage")
mainpage.mainloop()

