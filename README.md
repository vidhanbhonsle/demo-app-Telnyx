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
 - Sign up for Telnyx account 
 - Obtain a number with SMS capabilities for auto-responder app
 - Configure the number for messaging 

 <details>
<summary><strong>Steps to follow</strong> (click to expand)</summary><p>

1. Set up a developer account with Telnyx from https://telnyx.com/sign-up.

2. After creating an account and signing in, you need to [acquire a number](https://portal.telnyx.com/#/app/numbers/search-numbers) for the application. Search for the suitable 'Region' or 'Area Code'. Also make sure that the number supports SMS feature(Very Important!) as it will be used by our application.

3. Next create a [messaging profile](https://portal.telnyx.com/#/app/messaging) and provide a suitable name to it(you do not need to provide any further detail for now).

4. Go to the [numbers](https://portal.telnyx.com/#/app/numbers/my-numbers) management screen and find the number you created previously. Set the number's `Messaging Profile` to the profile you created in the previous step. 

    > You should be able to test the new number from within the Telnyx platform. Go to Step 3 at the [Messaging Learn & Build](https://portal.telnyx.com/#/app/messaging/learn-and-build) page.

5. Go to the [API Keys](https://portal.telnyx.com/#/app/api-keys) management screen and copy the API Key for a future step! If an API Key is not there, then create one!

    > You have created your number, associated with a messaging profile, and obtained your API Key. You are ready to move on to the next major step!

</p></details>


