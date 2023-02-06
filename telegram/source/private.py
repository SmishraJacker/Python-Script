Error = 'Please Type The Message In This Format\n\n/send : @username or chat_id : Message You Want To Send Here'

async def brodcast(message) :

	text = (message.text).split(" : ", 2)	try :

		flag = text[1]

		msg = text[2]

		if flag.startswith("@") :

			chat_id = flag

		else :

			try :

				chat_id = int(text[1])

			except :

				chat_id = message.chat.id

				return chat_id, Error

		return chat_id, msg

	except :

		return message.chat.id, Error

		
