from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys

# 1. pip install selenium
# 2. pip install webdriver_manager
# https://selenium-python.readthedocs.io/api.html selenium api link

browser = webdriver.Chrome(ChromeDriverManager().install())


browser.get("https://google.com")

search_bar = browser.find_element_by_class_name("gLFyf")

search_bar.send_keys("hello!")
search_bar.send_keys(Keys.ENTER)

search_result = browser.find_element_by_class_name("g")
print(search_result)
# print(search_bar)

# browser.quit()