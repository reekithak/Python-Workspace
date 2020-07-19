def my_print(txt):
    print(txt)

msg = """ hey {name} , {website}"""

def format_msg(name='akhil',website='ak.sh'):
    global msg
    msg_new = msg.format(name=name,website=website)
    #print(msg_new)
    return msg_new