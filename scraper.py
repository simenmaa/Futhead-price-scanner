from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

PATH = "C:\Program Files (x86)\chromedriver.exe"
s = Service(PATH)
op = webdriver.ChromeOptions()
driver = webdriver.Chrome(service = s,options=op)

        

def getPriceOnePlayer(playerURL):
        if not playerURL.startswith('https://www.futbin.com/22/player/'):
                return 'invalid url'
        driver.get(playerURL)
        price = driver.find_element_by_xpath('//*[@id="ps-lowest-1"]').text
        #name = driver.find_element_by_xpath('/html/body/div[8]/div[12]/div[3]/div[1]/ol/li[3]/span').text
        time.sleep
        driver.close()
        price = price.replace(',','')
        price = int(price)
        
        return price

def getPriceMultiplePlayers(listOfURLs):
        listOfPrices = []
        for i in range(len(listOfURLs)):
                if not listOfURLs[i].startswith('https://www.futbin.com/22/player/'):
                        return 'invalid url: '+ str(listOfURLs[i])
        try:
                for i in range(len(listOfURLs)):
                        playerInfo = []
                        driver = webdriver.Chrome(ChromeDriverManager().install())
                        driver.get(listOfURLs[i])
                        
                        price = driver.find_element_by_xpath('//*[@id="ps-lowest-1"]').text
                        name = driver.find_element_by_xpath('/html/body/div[8]/div[12]/div[3]/div[1]/ol/li[3]/span').text
                        time.sleep
                        driver.close()
                        price = price.replace(',','')
                        price = int(price)
                        playerInfo.append(name)
                        playerInfo.append(price)
                        listOfPrices.append(playerInfo)
                
                return listOfPrices
        except:
                return 'An error occured'




