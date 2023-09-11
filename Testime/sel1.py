from selenium import webdriver
import time
from selenium.webdriver.common.by import By
print("Test alustab:")
driver=webdriver.Chrome()  
driver.maximize_window()

driver.get("https://www.auto24.ee/")
time.sleep(1)
driver.find_element("id", "onetrust-accept-btn-handler").click()

time.sleep(3)

driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[1]/div[2]/div/div[1]/div[2]/div[2]/ul/li[2]/a").click()
time.sleep(2)
driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div[2]/ul/li[3]/a").click()
time.sleep(2)

driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div[2]/ul/li[3]/a").click()
time.sleep(2)
driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/h2/a").click()
time.sleep(2)

driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div[2]/form/div/div/div[2]/div[4]/div/input").send_keys('335')
time.sleep(3)

driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div[2]/form/div/div/div[8]/div[1]/div/input").click()

time.sleep(5)
driver.close()

print("Test oli edukas!")