
import scraper
import emailSender
from datetime import date, datetime


"""
url = 'https://www.futbin.com/22/player/415/erling-haaland' #27500
url2 = 'https://www.futbin.com/22/player/306/ole-gunnar-solskj%C3%A6r'#15500
url3 = 'https://www.futbin.com/22/player/24695/martin-%C3%B8degaard' #275000
players = [[url,27800], [url2,10000], [url3,270000]]
"""

def checkPrices(players):
    listOfURLs = []
    x=0
    currentPrices = []
    sellPrices = []
    message = '\n' + str(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

    #get sell price of players in seperate list
    for i in range(len(players)):
        sellPrices.append(players[i][1])
    #get URLs of players in seperate list
    for i in range(len(players)):
        listOfURLs.append(players[i][0])

    #Get playerinfo and extract their current price
    playerInfo = scraper.getPriceMultiplePlayers(listOfURLs)
    for i in range(len(playerInfo)):
        currentPrices.append(playerInfo[i][1])
    
    for i in range(len(currentPrices)):
        if(currentPrices[i]>sellPrices[i]):
            playerName = (playerInfo[i][0]).encode('utf-8')
            message+='\n'+str(playerName)+' is priced at: '+str(currentPrices[i])
            x+=1
    if(x>0):
            sender = "Email account of sender"
            receiver = "Email account of reciever"
            password = "Password to email account of sender"
            emailSender.sendEmail(sender,receiver,password,message)


