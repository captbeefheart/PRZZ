from flask import Flask

app=Flask(__name__)
@app.route('/')
def hello_world():
    return 'h33ck 0utLLL me J3nky!!!!!!!'

if __name__=="__main__":
    app.run()
