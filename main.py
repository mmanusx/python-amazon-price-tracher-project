# http://myhttpheader.com/ // browser http header bilgilerini almak için
# r=requests.get("http://www.example.com/", headers={"Content-Type":"text"}) // header bu şekilde eklenecek

import requests
import lxml
from bs4 import BeautifulSoup
import smtplib


SMTP_ADDRESS="smtp.gmail.com"
TARGETPRICE = 100
URL = "https://www.amazon.com/dp/B08GC6PL3D/ref=sbl_dpx_kitchen-electric-cookware_B08GC6PL3D_0"
HEADERS={"Accept-Language":"en-US,en;q=0.9,tr-TR;q=0.8,tr;q=0.7",
         "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36",
         "Accept-Encoding":"gzip, deflate",
         "Connection":"keep-alive",
         "Cookie":"PHPSESSID=030rvmo70c1vug7jpcntbm5fh6; _ga=GA1.2.1769518980.1646886944; _gid=GA1.2.589165990.1646886944"}


##################### Get Price Data ################################
response = requests.get(URL, headers=HEADERS)
webpage = response.text
#print(webpage)

soup =BeautifulSoup(webpage, "lxml")
# print(soup.prettify())
price_tag = soup.find(name="span",class_="a-offscreen").getText()
price = float(price_tag.strip("$"))
# print(price)

####################################### Send Email #####################################
# Gmail: smtp.gmail.com, Hotmail: smtp.live.com, Outlook: outlook.office365.com, Yahoo: smtp.mail.yahoo.com
# Disable the Captcha for Gmail account: https://accounts.google.com/DisplayUnlockCaptcha
if price <= TARGETPRICE:
    connection = smtplib.SMTP("SMTP_ADDRESS") # smtplib.SMTP("smtp.gmail.com", port=587) adding port number to
    connection.starttls() # encoding
    connection.login(MY_EMAIL, MY_PASSWORD)
    connection.sendmail(
        from_addr=MY_EMAIL,
        to_addrs=TO_EMAIL,
        msg="Subject: Lower Price Alert\n\n The price of product now under $100"
    )