### Importing section
import random as r            
import socket
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from flask import Flask, request, render_template, jsonify
### Importing section


### Defining name file as app
app = Flask(__name__)
### Defining name file as app

### Different system of visiting website
limiter = Limiter(app, key_func=get_remote_address)
### Different system of visiting website

### Defining variables that u see after POST(typing username) request
firstname = str("Duco Faucet ")
lastname = str(" 🍵 Donations are welcome :)")
cellphone = str("XMR: 42Q6S9RUxHy7NyfQB6uwmwbXK1Yvd3FzFCGz57a8Mh6J3xtLQNPvhPoKdVnKss8e61aj82Xy8Bejr9bb8iUHGiKh7hbJW4n")
duco_dnt0 = str("DUCO: Faucet_Furimos69")
### Defining variables that u see after POST(typing username) request

# Variables with faucet wallet details
faucetUsername = 'Faucet_Furimos69'
faucetPassword = 'I_Love_Hentais_Andi_registered_with_duinocoin_account_on_pornhub'
msgToSend = 'Furim_Faucet' # Message to send with ducos

### Code that is executed every time u visit website
@app.route("/", methods=['GET']) # Defining request that u can do get(get info)
def homepage(): # creating function homepage
    return render_template('form.html') #template that u get when u visit website

@app.route("/giveMeDucos", methods=['POST']) # Defining request that u can do post(send info)
@limiter.limit("1/hour") #limitier that limits visiting website [1 requests per hour]
def giveMeDucos():
    rand = str(r.uniform(0, 1)) #random variable that define how much u get from duco 
    
    # rand = float(0.0000001) # override for debuging
    ducoUsername = request.args.get("ducoUsername")# creating variable that get info from html variable in that case its called fname

    # check if post request (ducoUsername) is not empty
    if not ducoUsername:
        return '',400 # returning http code 400 (bad request) if ducoUsername was empty
    else:
        # here should be try/except to catch timeouts and errors

        server = ("server.duinocoin.com", 2811) # Defining server ip(domain) and port
        soc = socket.socket() # defining soc which is related socket variable

        soc.connect(server) #connecting to the server using soc variable

        version = soc.recv(5) #Decoding recived info(in that case version of duinocoin)
        soc.send(bytes("LOGI,{},{}".format(faucetUsername, faucetPassword),encoding="utf8")) #loggin in
        pong = soc.recv(8) #Decoding recived info(in that case successfully loged in / or not)
        
        soc.send(bytes("SEND,{},{},{}".format(msgToSend, ducoUsername, rand), encoding="utf8")) #Sending funds to someone who gave his username, ducoUsername = Duco username, rand = random amount that person will get 
        pong1 = soc.recv(8) #Decode it(in that case if sending was sucessfuly or not)
        pong1d = pong1.decode('utf-8') #Decoding it with utf-8 syntax, aka to recive pure string not (b'verycoolusername')

        soc.send(bytes("BALA,{}".format(faucetUsername),encoding="utf8")) # How much duco faucet have
        pong0 = soc.recv(8) #Decoding it(in that case balance of duinocoin)
        pong0d = pong0.decode('utf-8') # Decoding it again but in utf-8 syntax???, basically to not receive [b'69.00'] but [69.00]

        print('[REQUEST] srv version: %s, success? %s, wallet balance: %s, success: %s' % (version, pong, pong0d, pong1d)) # Printing server version, ping response, balance of faucet wallet, if sending duco was successful or not

        # returning json with sended amount, where and balance
        return jsonify(ducoSended=rand,
                    ducoSendedTo=ducoUsername,
                    ducoBalance=pong0d)

# error 429 aka cooldown website
@app.errorhandler(429)
def cooldown(e):
    return '', 409 
# error 429 aka cooldown website


# running app function  
if __name__=='__main__':
   app.run()
# running app function


# running app/debuging function
if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
# running app/debuging function