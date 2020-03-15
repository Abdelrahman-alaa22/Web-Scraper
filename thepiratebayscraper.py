from selenium import webdriver
from selenium import *
import time
import csv



with open('thepiratebay.csv', 'w') as f:
    f.write("Torrent Name\n")




chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")

driver = webdriver.Chrome("E:/Python Stuff/ChromeDriver/chromedriver.exe", chrome_options=chrome_options)
#driver = webdriver.Chrome("E:/Python Stuff/ChromeDriver/chromedriver.exe")

max_page_nums = 3

for i in range(1, max_page_nums + 1):
    url = f"https://www.xn--thepratebay-fcb.com/proxy/go.php?url=search/Python/{i}/99/0"

    driver.get(url)

    torrent_name = driver.find_elements_by_class_name('detName')


    with open('thepiratebay.csv', 'a') as f:
        for i in torrent_name:
            f.write(i.text + "," + "\n")


driver.close()





