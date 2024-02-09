import requests
from bs4 import BeautifulSoup
import smtplib


headers = {
    'Accept-Language': 'en-US,en;q=0.9',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/121.0.0.0 Safari/537.36',
    }

product_url = "https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"

product = requests.get(url=product_url, headers=headers)


soup = BeautifulSoup(product.text, features="lxml")

price_dollar = soup.find(name="span", class_="a-price-whole")
price_cent = soup.find(name="span", class_="a-price-fraction")
price = float(price_dollar.get_text() + price_cent.get_text())

if price <= 100:
    with smtplib.SMTP(host="smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user="<smtp account email>", password="<smtp password>")
        connection.sendmail(
            from_addr="<from email>",
            to_addrs="<to email address>",
            msg=f"Subject:Amazon Price Alert\n\nInstant Pot Duo Plus 9-in-1 Electric Pressure Cooker, Slow Cooker, "
                f"Rice Cooker, Steamer, Sauté, Yogurt Maker, Warmer & Sterilizer, Includes App With Over 800 Recipes, "
                f"Stainless Steel, 3 Quart is now {price}\n{product_url}".encode('utf8'))
