from pyrogram.types import Message
from pyrogram import filters
from AniPlay import app
from AniPlay.plugins.AnimeDex import AnimeDex
from AniPlay.plugins.button import BTN


@app.on_message(filters.command(['start', 'ping', 'help', 'alive']))
async def start(_, message: Message):
    try:
        await message.reply_video('https://te.legra.ph/file/95e080e5e47b5621fbf4c.mp4',caption="""𝗛𝗶 🦾

𝗜 𝗮𝗺 𝗦𝗶𝗺𝗽𝗹𝗲 𝗔𝗻𝗶𝗺𝗲 𝗦𝗲𝗮𝗿𝗰𝗵 𝗕𝗼𝘁 👁

𝗛𝗼𝘄 𝗧𝗼 𝗨𝘀𝗲 𝗠𝗲?

/search <animename>""")
    except:
        return


QUERY = '**Search Results:** `{}`'


@app.on_message(filters.command(['search', 's']))
async def searchCMD(_, message: Message):
    try:
        user = message.from_user.id
        query = ' '.join(message.command[1:])
        if query == '':
            return await message.reply_text('Give me something to search ^_^')
        data = AnimeDex.search(query)
        button = BTN.searchCMD(user, data, query)
        await message.reply_text(f'{QUERY.format(query)}\n\n© {message.from_user.mention}', reply_markup=button)
    except Exception as e:
        print(e)
        try:
            return await message.reply_text('**Anime Not Found...**\n\nProbably Incorrect Name, Try again')
        except:
            return
