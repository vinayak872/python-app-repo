from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello from Python App on Azure!"

if __name__ == "__main__":
    app.run()
