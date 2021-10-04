import os
from flask import Flask, request, abort

app = Flask(__name__)

@app.route('/webhooks', methods=['POST'])
def webhooks():
    body = request.json
    print(body)
    # print(body.data.payload.text)
    # print('------------------------------------------------------------------------')
    # print(body)
    return 'success', 200
    
if __name__ =="__main__":
    app.run(port=5000)