from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

ADDING_TIME = 3
PLAYING = True
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://orteil.dashnet.org/experiments/cookie/")

cookie_button = driver.find_element(By.ID, value="cookie")
stores = driver.find_elements(By.CSS_SELECTOR, value="#store div")
store_ids = [store.get_attribute("id") for store in stores]

timeout = time.time() + ADDING_TIME
playing_time = time.time() + 30

for item in store_ids:
    print(item)

while PLAYING:
    cookie_button.click()

    if time.time() > timeout:
        cookies = driver.find_element(By.ID, value="money").text
        if "," in cookies:
            cookies.replace(",", "")
        num_of_cookies = int(cookies)
        all_prices = driver.find_elements(By.CSS_SELECTOR, value="#store b")
        item_prices = []

        for price in all_prices:
            element_text = price.text
            if element_text != "":
                cost = int(element_text.split("-")[1].strip().replace(",", ""))
                item_prices.append(cost)

        prices_dict = {}
        for i in range(len(item_prices)):
            prices_dict[item_prices[i]] = store_ids[i]

        affordable_upgrades = {}
        for cost, id in prices_dict.items():
            if num_of_cookies > cost:
                affordable_upgrades[cost] = id

        highest_possible_upgrade = max(affordable_upgrades.keys())
        pucharse_id = affordable_upgrades[highest_possible_upgrade]
        driver.find_element(By.ID, value=pucharse_id).click()

        timeout = time.time() + ADDING_TIME

    if time.time() > playing_time:
        PLAYING = False
        cookies_per_second = driver.find_element(By.ID, value="cps").text.split(" : ")[1]
        print(cookies_per_second)





