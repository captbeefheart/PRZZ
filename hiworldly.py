from flask import Flask

app=Flask(__name__)
@app.route('/')
def hello_world():
    return 'h1 w0000r11dy'

if __name__=="__main__":
    app.run()
