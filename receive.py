import os
from flask import Flask, request, abort

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhooks():
    if request.method == 'POST':
        body = request.json
        print(body)
        return 'success', 200
    else:
        abort(400)

if __name__ =="__main__":
    app.run(port=5000)