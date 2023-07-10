from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello,this is my first POC UseCase"

if __name__=="__main__":
   app.run()

	
