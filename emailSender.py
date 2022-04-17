import smtplib



def sendEmail(sender, reciever, password,msg):
    try:
        smtp_server=smtplib.SMTP("smtp.gmail.com",587)
        smtp_server.ehlo() #setting the ESMTP protocol

        smtp_server.starttls() #setting up to TLS connection
        smtp_server.ehlo() #calling the ehlo() again as encryption happens on calling startttls()

        smtp_server.login(sender,password) #logging into out email id

        smtp_server.sendmail(sender,reciever,msg)
        #print('Successfully the mail is sent ' + msg) #priting a message on sending the mail
        smtp_server.quit()#terminating the server
        print('-----------')
        print('Email sent!')
        print('------------')
    except Exception as e:
        return 'Error: ' + str(e)





