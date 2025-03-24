from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("http://secure-retreat-92358.herokuapp.com")

# articles_numbers = driver.find_element(By.XPATH, value='//*[@id="articlecount"]/a[1]')
# print(articles_numbers.text)

first_name = driver.find_element(By.NAME, value="fName")
first_name.send_keys("Krzysztof")
last_name = driver.find_element(By.NAME, value="lName")
last_name.send_keys("Kozakiewicz")
email = driver.find_element(By.NAME, value="email")
email.send_keys("kfkozakiewicz@onet.pl")

submit_button = driver.find_element(By.CSS_SELECTOR, value="form button")
submit_button.click()