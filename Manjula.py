from selenium import webdriver
from selenium.webdriver import ActionChains

qspider=webdriver.Chrome(executable_path="C:/Users/Admin/Downloads/chromedriver.exe")
qspider.get("https://phptravels.com/")
qspider.find_element_by_xpath("//a[text()='Login']").click()


c_w=qspider.current_window_handle
w_h=qspider.window_handles

for i in w_h:
    if c_w!=i:
        qspider.switch_to_window(i)


qspider.find_element_by_name("username").send_keys("shivanpuneeth50@gmail.com")


