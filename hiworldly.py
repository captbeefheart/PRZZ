from flask import Flask

app=Flask(__name__)
@app.route('/')
def hello_world():
    return 'hi w0r1dy'

if __name__=="__main__":
    app.run()
