# Copyright (c) 2021 Itz-fork
# Don't kang this else your dad is gae

import math
import time

from unzipper import unzipperbot as client
from config import Config


# Credits: SpEcHiDe's AnyDL-Bot for Progress bar + Time formatter
async def progress_for_pyrogram(current, total, ud_type, message, start):
    now = time.time()
    diff = now - start
    #if round(diff % 10.00) == 0 or current == total:
    if round(diff % 3.00) > 2.99 or current == total:
        percentage = current * 100 / total
        speed = current / diff
        elapsed_time = round(diff) * 1000
        time_to_completion = round((total - current) / speed) * 1000
        estimated_total_time = elapsed_time + time_to_completion

        elapsed_time = TimeFormatter(milliseconds=elapsed_time)
        estimated_total_time = TimeFormatter(milliseconds=estimated_total_time)
        time_to_completion = TimeFormatter(milliseconds=time_to_completion) #time left

        progress = "\n<b>Uploading......</b> \n{0}{1} <b>{2}%</b>\n".format(
            ''.join(["●" for i in range(math.floor(percentage / 5))]),
            ''.join(["○" for i in range(20 - math.floor(percentage / 5))]),
            round(percentage, 2))

        tmp = progress + "\n🍿 **UpLoaded : {0}\n🍿 File Size : {1}**\n🍿 **Speed:** {2}/s\n🍿 **Time Left :** {3}\n".format(
            humanbytes(current),
            humanbytes(total),
            humanbytes(speed),
            #estimated_total_time if estimated_total_time != '' else "0 s"
            time_to_completion if time_to_completion != '' else  "0 s" #time left
        )
        try:
            await message.edit(text="{}\n {} \n\n**Made wit♥️by @MyTestBotZ**".format(tmp, ud_type))
        except:
            pass


def humanbytes(size):
    if not size:
        return ""
    power = 2**10
    n = 0
    Dic_powerN = {0: ' ', 1: 'Ki', 2: 'Mi', 3: 'Gi', 4: 'Ti'}
    while size > power:
        size /= power
        n += 1
    return str(round(size, 2)) + " " + Dic_powerN[n] + 'B'


def TimeFormatter(milliseconds: int) -> str:
    seconds, milliseconds = divmod(int(milliseconds), 1000)
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    days, hours = divmod(hours, 24)
    tmp = ((str(days) + "d, ") if days else "") + \
        ((str(hours) + "h, ") if hours else "") + \
        ((str(minutes) + "m, ") if minutes else "") + \
        ((str(seconds) + "s, ") if seconds else "") + \
        ((str(milliseconds) + "ms, ") if milliseconds else "")
    return tmp[:-2]

# Checking log channel
def check_logs():
    try:
        if Config.LOGS_CHANNEL:
            c_info = client.get_chat(chat_id=Config.LOGS_CHANNEL)
            if c_info.type != "channel":
                print("TF? Chat is not a channel")
                return
            elif c_info.username is not None:
                print("TF? Chat is not private")
                return
            else:
                client.send_message(chat_id=Config.LOGS_CHANNEL, text="`Unzipper-Bot has Successfully Started!` \n\n**Powered by @MyTestBotz**")
        else:
            print("No Log Channel ID is Given! Imma leaving Now!")
            exit()
    except:
        print("Error Happend while checking Log Channel! Make sure you're not dumb enough to provide a wrong Log Channel ID!")
