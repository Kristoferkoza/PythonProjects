import selenium.common.exceptions
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

SIMILAR_ACCOUNT = "ambitersi_matematyka"
INSTAGRAM_NAME = "kfkz_korepetycje"
INSTAGRAM_PASSWORD = "Krzysiu778"

instagram = webdriver.Chrome(ChromeDriverManager().install())
instagram.get("https://www.instagram.com/ambitersi_matematyka/")