# Chatbot Demo

Chatbot built with [Node.js](https://nodejs.org) and [Telnyx APIs](https://telnyx.com)

## Overview

Learn how to create your own custom SMS chatbot to respond to an end-user's simple food choices.

___

### 1. Prerequisites & Telnyx Setup

It is recommended you have experience in the following areas to continue: 
 * **JavaScript** 
 * **Node.js**
 * **npm**
 * **terminal | shell | command**

**Task:** You will sign up for a Telnyx account, obtain a number to use for your chatbot, and configure it for messaging. 

<details>
<summary><strong>Step-by-step instructions</strong> (expand for details)</summary><p>

1. You will need to set up a developer account with Telnyx at https://telnyx.com/sign-up.

2. Once you have your account created and you are signed in, you will need to [procure a number](https://portal.telnyx.com/#/app/numbers/buy-numbers) to use for your chatbot. Be sure to select a number that supports the SMS feature.

    > The number you buy is your "chatbot" number - this will be needed in a future step.

3. Now create a [messaging profile](https://portal.telnyx.com/#/app/messaging). For now, just create the profile and don't worry about filling in any data. Once you have named and saved your profile, you are ready for the next step.

4. Go to the [numbers](https://portal.telnyx.com/#/app/numbers/my-numbers) management screen and find the number you created previously. Set the number's `Messaging Profile` to the profile you created in the previous step. 

    > You should be able to test the new number from within the Telnyx platform. Go to Step 3 at the [Messaging Learn & Build](https://portal.telnyx.com/#/app/messaging/learn-and-build) page.

5. Go to the [API Keys](https://portal.telnyx.com/#/app/api-keys) management screen and copy the API Key for a future step! If an API Key is not there, then create one!

    > You have created your number, associated with a messaging profile, and obtained your API Key. You are ready to move on to the next major step!

</p></details>

___

### 2. Setup & Configure Node.js Application

**Task:** You will create a new npm project and associated packages. You will write code to implement a simple server and execute it.

<details>
<summary><strong>Step-by-step instructions</strong> (expand for details)</summary><p>

1. Create a new npm project and install all the dependencies:
    
    ``` shell
    npm init
    npm install express
    npm install dotenv
    npm install telnyx
    ```

    > This will create a [package.json](https://docs.npmjs.com/creating-a-package-json-file) file with the packages needed to run the application.

2. In the root folder of your project, create a text file named `.env` and populate it with the following:

    ``` csv
    TELNYX_KEY=
    BOT_NUMBER=
    PORT=5000
    ```

    > This allows you to store sensitive environment variables in a file during development. You access the values in code just as you do via `process.env`. For `TELNYX_KEY`, assign it the API Key value you copied earlier. For `BOT_NUMBER`, assign it the value of the number you procured earlier, and format as so: `+12223334444` (use appropriate country format) 

3. Create a file in the root of your project named `index.js` and place the following code there:

    ``` javascript
    require('dotenv').config();

    const express = require('express');
    const telnyx = require('telnyx')(process.env.TELNYX_KEY);
    const port = parseInt(process.env.PORT) || 5000;
    const app = express();

    // jsonify the request & response objects
    app.use(express.json());

    // app initialized via port
    app.listen(port, () => console.log(`App running on port ${port}`));
    ```

    > The code above connects the project dependencies and provides a simple server configured to listen on a port - and does nothing else at the moment. The calls to `process.env.TELNYX_KEY` and `process.env.PORT` are populated by the values in the `.env` file.

4. Run the application to confirm everything is configured correctly so far:

    ``` shell
    node index
    ```

    > If all is well, you should see a message appear in your console:

    > `App running on port 5000`

    > You can stop the application. You are now ready for the next major step!

</p></details>

___

### 3. Install Tunneling Tool & Configure

**Task:** You will install a tunneling tool to allow internet access to your running node application. You will configure your Telnyx messaging profile to use a webhook URL supplied by the tunneling tool. 

<details>
<summary><strong>Step-by-step instructions</strong> (expand for details)</summary><p>

1. Go to the [setup & installation page for ngrok](https://dashboard.ngrok.com/get-started/setup) and follow the instructions there. When you get to step 3, replace the command with the following:

    ``` shell
    ./ngrok http 5000
    ```

    > You should see something like what is shown here: 

    <img src='./img/ngrok.jpg' />

    > Copy the value of the `Forwarding` URL as highlighted in the screen capture above for use in the next step. Do NOT stop the ngrok process.

2. Return to the [messaging profile](https://portal.telnyx.com/#/app/messaging) and edit the one you created earlier. Under `Inbound Settings` paste the forwarding URL from the previous step and append it with `/webhook` so the value will look something like:

    ``` shell
    https://823565362b23.ngrok.io/webhook
    ```

    > Save your changes. Telnyx will use this webhook when it receives a message to your number and provide it to your node application when it is running!
    >> NOTE! Unless you [upgrade your ngrok account](https://dashboard.ngrok.com/billing/plan), each time you restart ngrok the URL changes! This means you need to repeat the previous step each time too!

    > You have installed the tunneling tool, you should have it running, and your Telnyx messaging profile is configured to use the ngrok forwarding URL. You are ready to embark on the last major step!

</p></details>

___

### 4. Code for Message Interactions

**Task:** You will write code to receive and respond to messages from your chatbot number. You will inspect any incoming messages for the words `pizza` and `ice cream` and respond uniquely for each value. If the incoming message contains neither value, the response will prompt for proper interaction.  

<details>
<summary><strong>Step-by-step instructions</strong> (expand for details)</summary><p>

1. Add the following code to the `index.js` file:

    ``` javascript
    // route for inbound or outbound post to webhook
    app.post('/webhook', (req, res) => {
        
        // payload contains incoming message info
        const payload = req.body.data.payload;
        
        // only process inbound requests
        if (payload.direction==='inbound') {
            processInboundPayload(payload);
        }

        // politely end response
        res.statusCode = 200;
        res.end();
    });

    // helper
    function processInboundPayload(payload){
        const incomingText = payload.text;
        const incomingFrom = payload.from.phone_number;
        const reply = getReply(incomingText);
        telnyx.messages.create(
        {
            'from': process.env.BOT_NUMBER,
            'to': incomingFrom,
            'text': reply
        },
        function(err, response) {
            err && console.log(err);
            response && console.log(response);
        });
    }

    // helper
    function getReply(text) {
        let reply = null;
        if (text.match(/pizza/i)){
            reply = "Chicago pizza is the best";
        }
        if (text.match(/ice cream/i)) {
            reply = "I prefer gelato";
        }
        return reply || "Please send either the word 'pizza' or 'ice cream' for a different response";
    }
    ```

    > Note the code comments

2. Start your node application:    
    
    ``` shell
    node index
    ```

    > With your node app and ngrok running, you can now test!

3. With your own phone, text your chatbot number. Try these values:

    ``` shell
    candy
    pizza
    ice cream
    ```

    > If all is well, you should have a similar experience as shown here:

    <img src='./img/msgs.jpg' width="600"/>

    > You have provided the code to make it possible to interact with Telnyx messaging APIs and tested with your own phone!
    
</p></details>

___

** Congratulations, you have created your own custom chatbot! **