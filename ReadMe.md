# Channel Auto-Post Bot

This bot can send all new messages from one channel, directly to another channel (or group, just in case), without the forwarded tag!


## 🚸 HEROKU CLI COMMANDS

`* git clone https://github.com/AsuranJ/ChannelAutoPost.git`

`* heroku login`

`* cd ChannelAutoPost`

`* heroku git:remote -a app-name`

`* git pull origin V2.0`

`* git push heroku V2.0:main`

## Setting up 
* First:
> `APP_ID` and `API_HASH` - Get it from my.telegram.org   
> `BOT_TOKEN` - Get it from [@BotFather](https://t.me/BotFather)   
> `FROM_CHANNEL` - The ID of the main channel from where posts have to be copied. (Use @chnlidbot to get it.)   
> `TO_CHANNEL` - The ID of the channel to which the posts are to be sent. (Use @chnlidbot to get it.)   
   
* Chose a platform to deploy on:
<details>
<summary>Heroku/Kintohub/Zeet</summary>
<br>
Add the above values to the environment vars and deploy the bot.
</details>
<details>
<summary>Local Deploys</summary>
<br>
- Clone the repo:   <code>git clone https://github.com/xditya/ChannelAutoForwarder</code></br>
- Make a <code>.env</code> file in the root of the repo, like <a href="https://github.com/xditya/ChannelAutoForwarder/blob/main/.env.sample">.env.sample</a> and fill in the values.</br>
- Use <code>python3 bot.py</code> to start the bot.</br>  
</details>

## Usage
Add the bot to both channels with admin permission, and thats it!
All new messages will be auto-posted!! 
