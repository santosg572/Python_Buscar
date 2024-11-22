from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from selenium.webdriver.chrome.options import Options

opt = Options()
opt.add_argument("--incognito")

service = Service(executable_path=r'/home/lucrecia/.wdm/drivers/chromedriver/linux64/114.0.5735.90/chromedriver')
driver = webdriver.Chrome(service=service)

driver.get("http://youtube.com")
driver.find_element_by_name("search_query").send_keys("Python")
driver.find_element_by_id("search-icon-legacy").click()
WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.ID, "video-title")))
links = driver.find_elements_by_id("video-title")

for x in links:

    print(x.get_attribute("href"))

