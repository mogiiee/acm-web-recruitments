from flask import Flask, render_template, request
app = Flask(__name__)

database = [
    {
        "name" : "manoj1",
        "email" : "m1@m.com",
        "balance" : 231254634
    },
    {
        "name" : "manoj2",
        "email" : "m2@m.com",
        "balance" : 2312436
    },
    {
        "name" : "manoj3",
        "email" : "m3@m.com",
        "balance" : 2312453
    },
    {
        "name" : "manoj4",
        "email" : "m4@m.com",
        "balance" : 2312765
    },
    {
        "name" : "manoj5",
        "email" : "m5@m.com",
        "balance" : 231223
    },
    {
        "name" : "manoj6",
        "email" : "m6@m.com",
        "balance" : 231286
    },{
        "name" : "manoj7",
        "email" : "m7@m.com",
        "balance" : 231235
    },
    {
        "name" : "manoj8",
        "email" : "m8@m.com",
        "balance" : 2312234324
    },
    {
        "name" : "manoj9",
        "email" : "m9@m.com",
        "balance" : 2312453
    },{
        "name" : "manoj10",
        "email" : "m10@m.com",
        "balance" : 2312546
    },
    {
        "name" : "manoj11",
        "email" : "m11@m.com",
        "balance" : 2312234
    },
    {
        "name" : "manoj12",
        "email" : "m12@m.com",
        "balance" : 233412
    }
]

@app.route('/')
def reciever():

    return render_template('db2.html', db = database)

if __name__== "__main__":
    app.run(debug = True)