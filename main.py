import script
import time
starttime = time.time()

#example URLs from Futbin. 
url = 'https://www.futbin.com/22/player/371/lionel-messi' 
url2 = 'https://www.futbin.com/22/player/24675/hidetoshi-nakata' 

#Insert urls into list. The number next to it is the price you want to sell the player for
players = [[url,70000],[url2,150000]]


def main():
    while True:
        print('Checking prices....')

        #Check the price of the players in the URL. Sends you an email if the prices are over
        #your target price.
        script.checkPrices(players)

        print('Prices checked!')

        #Decides how often you want to check the player prices
        #currently set to every 600 seconds(10 minutes)
        time.sleep(600.0 - ((time.time() - starttime) % 600.0))

main()