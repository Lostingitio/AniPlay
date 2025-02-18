from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.types import Message, CallbackQuery, InputMediaPhoto
from pyrogram import filters
from AniPlay import app
from AniPlay.plugins.AnimeDex import AnimeDex
from AniPlay.plugins.button import BTN, cache

QUERY = '**Search Results:** `{}`'


@app.on_callback_query(filters.regex('searchBACK'))
async def searchBACK(_, query: CallbackQuery):
    user = query.from_user.id

    _, id, hash = query.data.split(' ')

    if str(user) != id:
        return await query.answer("This Is Not Your Query...")

    url = cache.get(hash)

    if not url:
        await query.answer("Search Query Expired... Try Again")
        return await query.message.delete()

    await query.answer('Loading ...')
    data = AnimeDex.search(url[1])
    button = BTN.searchCMD(user, data, url[1])
    await query.message.edit(f'{QUERY.format(url[1])}\n\n© {query.from_user.mention}', reply_markup=button)


@app.on_callback_query(filters.regex('AnimeS'))
async def AnimeS(_, query: CallbackQuery):
    user = query.from_user.id

    _, id, hash = query.data.split(' ')

    if str(user) != id:
        return await query.answer("This Is Not Your Query...")

    anime = cache.get(hash)
    print(anime)

    if not anime:
        await query.answer("Search Query Expired... Try Again")
        return await query.message.delete()

    await query.answer('Loading ...')
    img, text, ep = AnimeDex.anime(anime[0])
    
    text += '\n\n© ' + query.from_user.mention
    button = BTN.AnimeS(id, ep, hash)

    if query.message.photo:
        await query.message.edit_media(media=InputMediaPhoto(img, caption=text), reply_markup=button)
    else:
        try:
            await query.message.reply_to_message.reply_photo(photo=img, caption=text, reply_markup=button)
        except:
            await query.message.reply_photo(photo=img, caption=text, reply_markup=button)
        await query.message.delete()


@app.on_callback_query(filters.regex('episode'))
async def episode(_, query: CallbackQuery):
    user = query.from_user.id

    _, id, hash = query.data.split(' ')

    if str(user) != id:
        return await query.answer("This Is Not Your Query...")

    epid = cache.get(hash)

    if not epid:
        await query.answer("Search Query Expired... Try Again")
        return await query.message.delete()

    await query.answer('Loading ...')
    text, surl, murl = AnimeDex.episode(epid[0])
    button = BTN.episode(id, surl, murl, epid[1])

    await query.message.edit(f'**{text}**\n\n© {query.from_user.mention}', reply_markup=button)


@app.on_callback_query(filters.regex('line'))
async def liner(_, query: CallbackQuery):
    try:
        await query.answer()
    except:
        return


@app.on_callback_query(filters.regex('engSUB'))
async def engSub(_, query: CallbackQuery):
    try:
        await query.answer('Direct Stream Urls')
    except:
        return


@app.on_callback_query(filters.regex('engDUB'))
async def engDub(_, query: CallbackQuery):
    try:
        await query.answer('Mirror Stream Urls')
    except:
        return


@app.on_callback_query(filters.regex('switch_ep'))
async def switch_ep(_, query: CallbackQuery):
    user = query.from_user.id

    _, id, hash, pos = query.data.split(' ')

    if str(user) != id:
        return await query.answer("This Is Not Your Query...")

    data = cache.get(hash)

    if not data:
        await query.answer("Search Query Expired... Try Again")
        return await query.message.delete()

    await query.answer('Loading ...')
    pos = int(pos)
    current = data[0][pos]
    await query.edit_message_reply_markup(reply_markup=InlineKeyboardMarkup(current))


@app.on_callback_query(filters.regex('switch_anime'))
async def switch_anime(_, query: CallbackQuery):
    user = query.from_user.id

    _, id, hash, pos = query.data.split(' ')

    if str(user) != id:
        return await query.answer("This Is Not Your Query...")

    data: list = cache.get(hash)

    if not data:
        await query.answer("Search Query Expired... Try Again")
        return await query.message.delete()

    await query.answer('Loading ...')

    pos = int(pos)
    current = data[0][pos]
    await query.edit_message_reply_markup(reply_markup=InlineKeyboardMarkup(current))
