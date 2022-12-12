
from flask import Flask,request
import base64
import requests

app1=Flask(__name__)

@app1.route("/")
def index():
    
    #Is there something_like_this method in Flask to perform the POST request?
    #sta=requests.post("http://127.0.0.1:4002"+"/board/True" ,json={"a":1})
    sta=requests.post("http://127.0.0.1:4002"+"/settings/start" ,json={"a":1})
    print(sta)
    return "amar"

@app1.route("/met/",methods=["POST"])
def function3():
    print(request.json)
    
    return "Success"


@app1.route("/images",methods=["POST"])
def function1():
    print("data")
    if ("photo1" in request.json and "photo2" in request.json):

        photo1 = request.json["photo1"]
        photo2 = request.json["photo2"]
        photo1 = base64.b64decode(photo1)
        photo2 = base64.b64decode(photo2)
        print(type(photo1))
        print(type(photo2))
    return "Success"


@app1.route("/images1/",methods=["POST"])
def function():
    print("data")
    if ("photo1" in request.json and "photo2" in request.json):

        photo1 = request.json["photo1"]
        photo2 = request.json["photo2"]
        photo1 = base64.b64decode(photo1)
        photo2 = base64.b64decode(photo2)
        print(type(photo1))
        print(type(photo2))
    return "Success"

if __name__=="__main__":
    
    app1.run("127.0.0.1",port=4001)
    
