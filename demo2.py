from flask import Flask, request
import telnyx

telnyx.api_key = "KEY017C41A1A876EAA1AE0FD375C7A48369_b1u44bgX3Cix5IdDWHAcKE" 
telnyx_number = '+18727580002'

app = Flask(__name__)

@app.route('/webhooks', methods=['POST'])
def webhooks():    
    payload = request.json
    print(payload)
    return 'success', 200

if __name__ =="__main__":
  app.run(port=5000)