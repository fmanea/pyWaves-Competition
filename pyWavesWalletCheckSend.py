import pywaves as pw
import time

time.sleep(0.3)
myAddress = pw.Address(privateKey='4EQByDHFnC7AmeqYxstC4bh52j9ZkTpkEpxh65YjM5F7')
###insert private key here (random private key used here)
tokenNumbers = 0
for p in myAddress.assets():
    myCurrentToken = pw.Asset(p)
    if myCurrentToken.name=='ALAN':
        tokenNumbers = tokenNumbers + 1
    elif myCurrentToken.name=='JOHN':
        tokenNumbers = tokenNumbers + 1
    elif myCurrentToken.name=='VLAD':
        tokenNumbers = tokenNumbers + 1
    elif myCurrentToken.name=='ZIGM':
        tokenNumbers = tokenNumbers + 1
    elif myCurrentToken.name=='YURI':  
        tokenNumbers = tokenNumbers + 1
if tokenNumbers != 5:
    print "the number of found tokens is not 5, it is currenly=",tokenNumbers 
else:
    print "Found all tokens, sending"    
    for p in myAddress.assets():
        myCurrentToken = pw.Asset(p)
        if myCurrentToken.name=='ALAN':
            print "Sending 1 ALAN"
            myAddress.sendAsset(recipient = pw.Address('3PG3JmVh1czUhvg8stVwFY8zXkqVJBqeeJw'), asset = myCurrentToken, amount = 1)
            print "Sent 1 ALAN"
        elif myCurrentToken.name=='JOHN':
            print "Sending 1 JOHN"
            myAddress.sendAsset(recipient = pw.Address('3PG3JmVh1czUhvg8stVwFY8zXkqVJBqeeJw'), asset = myCurrentToken, amount = 1)
            print "Sent 1 JOHN"
        elif myCurrentToken.name=='VLAD':
            print "Sending 1 VLAD"
            myAddress.sendAsset(recipient = pw.Address('3PG3JmVh1czUhvg8stVwFY8zXkqVJBqeeJw'), asset = myCurrentToken, amount = 1)
            print "Sent 1 VLAD"
        elif myCurrentToken.name=='ZIGM':
            print "Sending 1 ZIGM"
            myAddress.sendAsset(recipient = pw.Address('3PG3JmVh1czUhvg8stVwFY8zXkqVJBqeeJw'), asset = myCurrentToken, amount = 1)
            print "Sent 1 ZIGM"
        elif myCurrentToken.name=='YURI':
            print "Sending 1 YURI"
            myAddress.sendAsset(recipient = pw.Address('3PG3JmVh1czUhvg8stVwFY8zXkqVJBqeeJw'), asset = myCurrentToken, amount = 1)
            print "Sent 1 YURI"
            