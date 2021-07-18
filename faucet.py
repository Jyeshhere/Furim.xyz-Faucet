### Importing section
import random as r            
import socket
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from flask import Flask, request, render_template
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



### Code that is executed every time u visit website
@app.route("/", methods=['GET','POST']) # Defining request that u can do get(get info)/post(send info)
@limiter.limit("2/hour") #limitier that limits visiting website [2 requests per hour]
def homepage(): # creating function homepage
    rand = str(r.uniform(0, 1)) #random variable that define how much u get from duco 
    if request.method == 'POST': # as u see if requested method was POST(sending info),(in that case your username) it will execute sequence that will do stuff
        first_name = request.form.get("fname")# creating variable that get info from html variable in that case its called fname
        server = ("server.duinocoin.com", 2811) # Defining server ip(domain) and port
        soc = socket.socket() # defining soc which is related socket variable
        soc.connect(server) #connecting to the server using soc variable
        version = soc.recv(5) #Decoding recived info(in that case version of duinocoin)
        soc.send(bytes("LOGI,Faucet_Furimos69,I_Love_Hentais_Andi_registered_with_duinocoin_account_on_pornhub",encoding="utf8")) #loggin in
        pong = soc.recv(8) #Decoding recived info(in that case successfully loged in / or not)
        soc.send(bytes("BALA,Faucet_Furimos69",encoding="utf8")) # How much duco faucet have
        pong0 = soc.recv(8) #Decoding it(in that case balance of duinocoin)
        pong0d = pong0.decode('utf-8') # Decoding it again but in utf-8 syntax???, basically to not receive [b'69.00'] but [69.00]
        soc.send(bytes("SEND,Furim_Faucet,{},{}".format(first_name, rand), encoding="utf8")) #Sending funds to someone who gave his username, first_name = Duco username, rand = random amount that person will get 
        pong1 = soc.recv(8) #Decode it(in that case if sending was sucessfuly or not)
        pong1d = pong1.decode('utf-8') #Decoding it with utf-8 syntax, aka to recive pure string not (b'verycoolusername')
        print(version) #printing version that socket recived           }
        print(pong)#printing if login in was successfull or not        } if u want to know if that was sucessfull or not i must print it
        print(pong0d) # printing balance of duco faucet                }
        print(pong1d) # pritning if sending duco was sucessfull or not }
        return  '''<body style="background-color:#212121;"> </body> <body> <h1 style="color:white; ">{}</h1> <p style="color:white; ">{}</p> <p style="color:white; ">{}<p style="color:white; "> <p style="color:white; ">{}</p> <p style="color:white; ">Duco has been sent to username -> [ {} ]</p> <h1 style="color:white; ">{}</h1> <p style="color:white; ">How much faucet have duco: {}</p> </body>'''.format(firstname, lastname, cellphone, duco_dnt0, first_name, rand, pong0d) # html code with defined variables
        return render_template('form.html', #template that u get when u visit website
                       firstname=firstname, 
                       lastname=lastname,  
                       cellphone=cellphone,  
                       duco_dnt0=duco_dnt0, 
                       rand=rand,
                       processed_text=processed_text,
                       first_name=first_name,
                       pong0d=pong0d)
    return render_template('form.html') #template that u get when u visit website
    
# error 429 aka cooldown website
@app.errorhandler(429)
def page_not_found(e):
    return render_template('429.html'), 409 
# error 429 aka cooldown website


# running app function  
if __name__=='__main__':
   app.run()
# running app function


# running app/debuging function
if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
# running app/debuging function