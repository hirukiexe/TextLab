import functools
import asyncio
from core.replies import get_reply


prevent = {}
async def remove_user_from_prevent(user_id):
    
    await asyncio.sleep(0.5)
    if user_id in prevent:
        prevent.pop(user_id, None)


def CallbackEvents():
    def wrapper(func):
        @functools.wraps(func)
        async def inner(event, *args, **kwargs):
            
            event.get_reply = lambda key, **kwargs: get_reply(key, kwargs)
            
            
            
            sender_id = event.sender_id 
            
            if sender_id in prevent:
                await event.answer()
                return        
                
            asyncio.create_task(remove_user_from_prevent(sender_id))
            prevent[sender_id] = True   
            
            
            
            
            
            
            try:
                # Run original function
                return await func(event, *args, **kwargs)
            except Exception as e:
                error_msg = f"{e}"

                try:
                    await event.answer(error_msg)
                except:
                    pass  
                print(f"[ERROR] {e}")

        return inner
    return wrapper