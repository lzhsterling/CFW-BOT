import os
from dotenv import set_key

cloudflare_api_token = input("Enter Cloudflare API token➡️ ")
bot_token = input("Enter Telegram Bot token➡️ ")
account_id = input("Enter Cloudflare Account ID➡️ ")
admin_user_id = input("Enter Admin User ID➡️ ")

set_key('.env', 'CLOUDFLARE_API_TOKEN', cloudflare_api_token)
set_key('.env', 'BOT_TOKEN', bot_token)
set_key('.env', 'ACCOUNT_ID', account_id)
set_key('.env', 'ADMIN_USER_ID', admin_user_id)
set_key('.env', 'IP_API', 'https://raw.githubusercontent.com/NiREvil/CFW-BOT/main/ips.txt')

with open('workertemp.txt', 'r') as file:
    lines = file.readlines()

with open('workertemp.txt', 'w') as file:
    for line in lines:
        if 'account_id' in line:
            line = f'account_id = "{account_id}"\n'
        file.write(line)

print("🤝🏻✋🏻 متغیرها با موفقیت به روز شدند")
print(" حالا میتونی با دستور شماره نهم بات رو اجرا کنی ")
print("           💓 برای زن ")
print("     💚 زندگی        ")
print("🤍 آزادی             ")
