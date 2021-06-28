from time import sleep
import telegram
import badWords


def profanity(update, context):
    msg = update.message
    if msg is not None:
        message_chat_id = msg.chat.id
    else:
        return  # If abnormal message (msg is NoneType: if message is sent by group itself)

    # If bad word found, then delete the message
    for word in update.message.text.split():
        if word.lower() in badWords.bad_words:
            try:
                context.bot.delete_message(chat_id=message_chat_id, message_id=update.message.message_id)
                # Send warning message
                user = update.message.from_user
                name = user.name  # username, if it doesn't exist then full name (First Last)
                sent_message = context.bot.send_message(chat_id=update.effective_chat.id,
                                                        text=message_deleted_message(name),
                                                        parse_mode=telegram.ParseMode.HTML)
                sleep(5)  # Delay before deleting warning message
                # Delete warning message
                try:
                    context.bot.delete_message(chat_id=sent_message.chat.id, message_id=sent_message.message_id)
                except:  # If message has already been deleted
                    pass
                return
            except:  # If message has already been deleted
                return


def message_deleted_message(name):
    return (f"{name}\n\n"
            "Your message is being deleted. Any message that includes inappropriate language will be deleted!"
            "\n\nPlease do not use inappropriate language in your future messages. Thank you."
            )
