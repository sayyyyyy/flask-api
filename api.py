from flask import Flask

app = Flask(__name__)

@app.route('/')
def return_data():
    data = {1: "a",
            2: "b",
            3: "c",
            4: "d",
            5: "e"}
    return data


@app.route('/id=<id>')
def designated_return_data(id):

    if id == '1':
        data = {1: "a",
                2: "b",
                3: "c",
                4: "d",
                5: "e"}
    elif id == '2':
        data = {1: "あ",
                2: "い",
                3: "う",
                4: "え",
                5: "お"}
    else:
        data = {1: "Not Found"}   
    
    return data