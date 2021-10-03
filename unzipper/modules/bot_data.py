# Copyright (c) 2021 Itz-fork
# Don't kang this else your dad is gae

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# Inline buttons
class Buttons:
    START_BUTTON=InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("Creator", url="https://telegram.me/OO7ROBOT"),
                InlineKeyboardButton("OtherBotZ", url="https://telegram.me/mybotzlist")
            ],[
                InlineKeyboardButton("⚙️ Help 📜", callback_data="helpcallback"),
                InlineKeyboardButton("📝 About ⁉️", callback_data="aboutcallback"),
           # ],[
                InlineKeyboardButton("⛔ Cancel 🔐", callback_data="cancel_dis")
            ]
        ]
    )
    
    CHOOSE_E_BTN=InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("Extract 🗳️", callback_data="extract_file|no_pass"),
                InlineKeyboardButton("(Password) Extract 🗳️", callback_data="extract_file|with_pass")
            ],
            [
                InlineKeyboardButton("⛔ Cancel 🔐", callback_data="cancel_dis")
            ]
        ]
    )

    CLN_BTNS=InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("Clean My Files 😇", callback_data="cancel_dis")
            ],
            [
                InlineKeyboardButton("TF! Nooo 😳", callback_data="nobully")
            ]
        ]
    )
    
    ME_GOIN_HOME=InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("Back 🏡", callback_data="megoinhome")
            ]
        ]
    )


class Messages:
    START_TEXT = """
Hi 👋 **{}**,
I'm **Unzipper Bot**🗳️

__I can extract archives Telegram Files like zip, rar, tar etc.__


**Made with ❤️ by @MyTestBotZ**
    """

    HELP_TXT = """
**How To Extract? 🤔🤔🤔**

__1. Send the file that you want to extract.
2. Click on extract button.
3. wait for starting the Process..__


**Note:**
    **1.** __If your archive is password protected select__ **(Password) Extract🗳️** __mode. Bot isn't a GOD to know your file's password so If this happens just send that password!__
    
    **2.** __Please don't send corrupted files! If you sent a one by a mistake just send__ ** /clean** __command!__
    """

    ABOUT_TXT = """
**@TG_UnzipperBot**

✪ » **Creator :** [Meeeee...](https://telegram.me/OO7ROBot)
✪ » **Channel:** [MyTestBotZ](https://telegram.me/MyTestBotZ)
✪ » **Other Bots:** [Other BotZ](https://telegram.me/mybotzlist)
✪ » **Language:** [Python](https://www.python.org/)
✪ » **Framework:** [Pyrogram](https://docs.pyrogram.org/)
✪ » **Dev: Itz-fork**
✪ » **Build Version: V1**


    """

    LOG_TXT = """
**Extract Log 📝!**

**User ID:** `{}`
**File Name:** `{}`
**File Size:** `{}`
    """

    AFTER_OK_DL_TXT = """
**✅ Successfully Downloaded 📥**

**Download time:** `{}`
**Status:** `Trying to extract the archive`

**© @TG_UnZipperbot**
    """

    EXT_OK_TXT = """
**☑️ Extraction Successfull! 😌😌**

**Extraction time:** `{}`
**Status:** `Trying to upload 📤`
    """

    EXT_FAILED_TXT = """
**Extraction Failed 😕!**

**What to do?**

 - Please make sure archive isn't corrupted
 - Please make sure that you selected the right mode!
 - May be Your archive format isn't supported 😔


    """

    ERROR_TXT = """
**Error Happend 😕!**

**ERROR:** {}


    """

    CANCELLED_TXT = """
**{} ✅!**

`Now all of your files have been deleted from my server 😏!`
    """

    CLEAN_TXT = """
**Are sure want to delete your files from my server 🤔?**

**Note:** `This action cannot be undone!`
    """
