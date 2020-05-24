import telebot
import time

TOKEN = '1179891084:AAGKVT-QuP9x_ykoQfm8xp25ZnD_Ndeqxqo'


def listener(messages):
    """
    When new messages arrive TeleBot will call this function.
    """
    for m in messages:
        chatid = m.chat.id
        print(str(chatid))
        if m.content_type == 'text':
            text = m.text
            tb.send_message(chatid, text)


tb = telebot.TeleBot(TOKEN)
tb.set_update_listener(listener) #register listener
tb.polling()
#Use none_stop flag let polling will not stop when get new message occur error.
tb.polling(none_stop=True)
# Interval setup. Sleep 3 secs between request new message.
tb.polling(interval=3)

while True: # Don't let the main Thread end.
    pass

# 801016893