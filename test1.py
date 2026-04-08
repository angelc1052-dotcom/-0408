import requests
from bs4 import BeautifulSoup
import time
import os

stock = ["1101", "2330", "1102"]

token = os.getenv("TOKEN")
chat_id = os.getenv("CHAT_ID")

for stockid in stock:
    url = "https://tw.stock.yahoo.com/quote/" + stockid + ".TW"

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, 'html.parser')

    price_tag = soup.find('span', class_=[
        "Fz(32px) Fw(b) Lh(1) Mend(16px) D(f) Ai(c)",
        "Fz(32px) Fw(b) Lh(1) Mend(16px) D(f) Ai(c) C($c-trend-up)",
        "Fz(32px) Fw(b) Lh(1) Mend(16px) D(f) Ai(c) C($c-trend-down)"
    ])

    if not price_tag:
        print(f"{stockid} 抓不到股價 ❌")
        continue

    price = price_tag.getText()
    message = f"股票 {stockid} 即時股價為 {price}"

    send_url = f"https://api.telegram.org/bot{token}/sendMessage"

    payload = {
        "chat_id": chat_id,
        "text": message
    }

    res = requests.post(send_url, data=payload)

    print("發送結果:", res.text)  # 🔥 關鍵除錯

    time.sleep(3)
