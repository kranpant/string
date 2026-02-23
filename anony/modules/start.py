from pyrogram import filters, types

from anony import app, buttons, db


@app.on_message(filters.command(["start"]) & filters.private)
async def f_start(_, m: types.Message):
    await m.reply_text(
        text=f"ʜᴇʏ {m.from_user.first_name},\n\n๏ ᴛʜɪs ɪs {app.mention},\nAɴ ᴏᴘᴇɴ sᴏᴜʀᴄᴇ sᴛʀɪɴɢ sᴇssɪᴏɴ ɢᴇɴᴇʀᴀᴛᴏʀ ʙᴏᴛ, ᴡʀɪᴛᴛᴇɴ ɪɴ ᴩʏᴛʜᴏɴ ᴡɪᴛʜ ᴛʜᴇ ʜᴇʟᴩ ᴏғ ᴩʏʀᴏɢʀᴀᴍ.",
        reply_markup=buttons.start_key(),
    )
    await db.add_user(m.from_user.id)
