---

$$\color{silver} \Huge \text{\R $\sum{\vil_c = \mathbb{N\infty}}$}$$

---
---
# $\color{gold} \large \text{CFW-BOT}$
> $\color{silver} \large \text{Cloudflare Woker Bot ! No servers needed,}$
> $\color{silver} \large \text{ just pure Xray link creation, all running smoothly on PythonAnywhere.}$
> $\color{silver} \large \text{A Shortcut to internet freedom ✨}$

[**![Lang_farsi](https://user-images.githubusercontent.com/125398461/234186932-52f1fa82-52c6-417f-8b37-08fe9250a55f.png) توضیحات فارسی**](README-FA.md)


<p align="left">
  <br><img src="https://github.com/NiREvil/workers-cloudflare/blob/main/Other/pics/CFW%203.png" width="360px">
</p>


## $\color{gold} \large \text{New changes in the latest version!!}$
- added proxies.txt , now you can create your favorite proxy list in bot
- access to your favorite proxy while adding new user or changing users proxies
- access to recently used proxies
- redeploy your worker script with new proxy that you set
- you can change all users proxies at once !
- no tls configurate added
- bug fixed : now delete subscripton worker when you delete a user
- it can create unique subscription worker link for each user that can use IP-API value
- subscription can be updated just by changing the IP_API value
- cloudflare webiste error solved
  
  
## $\color{gold} \large \text{Table of Contents}$
- [What is this ?](#what-is-this-)
  - [Features](#features)
  - [Prerequisites](#prerequisites)
  - [LAZY INSTALL](#lazy-install)
  - [ADVANCE INSTALL](#advanced-install)
  - [How To Use the Bot](#how-to-use-the-bot)
- [Note](#note)
- [Disclaimer](#disclaimer)

# $\color{gold} \large \text{What is this ?}$
This Python Telegram bot, powered by Cloudflare's Workers, makes generating Xray links a breeze! No need for complex server setups, just follow these simple steps to get started:
## $\color{gold} \large \text{Features}$
- **Easy Setup**: No server configurations required. With Cloudflare's Workers, deploying the bot is a breeze.
- **Persistent Storage**: Utilizes SQLite for database management, ensuring that your user data and generated links are securely stored.
- **User Management**: Create and manage multiple users with ease. Each user has access to their generated links at all times.
- **Efficient Deployment**: Leveraging Wrangler, the bot's worker script can be easily deployed on Cloudflare, ensuring reliability and scalability.

## $\color{gold} \large \text{Prerequisites}$
- One domain registered on Cloudflare
- Access to Cloudflare account
- Telegram Bot token (available from Telegram's BotFather)
- Cloudflare API key (generate one from Cloudflare dashboard)
- Account ID of your Cloudflare account
- User ID of the Telegram account you want to use the bot on (for authentication)
## $\color{gold} \large \text{Single Command install | BETA }$
$\color{silver} \normalsize \text{just copy and run and send tokens when it ask for them:}$
```bash
bash -c "$(curl -fsSL https://raw.githubusercontent.com/NiREvil/CFW-BOT/main/install.sh)"
```
## $\color{gold} \large \text{LAZY INSTALL}$
1. Register for a free account on [PythonAnywhere](https://www.pythonanywhere.com).
2. Obtain the required API keys:
   - Telegram Bot token from BotFather
   - Cloudflare API key from Cloudflare dashboard (make sure to select "Edit Cloudflare Workers template" and grant necessary permissions, all of them should have EDIT permission)
   - Telegram UserID you can obtain it from here https://t.me/useridinfobot or any similar bot you know
   - Cloudflare Account id, you can find it from right side of overview page or worker page in cloudflare
3. in your Dashboard section Select Files and and Click on "Open Bash Console Here"
4. $\color{silver} \normalsize \text{Clone this repository:}$
 ```bash
 git clone https://github.com/NiREvil/CFW-BOT.git
```
$\color{silver} \normalsize \text{5. Navigate to the project directory:}$

 ```bash
 cd CFW-BOT
 ```
$\color{silver} \normalsize \text{6. Make `requirement.sh executable:}$
 ```bash
 chmod +x requirement.sh
 ```

$\color{silver} \normalsize \text{7. Run `requirement.sh:}$
 ```bash
 ./requirement.sh
 ```
$\color{silver} \normalsize \text{"If you encounter errors running requirement.sh on PythonAnywhere }$, simply close the console (using `exit` command) , go to file manager and open it and  save it (use `ctrl+s` ) $\color{silver} \normalsize \text{without changing any thing. thats it! now you can run it"}$
$\color{silver} \normalsize \text{another solution is converting it using dos2unix, since PythonAnyWhere does not support that you can use this simple python code 'dos2unix.py}$
$\color{silver} \normalsize \text{you can run this to solve the issue:}$
 ```bash
 python3 dos2unix.py
 ```
$\color{silver} \normalsize \text{9. Run `install.py and provide the required API tokens when prompted:}$
 ```bash
 python3 install.py
 ```
$\color{silver} \normalsize \text{10. Start the bot:}$
 ```bash
 python3 cfw.py
 ```
## $\color{gold} \large \text{ADVANCED INSTALL}$

1. install requirements:
 ```bash
 pip install telebot
 pip install pytelegrambotapi --upgrade
 pip install qrcode[pil]
 pip install requests
 pip install python-dotenv
 ```
2. install NVM
```bash
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.1/install.sh | bash
```
3. set nvm settings
``` bash
export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"  # This loads NVM
[ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion"  # This loads NVM bash completion
```
4. start nvm and install wrangler
```bash
nvm install 16.17.0
nvm use 16.17.0
npm install wrangler@latest
npx wrangler --version
```
5. set .env file variables


| Variable             | Description                                            |
|----------------------|--------------------------------------------------------|
| CLOUDFLARE_API_TOKEN | Cloudflare API token with Worker edit permission       |
| BOT_TOKEN            | Telegram bot token obtained from BotFather             |
| ACCOUNT_ID           | Cloudflare account ID                                  |
| ADMIN_USER_ID        | Numeric Telegram user ID for admin authentication      |
| IP_API               | use this as refrence [CFW_Worker_Sub/main/ips.txt](https://raw.githubusercontent.com/2ri4eUI/CFW_Worker_Sub/main/ips.txt)|

6.remember to set cloudflare account id in workertemp.txt 


## How To Use the Bot
Once the bot is running, simply send the necessary commands to generate Xray links right from your Telegram app!
Creating a new user is a straightforward process. Follow these steps to get started:
**Obtain Cloudflare IP or Domain:**
   - Use platforms like [fofa.info](https://fofa.info) to find Cloudflare IP addresses or domains.
   - Example search query for fofa.info:
 ```bash
 
 server=="cloudflare" && port=="443" && country=="NL" && city=="Amsterdam"
 ```
   - Choose based on your preferences and network speed.

## Note
This bot is designed to be lightweight and inexpensive to run, making it accessible for everyone. Enjoy creating Xray links hassle-free!


## Disclaimer

I want to acknowledge the work of others and clarify that the `index.js` and `subworker.js` file is not my original work. It has been edited solely to ensure compatibility with the bot. 
