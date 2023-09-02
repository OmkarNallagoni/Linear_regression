from flask import Flask, request


app=Flask(__name__)

@app.route('/')      # decorator
def welcome():
    return "Welcome All"


@app.route('/addition',
           methods=["Get"])
def add():
    a=request.args.get("num1")   # a=10     num1=10  in the browser itself
    b=request.args.get("num2")   # b=20     num2=20  in the browser itself
    return ([int(a)+int(b)])


if __name__=='__main__':
    app.run(host='0.0.0.0',port=8000)