from selenium import webdriver
import time
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())[:10])
id = ['00000000', '11111111'] #学号
password = ['qwer','asdf'] # 密码
bro = webdriver.Chrome(executable_path="E:/chromedriver.exe") #chromedriver的位置，如直接放在E盘下
for i in range(len(id)):
    bro.get('https://newsso.shu.edu.cn/login/eyJ0aW1lc3RhbXAiOjE2MjkwODUwNjIwMzU4NTc4ODUsInJlc3BvbnNlVHlwZSI6ImNvZGUiLCJjbGllbnRJZCI6IldVSFdmcm50bldZSFpmelE1UXZYVUNWeSIsInNjb3BlIjoiMSIsInJlZGlyZWN0VXJpIjoiaHR0cHM6Ly9zZWxmcmVwb3J0LnNodS5lZHUuY24vTG9naW5TU08uYXNweD9SZXR1cm5Vcmw9JTJmRGVmYXVsdC5hc3B4Iiwic3RhdGUiOiIifQ==')
    bro.find_element_by_id("username").send_keys(id[i])
    bro.find_element_by_id("password").send_keys(password[i])
    bro.find_element_by_id("submit").click()
    bro.get('https://selfreport.shu.edu.cn/Default.aspx')
    bro.find_element_by_id('lbReportHistory').click()
    bro.get('https://selfreport.shu.edu.cn/DayReport.aspx?day='+time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())[:10])
    bro.find_element_by_id('p1_ChengNuo-inputEl-icon').click()
    bro.find_element_by_id('fineui_7-inputEl-icon').click()
    time.sleep(1)
    bro.find_element_by_id('fineui_9-inputEl-icon').click()
    bro.find_element_by_id('fineui_12-inputEl-icon').click()
    bro.find_element_by_id('p1_ctl01_btnSubmit').click()
    time.sleep(1)
    bro.find_element_by_id('fineui_36').click()
    time.sleep(2)

