from pyrogram import *
app = Client("bot", api_id="157804", api_hash="f972bf837a1d8bf83d51f15034ffbd9e")
@app.on_message(filters.channel)
async def start (client,message):
    if message.chat.id==-1001451950568 :
        if message.text==None :
            try:
                if message.caption_entities[0]["type"]!="url" and message.caption_entities[-1]["type"]!="url":
                    app.copy_message(chat_id=-1001743487290,from_chat_id=-1001451950568 ,message_id=message.message_id,caption=(str(message.caption)).replace("@wikivoicetv","@itiktoks"))
            except:
                app.copy_message(chat_id=-1001743487290,from_chat_id=-1001451950568 ,message_id=message.message_id,caption=(str(message.caption)).replace("@wikivoicetv","@itiktoks"))
        else:
            try:
                if message.entities[0]["type"]!="url" and message.entities[-1]["type"]!="url":
                    app.send_message(chat_id=-1001743487290,text=(str(message.text)).replace("@wikivoicetv","@itiktoks"))
            except:
                app.send_message(chat_id=-1001743487290,text=(str(message.text)).replace("@wikivoicetv","@itiktoks"))
    elif message.chat.id==-1001569468106 :
        if message.text==None :
            try:
                if message.caption_entities[0]["type"]!="url" and message.caption_entities[-1]["type"]!="url":
                    app.copy_message(chat_id=-1001743487290,from_chat_id=-1001569468106 ,message_id=message.message_id,caption=(str(message.caption)).replace("@campvatani","@itiktoks"))
            except:
                app.copy_message(chat_id=-1001743487290,from_chat_id=-1001569468106 ,message_id=message.message_id,caption=(str(message.caption)).replace("@campvatani","@itiktoks"))
        else:
            try:
                if message.entities[0]["type"]!="url" and message.entities[-1]["type"]!="url":
                    app.send_message(chat_id=-1001743487290,text=(str(message.text)).replace("@campvatani","@itiktoks"))
            except:
                app.send_message(chat_id=-1001743487290,text=(str(message.text)).replace("@campvatani","@itiktoks"))
print("done")
app.run()
