from flask import Flask

app=Flask(__name__)
@app.route('/')
def hello_world():
    return 'h 0000ch333333333333ck 0ut me J3nky!!!!!!!'

if __name__=="__main__":
    app.run()
