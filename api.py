from flask import Flask

app = Flask(__name__)

@app.route('/')
def return_data():
    data = {1: "あ",
            2: "い",
            3: "う",
            4: "え",
            5: "お"}
    return data