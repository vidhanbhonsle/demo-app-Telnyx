from flask import Flask, request
import telnyx

telnyx.api_key = "YOUR_API_KEY" 
telnyx_number = '+YOUR_TELNYX_NUMBER'

app = Flask(__name__)

@app.route('/webhooks', methods=['POST'])
def webhooks():
    payload = request.json['data']['payload']
    if payload['direction'] == 'inbound':
        takeAction(payload)
    return 'success', 200
    
def takeAction(payload):
    incomingText    = payload['text']
    incomingNumber  = payload['from']['phone_number']
    
    reply = calculateReply(incomingText)
    
    telnyx.Message.create(
    from_ = telnyx_number,
    to = incomingNumber,
    text = reply,
    )

def calculateReply(incomingText):
    if(incomingText.lower() == 'ice cream'):
        reply = "I prefer gelato"
    elif(incomingText.lower() == 'pizza'):
        reply = "Chicago pizza is the best"
    else:
        reply = "Please send either the word 'pizza' or 'ice cream' for a different response"
    return reply 

if __name__ =="__main__":
    app.run(port=5000)