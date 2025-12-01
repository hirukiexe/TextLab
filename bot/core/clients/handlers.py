"""
This module is responsible for handling various types of bots, such as:

- Group management bots
- Sticker management bots
- Command registration
- Event dispatching

It serves as the central place to register and manage all bot functionalities,
ensuring that handlers and commands are properly attached and executed.
"""
import handlers




def register_bot(bot):
    # Register bot to the group managment module 
    handlers.register(bot)