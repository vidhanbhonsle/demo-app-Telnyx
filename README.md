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
 
 <details>
<summary><strong>Steps to follow</strong> (click to expand)</summary><p>

 1. Sign up for Telnyx account
    > Set up a developer account with Telnyx from https://telnyx.com/sign-up.

 2. Obtain a number with SMS capabilities for auto-responder app
    > After creating an account and signing in, you need to [acquire a number](https://portal.telnyx.com/#/app/numbers/search-numbers) for the application. Search for a number by setting 'Region' or 'Area Code' of your preference. 
    
    > Make sure that the number supports SMS feature(Very Important!) as it will be used by our application.
 
 3. Create a messaging profile
    > Next create a [messaging profile](https://portal.telnyx.com/#/app/messaging) by clicking on "Ass new profile" and provide a suitable profile name to it(you do not need to provide any other detail for now).

 4. Configure the number for messaging
    > Go to the [numbers](https://portal.telnyx.com/#/app/numbers/my-numbers) page, look for the number you created and set the number's `Messaging Profile` to the profile you created in the previous step. 
    
    <details>
    <summary>Click if the Telnyx number is an international number for User</summary>
    <br>    
    
    > If you want to send the message to a Telnyx number which is not in the country where you are, you will need to click on the 'Routing' option.
     <img src='./img/routing_click_red.png' width="800"/>
    
    > Once you click on 'Routing' a pop up will open. Select traffic type as "P2P" to allow International Inbound and Outbound SMS deliverability. And do not forget to save the changes!  

     <img src='./img/routing_selected.png' width="800"/> 
    </details>
    
 5. Acquire Telnyx API key
    > Go to the [API Keys](https://portal.telnyx.com/#/app/api-keys) management screen and copy the API Key for a future step! If an API Key is not there, then create one!

</p></details>

___

### Step 2: Install and configure ngrok

<details>
<summary><strong>Steps to follow</strong> (click to expand)</summary><p>

 1. Sign up for ngrok account and download the setup file
    > Go to https://dashboard.ngrok.com/signup and create an account.

 2. Obtain the ngrok setup file and follow the steps mentioned
    > Download the ngrok setup file as per your OS from https://dashboard.ngrok.com/get-started/setup and follow the steps mentioned on the page.
    
    > You need to run the setup file (It has zero run-time dependencies!)
    
    > In the Step 3, you need to change the command to
     ``` shell
    ./ngrok http 5000
    ```
    > After running the above command, you would see something similar to following
    
    <img src='./img/ngrok_tunnel.png' width="800"/> 

    > Copy the highlighted 'Forwarding' address

    ``` shell
    http://0ab4-2405-201-300a-ecf1-201a-6ad8-c0d4-eddd.ngrok.io
    ```

    > **Always keep the ngrok process running, do not stop it!**

 3. Edit Telnyx messaging profile to add webhook
    
    > Go to [messaging profile](https://portal.telnyx.com/#/app/messaging) and click on the message profile you created earlier.

    > It will open "Edit Messaging Profile" page, here under "Inbound Settings" you need to provide value to 'Send a webhook to this URL' 

    > The value is Forwarding address we copied in the previous step. Append it with '/webhooks'. It will look like this -

    ``` shell
    http://0ab4-2405-201-300a-ecf1-201a-6ad8-c0d4-eddd.ngrok.io/webhooks
    ```
    <img src='./img/inbound_webhook.png' width="800"/>
    
    <details>
    <summary>Click if the Telnyx number is an international number for User</summary>
    <br>    
    
    > If you want to send the message to a Telnyx number which is not in the country where you are, you will need to click on the 'Routing' option.
     <img src='./img/routing_click_red.png' width="800"/>
    
    > Once you click on 'Routing' a pop up will open. Select traffic type as "P2P" to allow International Inbound and Outbound SMS deliverability. And do not forget to save the changes!  

     <img src='./img/routing_selected.png' width="800"/> 
    </details>
    
 5. Acquire Telnyx API key
    > Go to the [API Keys](https://portal.telnyx.com/#/app/api-keys) management screen and copy the API Key for a future step! If an API Key is not there, then create one!

</p></details>

___





