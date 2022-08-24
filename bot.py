import os
import telebot
import fnmatch
import asyncio
from telebot.async_telebot import AsyncTeleBot

botToken = os.environ['token']

bot = AsyncTeleBot(botToken, parse_mode=None)

print("spotBot is up and running.")

@bot.message_handler(commands=['help'])
async def send_welcome(message):
    await bot.reply_to(message, """\
This bot can download songs / albums / playlists from Spotify (FLAC, MP3, M4A, WAV) & Soundcloud (MP3).
Send a spotify song link to see the magic.
Use /flac for FLACs.
Use /mp3 for MP3s.
Use /m4a for M4As.
Use /wav for WAVs.
Use /sc to download songs from SoundCloud. Only LINKS are supported!

For example: /flac https://open.spotify.com/track/2iUXsYOEPhVqEBwsqP70rE?si=833f974040c341d0
OR: /flac rewrite the stars anne marie

This bot uses spotDL (https://github.com/spotDL). Hats off to their work.
This bot uses scdl (https://github.com/flyingrub/scdl). Hats off to their work.
This bot uses pyTelegramBotAPI (https://github.com/eternnoir/pyTelegramBotAPI).
This bot forked from https://github.com/Diaz1401/SpotifyTeleBot.
Bot source code is available at https://github.com/rain2wood/spotBot-OSS.
\
""")

@bot.message_handler(commands=['faq'])
async def faq(message):
    await bot.reply_to(message, """ \
    Q: My song isn't right! What Can I do?
    A: Try to use another Spotify link.

    Q: My lyrics aren't right! What can I do?
    A: I don't know either. Just don't read lyrics.

    Note that the tool fetches results from YouTube Music and it isn't 100 percent accurate.
    \
    """)
@bot.message_handler(commands=['up'])
async def up_check(message):
    await bot.reply_to(message, "Bot is up and running.")

@bot.message_handler(commands=['flac'])
async def download_flac(message):
    chat_id = message.chat.id
    songLink = message.text
    str = songLink
    if str.find("track")!=-1:
        print("is track")
        realSong = songLink.replace("/flac", "")
        await bot.reply_to(message, "Fetching song...")
        DownloadSong = "bash magic.sh '{}' flac -t".format(realSong)
        os.system(DownloadSong)
        f = open("link.txt", "r")
        text = f.read()
        await bot.send_message(chat_id, text)
        cleansong = "rm -rf link.txt"
        os.system(cleansong)
    elif str.find("album")!=-1 or str.find("playlist")!=-1:
        print("is album or playlist")
        realSong = songLink.replace("/flac", "")
        await bot.reply_to(message, "Fetching album / playlist. This will take a while.")
        DownloadSong = "bash magic.sh '{}' flac -a".format(realSong)
        os.system(DownloadSong)
        f = open("link.txt", "r")
        text = f.read()
        await bot.send_message(chat_id, text)
        cleansong = "rm -rf link.txt"
        os.system(cleansong)
    else:
        print("is maybe query")
        realSong = songLink.replace("/flac", "")
        tryQuery = "Trying to search for '{}' on Spotify...".format(realSong)
        await bot.reply_to(message, tryQuery)
        DownloadSong = "bash magic.sh '{}' flac -t".format(realSong)
        os.system(DownloadSong)
        f = open("link.txt", "r")
        text = f.read()
        await bot.send_message(chat_id, text)
        cleansong = "rm -rf link.txt"
        os.system(cleansong)

@bot.message_handler(commands=['mp3'])
async def download_mp3(message):
    chat_id = message.chat.id
    songLink = message.text
    str = songLink
    if str.find("track")!=-1:
        print("is track")
        realSong = songLink.replace("/mp3", "")
        await bot.reply_to(message, "Fetching song...")
        DownloadSong = "bash magic.sh '{}' mp3 -t".format(realSong)
        os.system(DownloadSong)
        f = open("link.txt", "r")
        text = f.read()
        await bot.send_message(chat_id, text)
        cleansong = "rm -rf link.txt"
        os.system(cleansong)
    elif str.find("album")!=-1 or str.find("playlist")!=-1:
        print("is album or playlist")
        realSong = songLink.replace("/mp3", "")
        await bot.reply_to(message, "Fetching album / playlist. This will take a while.")
        DownloadSong = "bash magic.sh '{}' mp3 -a".format(realSong)
        os.system(DownloadSong)
        f = open("link.txt", "r")
        text = f.read()
        await bot.send_message(chat_id, text)
        cleansong = "rm -rf link.txt"
        os.system(cleansong)
    else:
        print("is maybe query")
        realSong = songLink.replace("/mp3", "")
        tryQuery = "Trying to search for '{}' on Spotify...".format(realSong)
        await bot.reply_to(message, tryQuery)
        DownloadSong = "bash magic.sh '{}' mp3 -t".format(realSong)
        os.system(DownloadSong)
        f = open("link.txt", "r")
        text = f.read()
        await bot.send_message(chat_id, text)
        cleansong = "rm -rf link.txt"
        os.system(cleansong)

