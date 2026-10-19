# open the browser search flsk module 1link welcome  click the first link copy the code 
# pase vscode 

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
app.run()