import selenium.common.exceptions
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

PROMISED_DOWN = 90
PROMISED_UP = 90
TWITTER_EMAIL = "kfkozakiewicz@onet.pl"
TWITTER_PASSWORD = "Krzysiu778"


class InternetSpeedTwitterBot:
    def __init__(self, promised_up, promised_down):
        self.promised_up = promised_up
        self.promised_down = promised_down

        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        self.speedtest = webdriver.Chrome(ChromeDriverManager().install())
        self.speedtest.get("https://www.speedtest.net")
        time.sleep(2)
        xpath = '//*[@id="onetrust-accept-btn-handler"]'
        privacy_button = self.speedtest.find_element(By.XPATH, value=xpath)
        privacy_button.click()

        xpath2 = '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a'
        start_test_button = self.speedtest.find_element(By.XPATH, value=xpath2)
        start_test_button.click()

        for i in range(60):
            if i % 10 == 0:
                print(i)
            time.sleep(1)

        test_50_xpath = '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[8]/div/div/p[' \
                        '2]/button'
        self.speedtest.find_element(By.XPATH, value=test_50_xpath).click()

        download_xpath = '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[' \
                         '2]/div[1]/div[1]/div/div[2]/span'
        download = self.speedtest.find_element(By.XPATH, value=download_xpath).text

        upload_xpath = '//*[@id="container"]/div/div[3]/div/div/div/div[2]' \
                       '/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span'
        upload = self.speedtest.find_element(By.XPATH, value=upload_xpath).text

        self.down = download
        self.up = upload

    def tweet_at_provider(self):
        self.twitter = webdriver.Chrome(ChromeDriverManager().install())
        self.twitter.get("https://twitter.com/home")
        time.sleep(5)
        email_input = self.twitter.find_element(By.XPATH, "//*[@id='layers']/div/div/div/div/div/div/div[2]/div["
                                                          "2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div["
                                                          "2]/div/input")
        time.sleep(1)
        email_input.send_keys(TWITTER_EMAIL)
        email_input.send_keys(Keys.ENTER)
        time.sleep(3)

        double_werify = self.twitter.find_element(By.XPATH, "//*[@id='layers']/div/div/div/div/div/div/div[2]/div["
                                                            "2]/div/div/div[2]/div[2]/div[1]/div/div["
                                                            "2]/label/div/div[2]/div/input")

        try:
            double_werify.send_keys("Kristoferkoza")
            double_werify.send_keys(Keys.ENTER)
            time.sleep(3)
        except selenium.common.exceptions.NoSuchElementException:
            pass

        pass_input = self.twitter.find_element(By.XPATH,
                                               "//*[@id='layers']/div/div/div/div/div/div/div[2]/div[2]/div/div/div["
                                               "2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input")
        pass_input.send_keys(TWITTER_PASSWORD)
        pass_input.send_keys(Keys.ENTER)

        time.sleep(3)
        try:
            security = self.twitter.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div['
                                                           '2]/div[2]/div/div[1]/div/div/div/div[1]/div/div/svg')
            security.click()
        except selenium.common.exceptions.NoSuchElementException:
            pass

        try:
            cookies = self.twitter.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div[2]/div[1]/div')
            cookies.click()
        except selenium.common.exceptions.NoSuchElementException:
            pass

        twitter_post_xpath = '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[' \
                             '1]/div/div/div[1]/div[2]/div/div/div/div/div/div/div/div/div/div/div/label/div[' \
                             '1]/div/div/div/div/div/div[2]/div/div/div/div'
        twitter_post = self.twitter.find_element(By.XPATH, twitter_post_xpath)
        twitter_post.send_keys(f"My Current Internet Speed is {self.down} Download and {self.up} Upload")
        time.sleep(3)

        tweet_xpath = '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[' \
                      '1]/div/div/div/div[2]/div[2]/div[2]/div/div/div/div[3]/div/span/span'
        tweet = self.twitter.find_element(By.XPATH, tweet_xpath)
        tweet.click()
        time.sleep(5)
        print("Tweet Done")


Best_Internet_Bot = InternetSpeedTwitterBot(PROMISED_UP, PROMISED_DOWN)
Best_Internet_Bot.get_internet_speed()
if Best_Internet_Bot.up < 100 or Best_Internet_Bot.down < 100:
    Best_Internet_Bot.tweet_at_provider()
