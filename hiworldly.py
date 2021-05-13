from flask import Flask

app=Flask(__name__)
@app.route('/')
def hello_world():
    return 'h1 ch3ck out me J3nky!'

if __name__=="__main__":
    app.run()
