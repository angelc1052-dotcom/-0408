# 先導入後面會用到的套件
import requests
from bs4 import BeautifulSoup
import time

# 要爬的股票
stock = ["1101", "2330", "1102"]

for i in range(len(stock)):  # ✅ 縮排修正
    stockid = stock[i]

    # 網址
    url = "https://tw.stock.yahoo.com/quote/" + stockid + ".TW"

    # 發送請求
    r = requests.get(url)

    # 解析 HTML
    soup = BeautifulSoup(r.text, 'html.parser')

    # 抓股價
    price_tag = soup.find(
        'span',
        class_=[
            "Fz(32px) Fw(b) Lh(1) Mend(16px) D(f) Ai(c) C($c-trend-down)",
            "Fz(32px) Fw(b) Lh(1) Mend(16px) D(f) Ai(c)",
            "Fz(32px) Fw(b) Lh(1) Mend(16px) D(f) Ai(c) C($c-trend-up)"
        ]
    )

    # 防呆（避免抓不到）
    if price_tag:
        price = price_tag.getText()
    else:
        price = "抓不到"

    # 訊息
    message = f"股票 {stockid} 即時股價為 {price}"
    print(message)

    # Telegram 設定
    token = "你的token"
    chat_id = "你的id"

    send_url = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={message}"
    requests.get(send_url)

    # 暫停
    time.sleep(3)
