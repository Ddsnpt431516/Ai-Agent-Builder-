from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "🚀 Hello from Agentic AI Builder on Railway!"

if __name__ == '__main__':
    app.run(debug=True)
