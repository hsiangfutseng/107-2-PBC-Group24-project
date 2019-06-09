	#公司名稱
	from selenium.webdriver.common.keys import Keys #模擬鍵盤操作
	browser.find_element_by_xpath("/html[1]/body[1]/table[2]/tbody[1]/tr[1]/td[3]/table[1]/tbody[1]/tr[1]/td[1]/table[1]/tbody[1]/tr[1]/td[1]/table[1]/tbody[1]/tr[1]/td[1]/nobr[1]/a[1]").click()
	time.sleep(3)
	
	soup = BeautifulSoup(browser.page_source, 'html.parser')
	name_tags = soup.select('table.solid_1_padding_4_3_tbl tbody tr td')
	for i in range(0, len(name_tags)):
		if name_tags[i].text == "名稱":
			#print(name_tags[i+1].text)
			companyName.append(name_tags[i+1].text)