# SMS Auto-responder App
 Learn how to built a custom SMS Auto responder application using [Python programming language](https://www.python.org/), [Telnyx APIs](https://telnyx.com) and [ngrok](https://ngrok.com/). 

 ## Architecture
 
 <img src='./img/architecture.png' width="1000"/>
 
1. The user sends the text message to a number procurred from Telnyx
1. Telnyx receives the message and hands it to ngrok webhook
1. Ngrok webhook hands the data to flask aapplication
1. Flask application reads the message, evaluates it and responds to users number
1. Telnyx number sends response to users number as text message from flask application

## Prerequisite

 * Python installed (https://www.python.org/downloads/) 
 * Telnyx Developer Account (https://developers.telnyx.com/)
 * Ngrok (https://dashboard.ngrok.com/signup)
 * Code IDE or text Editor
 * terminal or shell or command prompt

 ## Steps

 ### Step 1: Telnyx Setup
 
 You need to do following: 
 1. Sign up for Telnyx account 
 1. Obtain a number to use for SMS auto-responder app
 1. Configure the number for messaging 
