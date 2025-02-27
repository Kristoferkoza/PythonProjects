import requests
import datetime as dt
import math

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
STOCK_API_KEY = "84L6UUMXEKPPX3JA"
NEWS_API_KEY = "c02afe1e11bf4f70904042cd9c189ea2"

## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

# TODO 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries.
#  e.g. [new_value for (key, value) in dictionary.items()]
parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY,
}

data = requests.get(STOCK_ENDPOINT, params=parameters).json()
# print(response.status_code)

# TODO 2. - Get the day before yesterday's closing stock price
today = dt.datetime.today()
yesterday = today - dt.timedelta(days=1)
the_day_before = today - dt.timedelta(days=2)

closing_price = float(data["Time Series (Daily)"][str(yesterday.date())]["4. close"])
# print(closing_price)
closing_price_2 = float(data["Time Series (Daily)"][str(the_day_before.date())]["4. close"])
# print(closing_price_2)

# TODO 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20.
#  Hint: https://www.w3schools.com/python/ref_func_abs.asp
difference = round(math.fabs(closing_price - closing_price_2), 2)

# TODO 4. - Work out the percentage difference in price between closing price yesterday and closing price the day
#  before yesterday.
diff_percentage = round((difference/closing_price_2) * 100, 2)

# TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").
# if diff_percentage >= 5:
#     print("Get News")

## STEP 2: https://newsapi.org/
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.

# TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.
parameters2 = {
    "q": "tesla",
    "from": str(yesterday.date()),
    "sortBy": "publishedAt",
    "apiKey": NEWS_API_KEY,
}

news_response = requests.get(NEWS_ENDPOINT, params=parameters2)
news_data = news_response.json()
# print(news_data)

# TODO 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint:
#  https://stackoverflow.com/questions/509211/understanding-slice-notation
articles = news_data["articles"][0:3]
# print(articles)


## STEP 3: Use twilio.com/docs/sms/quickstart/python
# to send a separate message with each article's title and description to your phone number.

# TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.
new_list = [(article["title"], article["description"]) for article in articles]

if diff_percentage >= 0.5:
    # print("Get News")
    print(new_list)

# TODO 9. - Send each article as a separate message via Twilio.


# Optional TODO: Format the message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
