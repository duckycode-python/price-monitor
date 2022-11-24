import time
import requests
import telebot
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import threading
bot = telebot.TeleBot("5730193887:AAEoVhwg4aWm5I44Z3IavPOT85K3rOg5Img", parse_mode=None)
token = "5730193887:AAEoVhwg4aWm5I44Z3IavPOT85K3rOg5Img"
chat_id = "5637368190"
def check():
    cenaSplit = [*cenaZL]
    zl = cenaSplit[:3]
    cena = int(f"{zl[0]}{zl[1]}{zl[2]}")
    if cena != 999:
        send_message(f"Price changed.\nNow is {cenaZL}.")
    time.sleep(30)

def send_message(message):
    url = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={message}"
    requests.get(url).json()



@bot.message_handler(commands=['price'])
def send_welcome(message):
    try:
        bot.send_message(chat_id, f"Current price is {cenaZL}.")
    except NameError:
        bot.send_message(chat_id, f"No Data")


def strona():
    global cenaZL
    while True:
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get("https://iiyama-sklep.pl/832-508-g-master-red-eagle-monitor-iiyama-g-master-g2770hsu-b1-27-ips-165hz-08ms-freesync-premium-red-eagle-4948570117741.html#/26-gwarancja-3_lata")
        cenaZL = driver.find_element(By.XPATH, '//span[@itemprop="price"]').text
        check()
        driver.quit()
def polling():
    bot.infinity_polling()

thread1 = threading.Thread(target=strona)
thread1.start()
thread2 = threading.Thread(target=polling)
thread2.start()