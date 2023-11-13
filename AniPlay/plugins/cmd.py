from pyrogram.types import Message
from pyrogram import filters
from AniPlay import app
from AniPlay.plugins.AnimeDex import AnimeDex
from AniPlay.plugins.button import BTN


@app.on_message(filters.command(['start', 'ping', 'help', 'alive']))
async def start(_, message: Message):
    try:
        await message.reply_text('Bot Is Online...\n\nSearch Animes Using /search <anime name> or /s <anime name>')
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
