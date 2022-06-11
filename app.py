from flask import Flask
import os


app=Flask(__name__)

@app.route('/',methods=['GET'])
def index():
    return "hello world this is 2nd build"



if __name__=="__main__":
    app.run()