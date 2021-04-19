from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# 1. pip install selenium
# 2. pip install webdriver_manager


browser = webdriver.Chrome(ChromeDriverManager().install())

browser.get("https://google.com")