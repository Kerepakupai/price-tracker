from email import message
from bs4 import BeautifulSoup
import requests
from notification_manager import NotificationManager as notification


TARGET_PRICE = 50000
PRODUCT_URL = "https://www.falabella.com/falabella-cl/product/882681334/La-Martina-Camisa-Casual-Manga-Larga-Hombre/882681340?exp=tienda"


response = requests.get(PRODUCT_URL)
content = response.text

soup = BeautifulSoup(content, "html.parser")

price = int(soup.find("span", id="", class_="copy12").string.split()[1].replace(".", ""))

if price <= TARGET_PRICE:
    message = f"Subject:Falabella Price Alert!\n\n La Martina Camisa Casual Manga Larga Hombre price is now $ {price}\n\n{PRODUCT_URL}".encode('utf-8')

    notification.send_email(
        "ing.davidfuentes@gmail.com",
        message
    )

    print("Message Sent")
    print(message)
