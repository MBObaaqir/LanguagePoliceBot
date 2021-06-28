from threading import Thread
import profanity


def polling_threading(update, context):
    Thread(target=polling_thread, args=(update, context)).start()


def polling_thread(update, context):
    profanity.profanity(update, context)
