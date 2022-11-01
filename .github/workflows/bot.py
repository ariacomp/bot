from pyrogram import *
app = Client("bot", api_id="157804", api_hash="f972bf837a1d8bf83d51f15034ffbd9e")
@app.on_message(filters.channel)
def start (client,message):
    if message.chat.id==-1001480403747 :
        if message.text==None :
            try:
                if message.caption_entities[0]["type"]!="url" and message.caption_entities[-1]["type"]!="url":
                    app.copy_message(chat_id=-1001743487290,from_chat_id=-1001480403747 ,message_id=message.message_id,caption=(str(message.caption)).replace("@tiktokeTV","@itiktoks"))
            except:
                app.copy_message(chat_id=-1001743487290,from_chat_id=-1001480403747 ,message_id=message.message_id,caption=(str(message.caption)).replace("@tiktokeTV","@itiktoks"))
        else:
            try:
                if message.entities[0]["type"]!="url" and message.entities[-1]["type"]!="url":
                    app.send_message(chat_id=-1001743487290,text=(str(message.text)).replace("@tiktokeTV","@itiktoks"))
            except:
                app.send_message(chat_id=-1001743487290,text=(str(message.text)).replace("@tiktokeTV","@itiktoks"))
    elif message.chat.id==-1001107615180 :
        if message.text==None :
            try:
                if message.caption_entities[0]["type"]!="url" and message.caption_entities[-1]["type"]!="url":
                    app.copy_message(chat_id=-1001743487290,from_chat_id=-1001107615180 ,message_id=message.message_id,caption=(str(message.caption)).replace("@lichar","@itiktoks"))
            except:
                app.copy_message(chat_id=-1001743487290,from_chat_id=-1001107615180 ,message_id=message.message_id,caption=(str(message.caption)).replace("@lichar","@itiktoks"))
        else:
            try:
                if message.entities[0]["type"]!="url" and message.entities[-1]["type"]!="url":
                    app.send_message(chat_id=-1001743487290,text=(str(message.text)).replace("@lichar","@itiktoks"))
            except:
                app.send_message(chat_id=-1001743487290,text=(str(message.text)).replace("@lichar","@itiktoks"))
    elif message.chat.id==-1001451950568 :
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
    elif message.chat.id==-1001071599220 :
        if message.text==None :
            try:
                if message.caption_entities[0]["type"]!="url" and message.caption_entities[-1]["type"]!="url":
                    app.copy_message(chat_id=-1001743487290,from_chat_id=-1001071599220 ,message_id=message.message_id,caption=(str(message.caption)).replace("@SiCKiCM","@itiktoks"))
            except:
                app.copy_message(chat_id=-1001743487290,from_chat_id=-1001071599220 ,message_id=message.message_id,caption=(str(message.caption)).replace("@SiCKiCM","@itiktoks"))
        else:
            try:
                if message.entities[0]["type"]!="url" and message.entities[-1]["type"]!="url":
                    app.send_message(chat_id=-1001743487290,text=(str(message.text)).replace("@SiCKiCM","@itiktoks"))
            except:
                app.send_message(chat_id=-1001743487290,text=(str(message.text)).replace("@SiCKiCM","@itiktoks"))
    elif message.chat.id==-1001432169967 :
        if message.text==None :
            try:
                if message.caption_entities[0]["type"]!="url" and message.caption_entities[-1]["type"]!="url":
                    app.copy_message(chat_id=-1001743487290,from_chat_id=-1001432169967 ,message_id=message.message_id,caption=(str(message.caption)).replace("@chosJaghi","@itiktoks"))
            except:
                app.copy_message(chat_id=-1001743487290,from_chat_id=-1001432169967 ,message_id=message.message_id,caption=(str(message.caption)).replace("@chosJaghi","@itiktoks"))
        else:
            try:
                if message.entities[0]["type"]!="url" and message.entities[-1]["type"]!="url":
                    app.send_message(chat_id=-1001743487290,text=(str(message.text)).replace("@chosJaghi","@itiktoks"))
            except:
                app.send_message(chat_id=-1001743487290,text=(str(message.text)).replace("@chosJaghi","@itiktoks"))
    elif message.chat.id==-1001104664708 :
        if message.text==None :
            try:
                if message.caption_entities[0]["type"]!="url" and message.caption_entities[-1]["type"]!="url":
                    app.copy_message(chat_id=-1001743487290,from_chat_id=-1001104664708 ,message_id=message.message_id,caption=(str(message.caption)).replace("@DIRTTY_FUNy","@itiktoks"))
            except:
                app.copy_message(chat_id=-1001743487290,from_chat_id=-1001104664708 ,message_id=message.message_id,caption=(str(message.caption)).replace("@DIRTTY_FUNy","@itiktoks"))
        else:
            try:
                if message.entities[0]["type"]!="url" and message.entities[-1]["type"]!="url":
                    app.send_message(chat_id=-1001743487290,text=(str(message.text)).replace("@DIRTTY_FUNy","@itiktoks"))
            except:
                app.send_message(chat_id=-1001743487290,text=(str(message.text)).replace("@DIRTTY_FUNy","@itiktoks"))
print("done")
app.run()