@bot.message_handler(commands=['wav'])
async def download_mp3(message):
    chat_id = message.chat.id
    songLink = message.text
    str = songLink
    if str.find("track")!=-1:
        print("is track")
        realSong = songLink.replace("/wav", "")
        await bot.reply_to(message, "Fetching song...")
        DownloadSong = "bash magic.sh '{}' wav -t".format(realSong)
        os.system(DownloadSong)
        f = open("link.txt", "r")
        text = f.read()
        await bot.send_message(chat_id, text)
        cleansong = "rm -rf link.txt"
        os.system(cleansong)
    elif str.find("album")!=-1 or str.find("playlist")!=-1:
        print("is album or playlist")
        realSong = songLink.replace("/wav", "")
        await bot.reply_to(message, "Fetching album / playlist. This will take a while.")
        DownloadSong = "bash magic.sh '{}' wav -a".format(realSong)
        os.system(DownloadSong)
        f = open("link.txt", "r")
        text = f.read()
        await bot.send_message(chat_id, text)
        cleansong = "rm -rf link.txt"
        os.system(cleansong)
    else:
        print("is maybe query")
        realSong = songLink.replace("/wav", "")
        tryQuery = "Trying to search for '{}' on Spotify...".format(realSong)
        await bot.reply_to(message, tryQuery)
        DownloadSong = "bash magic.sh '{}' wav -t".format(realSong)
        os.system(DownloadSong)
        f = open("link.txt", "r")
        text = f.read()
        await bot.send_message(chat_id, text)
        cleansong = "rm -rf link.txt"
        os.system(cleansong)

@bot.message_handler(commands=['m4a'])
async def download_mp3(message):
    chat_id = message.chat.id
    songLink = message.text
    str = songLink
    if str.find("track")!=-1:
        print("is track")
        realSong = songLink.replace("/m4a", "")
        await bot.reply_to(message, "Fetching song...")
        DownloadSong = "bash magic.sh '{}' m4a -t".format(realSong)
        os.system(DownloadSong)
        f = open("link.txt", "r")
        text = f.read()
        await bot.send_message(chat_id, text)
        cleansong = "rm -rf link.txt"
        os.system(cleansong)
    elif str.find("album")!=-1 or str.find("playlist")!=-1:
        print("is album or playlist")
        realSong = songLink.replace("/m4a", "")
        await bot.reply_to(message, "Fetching album / playlist. This will take a while.")
        DownloadSong = "bash magic.sh '{}' m4a -a".format(realSong)
        os.system(DownloadSong)
        f = open("link.txt", "r")
        text = f.read()
        await bot.send_message(chat_id, text)
        cleansong = "rm -rf link.txt"
        os.system(cleansong)
    else:
        print("is maybe query")
        realSong = songLink.replace("/m4a", "")
        tryQuery = "Trying to search for '{}' on Spotify...".format(realSong)
        await bot.reply_to(message, tryQuery)
        DownloadSong = "bash magic.sh '{}' m4a -t".format(realSong)
        os.system(DownloadSong)
        f = open("link.txt", "r")
        text = f.read()
        await bot.send_message(chat_id, text)
        cleansong = "rm -rf link.txt"
        os.system(cleansong)

@bot.message_handler(commands=['sc'])
async def download_soundcloud(message):
    chat_id = message.chat.id
    songLink = message.text
    realSong = songLink.replace("/sc", "")
    print("attempt to download track from soundcloud")
    await bot.reply_to(message, "Fetching song from link...")
    DownloadSong = "bash magic.sh {} -sc -x".format(realSong)
    os.system(DownloadSong)
    f = open("link.txt", "r")
    text = f.read()
    await bot.send_message(chat_id, text)
    cleansong = "rm -rf link.txt"
    os.system(cleansong)

asyncio.run(bot.infinity_polling())