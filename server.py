from flask import Flask, render_template, request
app = Flask(__name__)



@app.route('/')
def reciever():
    database = [
        {
            "name" : "manoj1",
            "email" : "m@m.com",
            "balance" : 2312
        },
        {
            "name" : "manoj2",
            "email" : "m@m.com",
            "balance" : 2312
        },
        {
            "name" : "manoj3",
            "email" : "m@m.com",
            "balance" : 2312
        }
    ]
    # for i in db:
    #     print(i["name"])
    return render_template('db2.html', db = database)






if __name__== "__main__":
    app.run(debug = True)