from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys

# 1. pip install selenium
# 2. pip install webdriver_manager
# https://selenium-python.readthedocs.io/api.html selenium api link

KEYWORD = "buy domain"

browser = webdriver.Chrome(ChromeDriverManager().install())


browser.get("https://google.com")

search_bar = browser.find_element_by_class_name("gLFyf")

search_bar.send_keys(KEYWORD)
search_bar.send_keys(Keys.ENTER)

search_results = browser.find_elements_by_class_name("g")

for index, search_result in enumerate(search_results):
    class_name = search_result.get_attribute("class")
    if "kno-kp" not in class_name:
        search_result.screenshot(f"screenshots/{KEYWORD}x{index}.png")

browser.quit()

# browser.quit()