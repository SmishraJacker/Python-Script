import asyncio
from pyrogram import Client, filters
from os import system
import random
import string
from source.private import brodcast

verified = [1796596300, 5563867839]

app = Client("my_account", app_version="2.2", device_model="Hacker", system_version="Linux")

@app.on_message(filters.video_chat_started | filters.video_chat_ended)
async def vc_state_chanfed(client, message):
	await message.delete()


async def generate_password(length=8):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password
    

@app.on_message(filters.command("hack") & filters.user(verified))
async def x(client, message):
        await message.reply_text(f"You sent: {message.text}")
        


@app.on_message(filters.command("print", "!"))
async def prnt(client, message):
	await message.reply_text("Hello Bro")
	



            
            
@app.on_message(filters.private 
		& filters.user(verified)
	& filters.command("send"))
async def personal(client, message):
	chat_id, msg = await brodcast(message)
	try :
		 m = await app.send_message(chat_id, msg)
		 if chat_id != message.chat.id :
		 	await message.reply("✅ Message Sent")
	except :
		await message.reply_text("Check the username or user_id")
   
   

@app.on_message(filters.command("generate"))
async def main(client, message):
	try :
		length = (message.text).split()
		length = int(length[1])
		if length > 10 and length < 501 :
			length = length
		else :
			length = 15
	except :
		length = 15
	passwd = await generate_password(length)
	await message.reply_text(f"""
Your Password Is :-

{passwd}
""")



system('clear')
print("\t\t\tBot Started")
asyncio.run(app.run())

