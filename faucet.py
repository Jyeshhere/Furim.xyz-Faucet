### Importing section
import random as r            
import socket
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from flask import Flask, request, render_template, jsonify
import requests
import json
from flask import Flask
from flask import request


### Importing section
app = Flask(__name__)

from werkzeug.middleware.proxy_fix import ProxyFix

app.wsgi_app = ProxyFix(app.wsgi_app, x_proto=1)

### Defining name file as app
### Defining name file as app

### Different system of visiting website
limiter = Limiter(app, key_func=get_remote_address)
### Different system of visiting website

### Defining variables that u see after POST(typing username) request

### Defining variables that u see after POST(typing username) request
firstname = str("Duco Faucet ")
lastname = str(" 🍵 Donations are welcome :)")
cellphone = str("XMR: 42Q6S9RUxHy7NyfQB6uwmwbXK1Yvd3FzFCGz57a8Mh6J3xtLQNPvhPoKdVnKss8e61aj82Xy8Bejr9bb8iUHGiKh7hbJW4n")
duco_dnt0 = str("DUCO: Faucet_Furimos69")
### Defining variables that u see after POST(typing username) request

# Variables with faucet wallet details
faucetUsername = ''
faucetPassword = ''
msgToSend = 'Furim_Faucet' # Message to send with ducos

### Code that is executed every time u visit website
@app.route("/", methods=['GET']) # Defining request that u can do get(get info)
def homepage(): # creating function homepage
    return render_template('form.html') #template that u get when u visit website

@app.route("/giveMeDucos", methods=['POST']) # Defining request that u can do post(send info)
@limiter.limit("1/hour") #limitier that limits visiting website [1 requests per hour]
def giveMeDucos():

# number1 = 5
 #   number2 = balance_var



  #  percent = (number1*number2)/100
   # print(percent)


   # percent = (number1*number2)/100
   # print(percent)
    
    #rand = str(r.uniform(0, 0.1)) #random variable that define how much u get from duco 
#haidangclone    
    # rand = float(0.0000001) # override for debuging
    ducoUsername = request.args.get("ducoUsername")# creating variable that get info from html variable in that case its called fname

    if ','  in ducoUsername:
        return render_template('myes.html')

    if 'Furrymann2578' in ducoUsername:
        return render_template('myes.html')
 
    if "ArduinoUno" in ducoUsername:
        return render_template('myes.html')

    if "haidangclone" in ducoUsername:
        return render_template('myes.html')


    if "darestz" in ducoUsername:
        return render_template('myes.html')


    #if "Furrmann2578" in ducoUsername:
    #           print("Fuck you idiot")


    ip = request.environ.get('REMOTE_ADDR')    
    json_ze_strony = requests.get("http://daiman.nl/check.php?ip={}".format(ip)).json()
    json_api_username_var = json_ze_strony["code"]
    print(json_ze_strony)
    print(json_api_username_var)    
    str_json_api_username_var = (str(json_api_username_var))
    if str_json_api_username_var == "100":    
         return render_template("429.html")
    else:   
        # here should be try/except to catch timeouts and errors
        response_balance = requests.get('https://server.duinocoin.com/balances/{}'.format(faucetUsername))
        normalized_response_balance = response_balance.text
        
        y = json.loads(response_balance.text)
        not_splitted_var = y["result"]["balance"]

        print(not_splitted_var)



        number1 = float(0.001)
        number2 = float(not_splitted_var)
        percent = (number1*number2)/100
        print(percent)


 

        response = requests.get('https://server.duinocoin.com/transaction/?username={}&password={}&recipient={}&amount={}&memo={}'.format(faucetUsername, faucetPassword, ducoUsername, percent, msgToSend))
        print(response.text)


        y = json.loads(response.text)
        not_splitted_var = y["result"]


        splitted_var = not_splitted_var.split(",")


        hash_of_transaction = '''<a style="color:#f5cd79; font-size:40px" href="https://server.duinocoin.com/transactions/{}">🐼</a>'''.format(splitted_var[2])

        print("there is ma boi hash: ", splitted_var[2])





        print(not_splitted_var) # Printing server version, ping response, balance of faucet wallet, if sending duco was successful or not

        # returning json with sended amount, where and balance
        return jsonify(ducoSended=percent,
                    ducoSendedTo=ducoUsername,
                    hash_of_transaction=hash_of_transaction)
# error 429 aka cooldown website
@app.errorhandler(429)
def cooldown(e):
    return '', 409 
# error 429 aka cooldown website


# running app function  
if __name__=='__main__':
   app.run()
# running app function

if __name__ == "__main__":
   app.run(host='0.0.0.0',port=6996)


# running app/debuging function
if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
# running app/debuging function
