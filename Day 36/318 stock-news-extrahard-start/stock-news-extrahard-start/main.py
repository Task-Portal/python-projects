from typing import Tuple
from twilio.rest import Client
import requests
from datetime import datetime as d, timedelta

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
API_STOCK_KEY = ""
API_NEWS_KEY = ""

account_sid_twilio = ""
auth_token_twilio = ""

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

def get_time(days:int):
    day = d.now() - timedelta(days=days)
    day = day.strftime("%Y-%m-%d")
    return day


def get_stock()-> Tuple[bool, str,int]:
    params = {
       "function":"TIME_SERIES_DAILY_ADJUSTED",
        "symbol":STOCK,
        "apikey":API_STOCK_KEY
    }
    # replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
    last_day_today = get_time(3)
    last_day_yesterday = get_time(4)
    url = 'https://www.alphavantage.co/query'
    r = requests.get(url,params=params)
    r.raise_for_status()
    data = r.json()
    last_day_today_close = float(data["Time Series (Daily)"][last_day_today]["4. close"])
    last_day_yesterday_close = float( data["Time Series (Daily)"][last_day_yesterday]["4. close"])
    difference = last_day_today_close-last_day_yesterday_close
    percentage = round(difference *100/last_day_today_close)

    if percentage>=1:
        return  True, "🔺",percentage
    else: return False, "🔻",percentage






## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.

def get_news():
    val,pic,percentage = get_stock()
    if  val:
        params={
            "q":COMPANY_NAME,
            "from":get_time(4),
            "sortBy":"popularity",
            "apiKey":API_NEWS_KEY,
            "searchIn":"title,description"

        }
        url = ('https://newsapi.org/v2/everything')

        response = requests.get(url,params=params)
        response.raise_for_status()
        data = response.json()
        arr=[ i for i in data["articles"][:3]]


        messages = [f"{STOCK},{pic},{percentage}%\n. Headline: {i['title']}.\n Brief:{i['description']}.\n url:{i['url']}" for i in arr]


        print(messages)

        if len(messages)>0:
            client = Client(account_sid_twilio, auth_token_twilio)
            for i in messages:
                message = client.messages.create(
                    body=i,
                    from_="",
                    to=""
                )
                print(message.status)


get_news()

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

