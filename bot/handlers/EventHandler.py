from telethon import events
from core.events import MessageEvents, CallbackEvents

from .handles import (
    generate_random_mail
)




def register(client):
    
    @client.on(events.NewMessage(pattern=r'^/start'))
    async def start_cmd(event):
        await event.reply(
            "Hey! 👋\n\nI'm your Text Tool Bot.\nType /help to see all features!"
        )
    
    

    @client.on(events.NewMessage(pattern=r'^/genmail$'))
    @MessageEvents()
    async def genmail_command(event):
        """
        Handles generating random mails
        """
        await generate_random_mail.handle(event)
    
    @client.on(events.CallbackQuery(pattern=r'^mail_'))
    @CallbackEvents()
    async def mail_callback_handler(event):
        await generate_random_mail.buttons_handle(event)
        