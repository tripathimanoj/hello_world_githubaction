from flask import Flask
import os


app=Flask(__name__)

@app.route('/',methods=['GET'])
def index():
    return "hello world this is from manoj"



if __name__=="__main__":
    app.run()