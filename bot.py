import logging
#import os
import asyncio
from telethon import TelegramClient, events, Button
from decouple import config
from telethon.tl.functions.users import GetFullUserRequest

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s', level=logging.INFO)
print("Starting The Bot With Given Details.")
try:
    apiid = config("APP_ID", cast=int)
    apihash = config("API_HASH")
    bottoken = config("BOT_TOKEN")
    frm = config("FROM_CHANNEL", cast=int)
    tochnl = config("TO_CHANNEL", cast=int)
    tochnl0 = config("TO_CHANNEL0", cast=int)
    tochnl1 = config("TO_CHANNEL1", cast=int)
    tochnl2 = config("TO_CHANNEL2", cast=int)
    tochnl3 = config("TO_CHANNEL3", cast=int)
    tochnl4 = config("TO_CHANNEL4", cast=int)
    tochnl5 = config("TO_CHANNEL5", cast=int)
    Bot = TelegramClient('bot', apiid, apihash).start(bot_token=bottoken)
except:
    print("Environment vars are missing! Kindly recheck.")
    print("Bot is quiting...")
    exit()


@Bot.on(events.NewMessage(pattern="/start"))
async def _(event):
    ok = await Bot(GetFullUserRequest(event.sender_id))
    await event.reply(f"Hi {mention}`!\n\nThis bot can send all new messages from one channel to another channel or group without the forwarded tag!", buttons=[Button.url("Repo", url="https://github.com/xditya/ChannelAutoForwarder"), Button.url("Dev", url="https://t.me/JAsuran123")], link_preview=False)


@Bot.on(events.NewMessage(pattern="/help"))
async def helpp(event):
    await event.reply("**Help**\n\nThis bot will send all new posts in one channel to the other channel. (without forwarded tag)!\nIt can be used only in two channels at a time, so kindly deploy your own bot from [here](https://github.com/xditya/ChannelAutoForwarder).\n\nAdd me to both the channels and make me an admin in both, and all new messages would be autoposted on the linked channel!!\n\nLiked the bot? Drop a ♥ to @JAsuran123 :)")

@Bot.on(events.NewMessage(incoming=True, chats=frm)) 
async def _(event): 
    if not event.is_private:
        try:
            if event.poll:
                return
            if event.photo:
                photo = event.media.photo
                await Bot.send_file(tochnl, photo, caption = event.text, link_preview = False)
            elif event.media:
                try:
                    if event.media.webpage:
                        await Bot.send_message(tochnl, event.text, link_preview = False)
                        return
                except:
                    media = event.media.document
                    await Bot.send_file(tochnl, media, caption = event.text, link_preview = False)
                    return
            else:
                await Bot.send_message(tochnl, event.text, link_preview = False)
        except:
            print("TO_CHANNEL ID is wrong or I can't send messages there (make me admin).")

##
@Bot.on(events.NewMessage(incoming=True, chats=frm)) 
async def _(event0): 
    if not event0.is_private:
        try:
            if event0.poll:
                return
            if event0.photo:
                photo = event0.media.photo
                await Bot.send_file(tochnl0, photo, caption = event0.text, link_preview = False)
            elif event0.media:
                try:
                    if event0.media.webpage:
                        await Bot.send_message(tochnl0, event0.text, link_preview = False)
                        return
                except:
                    media = event0.media.document
                    await Bot.send_file(tochnl0, media, caption = event0.text, link_preview = False)
                    return
            else:
                await Bot.send_message(tochnl0, event1.text, link_preview = False)
        except:
            print("TO_CHANNEL ID0 is wrong or I can't send messages there (make me admin).")

@Bot.on(events.NewMessage(incoming=True, chats=frm)) 
async def _(event1): 
    if not event1.is_private:
        try:
            if event1.poll:
                return
            if event1.photo:
                photo = event1.media.photo
                await Bot.send_file(tochnl1, photo, caption = event1.text, link_preview = False)
            elif event1.media:
                try:
                    if event1.media.webpage:
                        await Bot.send_message(tochnl1, event1.text, link_preview = False)
                        return
                except:
                    media = event1.media.document
                    await Bot.send_file(tochnl1, media, caption = event1.text, link_preview = False)
                    return
            else:
                await Bot.send_message(tochnl1, event1.text, link_preview = False)
        except:
            print("TO_CHANNEL ID1 is wrong or I can't send messages there (make me admin).")

@Bot.on(events.NewMessage(incoming=True, chats=frm)) 
async def _(event2): 
    if not event2.is_private:
        try:
            if event2.poll:
                return
            if event2.photo:
                photo = event2.media.photo
                await Bot.send_file(tochnl2, photo, caption = event2.text, link_preview = False)
            elif event2.media:
                try:
                    if event2.media.webpage:
                        await Bot.send_message(tochnl2, event2.text, link_preview = False)
                        return
                except:
                    media = event2.media.document
                    await Bot.send_file(tochnl2, media, caption = event2.text, link_preview = False)
                    return
            else:
                await Bot.send_message(tochnl2, event2.text, link_preview = False)
        except:
            print("TO_CHANNEL ID2 is wrong or I can't send messages there (make me admin).")

@Bot.on(events.NewMessage(incoming=True, chats=frm)) 
async def _(event3): 
    if not event3.is_private:
        try:
            if event3.poll:
                return
            if event3.photo:
                photo = event3.media.photo
                await Bot.send_file(tochnl3, photo, caption = event3.text, link_preview = False)
            elif event3.media:
                try:
                    if event3.media.webpage:
                        await Bot.send_message(tochnl3, event3.text, link_preview = False)
                        return
                except:
                    media = event3.media.document
                    await Bot.send_file(tochnl3, media, caption = event3.text, link_preview = False)
                    return
            else:
                await Bot.send_message(tochnl3, event3.text, link_preview = False)
        except:
            print("TO_CHANNEL ID3 is wrong or I can't send messages there (make me admin).")
@Bot.on(events.NewMessage(incoming=True, chats=frm)) 
async def _(event4): 
    if not event4.is_private:
        try:
            if event4.poll:
                return
            if event4.photo:
                photo = event4.media.photo
                await Bot.send_file(tochnl4, photo, caption = event4.text, link_preview = False)
            elif event4.media:
                try:
                    if event4.media.webpage:
                        await Bot.send_message(tochnl4, event4.text, link_preview = False)
                        return
                except:
                    media = event4.media.document
                    await Bot.send_file(tochnl4, media, caption = event4.text, link_preview = False)
                    return
            else:
                await Bot.send_message(tochnl4, event4.text, link_preview = False)
        except:
            print("TO_CHANNEL ID4 is wrong or I can't send messages there (make me admin).")

@Bot.on(events.NewMessage(incoming=True, chats=frm)) 
async def _(event5): 
    if not event5.is_private:
        try:
            if event5.poll:
                return
            if event5.photo:
                photo = event5.media.photo
                await Bot.send_file(tochnl5, photo, caption = event5.text, link_preview = False)
            elif event5.media:
                try:
                    if event5.media.webpage:
                        await Bot.send_message(tochnl5, event5.text, link_preview = False)
                        return
                except:
                    media = event5.media.document
                    await Bot.send_file(tochnl5, media, caption = event5.text, link_preview = False)
                    return
            else:
                await Bot.send_message(tochnl5, event5.text, link_preview = False)
        except:
            print("TO_CHANNEL ID5 is wrong or I can't send messages there (make me admin).")

print("Bot has started.")
print("Do visit JAsuran")
Bot.run_until_disconnected()
