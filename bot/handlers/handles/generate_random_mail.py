
from telethon import Button
from ..utils.random_mail import generate_mail, domain_map


users_mail_settings = {}





# Inline keyboard layout
mail_keyboard = [
    [
        Button.inline("Domain", b"mail_domain"),   # callback data = "domain"
        Button.inline("Count", b"mail_count"),     # callback data = "count"
        Button.inline("Type", b"mail_type")  # callback data = "mailtype"
    ],
    [
        Button.inline("Generate", b"mail_generate")  # Generate button
    ]
]


async def handle(event):
    
    sender_id = event.sender_id
    
    data = users_mail_settings.get(sender_id, None)
    
    if not data:
        users_mail_settings[sender_id] = data = {
            "domain" : "all",
            "mail_type" : "unique",
            "count" : 10
        }
    
    mail_type = data["mail_type"]
    domain = data["domain"]  
    count = data["count"]  
    
    mails_list = generate_mail(domain, mail_type, count)
    
    msg = mail_list_msg(mails_list)
    await event.reply(f"{msg}", buttons=mail_keyboard)


def mail_list_msg(mails_list):
    
    mail_msg = ""
    for i, mail in enumerate(mails_list, start=1):
        # i = index starting from 1
        num_str = f"{i:02}"  # automatically pad 0 if single digit
    
        # Append email to message
        mail_msg += f"{num_str}. `{mail}`\n"
    
    return mail_msg  
    



async def buttons_handle(event):
    data = event.data.decode('utf-8')
    sender_id = event.sender_id
    
    
    user_data = users_mail_settings.get(sender_id, None)
    
    if not user_data:
        users_mail_settings[sender_id] = data = {
            "domain" : "all",
            "mail_type" : "unique",
            "count" : 10
        }
    
    
    
    if data == "mail_domain":
        buttons = gen_domain_select_buttons(domain_map)
        buttons.append([Button.inline("Back", b"mail_back_home")])
        await event.edit(buttons=buttons)
    
    
    elif data == "mail_back_home":
        await event.edit(buttons=mail_keyboard)   
    
    elif data.startswith("mail_select_"):
        _data = data.split("_")
        domain = _data[-1] 
        
        if not sender_id in users_mail_settings:
            await event.answer()
            return
        
        users_mail_settings[sender_id]["domain"] = domain
        mail_type = users_mail_settings[sender_id]["mail_type"]  
        count = users_mail_settings[sender_id]["count"]  
        
            
        mails_list = generate_mail(domain, mail_type, count)
        msg = mail_list_msg(mails_list)
        await event.edit(f"{msg}", buttons=mail_keyboard)
    
    elif data == "mail_count":
        buttons = [
            [Button.inline("10", b"mail_count_10"), Button.inline("20", b"mail_count_20")],
            [Button.inline("30", b"mail_count_30"), Button.inline("40", b"mail_count_40")],
            [Button.inline("50", b"mail_count_50")],
            [Button.inline("Back", b"mail_back_home")]
        ]
        
        await event.edit(buttons=buttons)
    
    elif data.startswith("mail_count_"):
        _data = data.split("_")
        count = int(_data[-1])
        
        if not sender_id in users_mail_settings:
            await event.answer()
            return
        
        domain = users_mail_settings[sender_id]["domain"]  
        mail_type = users_mail_settings[sender_id]["mail_type"]  
        
        
        users_mail_settings[sender_id]["count"] = count
        
        mails_list = generate_mail(domain, mail_type, count)
        msg = mail_list_msg(mails_list)
        await event.edit(f"{msg}", buttons=mail_keyboard)
    
    elif data == "mail_type":
        
        buttons = [
            [Button.inline("Unique", b"mail_t_unique"), Button.inline("Name", b"mail_t_name")],
            [Button.inline("Back", b"mail_back_home")]
        ]
        
        await event.edit(buttons=buttons)
        
    elif data.startswith("mail_t_"):
        _data = data.split("_") 
        _type = _data[-1] 
        
        if not sender_id in users_mail_settings:
            await event.answer()
            return
        
        users_mail_settings[sender_id]["mail_type"] = _type
        domain = users_mail_settings[sender_id]["domain"]  
        count = users_mail_settings[sender_id]["count"] 
        
        mails_list = generate_mail(domain, _type, count)
        msg = mail_list_msg(mails_list)
        await event.edit(f"{msg}", buttons=mail_keyboard)
    
    
    elif data == "mail_generate":
        domain = users_mail_settings[sender_id]["domain"]  
        mail_type = users_mail_settings[sender_id]["mail_type"]  
        
        
        count = users_mail_settings[sender_id]["count"]
        
        mails_list = generate_mail(domain, mail_type, count)
        msg = mail_list_msg(mails_list)
        await event.edit(f"{msg}", buttons=mail_keyboard)
    
           
         
        
            
        
               
            
        
        
        
        
    
    





def gen_domain_select_buttons(domains: dict):
    """
    Generate inline buttons for domains, 3 per row.
    
    :param domains: dict, key=domain key, value=display text
    :return: list of list of Button objects
    """
    buttons = []
    row = []

    for i, (key, value) in enumerate(domains.items(), start=1):
        # Create button with callback_data
        callback_data = f"mail_select_{key}".encode()
        row.append(Button.inline(f"{value}", callback_data))

        # Add row after every 3 buttons
        if i % 3 == 0:
            buttons.append(row)
            row = []

    # Append remaining buttons if any
    if row:
        buttons.append(row)

    return buttons 