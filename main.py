from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# 1. pip install selenium
# 2. pip install webdriver_manager
# https://selenium-python.readthedocs.io/api.html selenium api link

class GoogleKeywordScreenshooter:
    def __init__(self,keyword,screenshots_dir):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
        self.keyword = keyword
        self.screenshots_dir = screenshots_dir

    def start(self):
        self.browser.get("https://google.com")        
        search_bar = self.browser.find_element_by_class_name("gLFyf")
        search_bar.send_keys(self.keyword)
        search_bar.send_keys(Keys.ENTER)
        try:
        shitty_element = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "g-blk"))
        )

        self.browser.execute_script(
            """ 
            const shitty = arguments[0];
            shitty.parentElement.removeChild(shitty)
        """,
            shitty_element,
        )
        except Exception:
            pass
        search_results = browser.find_elements_by_class_name("g")
        for index, search_result in enumerate(search_results):
        class_name = search_result.get_attribute("class")
        if "kno-kp" not in class_name:
        search_result.screenshot(f"screenshots/{KEYWORD}x{index}.png")

    def finish(self):
        self.browser.quit()


domain_competitors = GoogleKeywordScreenshooter("buy domain", "screenshots")
domain_competitors.start()
domain_competitors.finish()
python_competitors = GoogleKeywordScreenshooter("python book", "screenshots")
python_competitors.start()
python_competitors.finish()






