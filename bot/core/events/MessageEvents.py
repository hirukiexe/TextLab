import functools
from core.replies import get_reply

def MessageEvents():
    def wrapper(func):
        @functools.wraps(func)
        async def inner(event, *args, **kwargs):
            
            if not event.sender_id:
                return
            
            event.get_reply = lambda key, **kwargs: get_reply(key, kwargs)
            
            
            
            
            
            
            try:
                # Run original function
                return await func(event, *args, **kwargs)
            except Exception as e:
                error_msg = f"Error CAUSED BY MessageEvents Decorator:\n{e}"

                try:
                    await event.reply(error_msg)
                except:
                    pass  
                print(f"[ERROR] {e}")

        return inner
    return wrapper