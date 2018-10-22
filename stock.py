import win32api
import time
import vlc
import sys
from selenium import webdriver

def run():
    if len(sys.argv) != 3:
        print "Usage: python stock.py TSLA 300.00"
    stock = sys.argv[1]
    price = float(sys.argv[2])
    chop = webdriver.ChromeOptions()
    chop.add_extension('Block-image_v1.1.crx')
    chop.add_extension('Adblock-Plus_v3.3.2.crx')
    driver = webdriver.Chrome("chromedriver.exe", chrome_options = chop)
    driver.get("https://finance.yahoo.com/quote/"+stock)
    while 1:
        tag = driver.find_element_by_xpath("//div[@id='quote-market-notice']/../span")
        curprice = float(tag.text)        
        if curprice <= price:
            p = vlc.MediaPlayer("siren.mp3")
            p.play()
            win32api.MessageBox(0, "STOCK PRICE ALERT: CURRENT " + "%.02f"%curprice, stock + " STOCK")
            p.stop()
        time.sleep(3)
    driver.quit()

if __name__ == '__main__':
    run()