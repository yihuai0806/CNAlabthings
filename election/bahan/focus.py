import selenium
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time as tm
import re
from ftplib import FTP
from datetime import datetime
from glob import glob

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('disable-notifications')
chrome_options.add_argument('hide-scrollbars')
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs",prefs)
driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
driver.set_window_size(800, 600)
url = 'file:///C:/Users/pc/Dropbox/py/medialab/bahan/uselection-focus.html'

while True:
    loopbegin = datetime.now()
    driver.get(url)
    tm.sleep(10)
    driver.get_screenshot_as_file('focus.png')

    file_path = 'focus.png'

    with FTP('172.17.242.151','20090948','u0401006@CNA123') as ftp, open(file_path, 'rb') as file:
        ftp.cwd('/20201103-USelection')
        ftp.storbinary(f'STOR {file_path}', file)
    with FTP('210.69.89.186','20090948','u0401006@CNA123') as ftp, open(file_path, 'rb') as file:
        ftp.cwd('/20201103-USelection')
        ftp.storbinary(f'STOR {file_path}', file)

    print('now sleep')
    tm.sleep(180-(datetime.now()-loopbegin).total_seconds())
