import os
from flask import Flask
app = Flask(__name__)

@app.route("/") # # take note of this decorator syntax, it's a common pattern

def index():
    return "Hello World, Flask is working! with more information to be loaded!"
    
app.run(host=os.getenv('IP', '0.0.0.0'), port=int(os.getenv('PORT', 8080)))

if __name__ == "__main__":
    app.run()
    app.debug = True    # this is not safe, so don't use this when used in production
    
