from telegram.ext import MessageHandler, filters, ContextTypes, CallbackContext
from telegram import Chat, Update


async def correct_link(update: Update, context: ContextTypes.DEFAULT_TYPE):
    '''
    input 'https://www.instagram.com/reel/C6V2sNYNxy7/?igsh=aXBjYmVlZzl5ZjJw'
    output https://www.ddinstagram.com/reel/C6V2sNYNxy7/?igsh=aXBjYmVlZzl5ZjJw
    '''
    chat_id = update.effective_chat.id
    full_name = update.message.from_user.full_name
    nickname = update.message.from_user.name
    _id = update.message.id
    text = update.message.text
    
    delete_result = await context.bot.delete_message(
        message_id=_id,
        chat_id=chat_id
    )

    if delete_result:
        new_link = (
            f'message from {full_name} ({nickname})\n'
            f'{text[:12]}dd{text[12:]}'
        )
        await context.bot.send_message(
            chat_id=chat_id,
            text=new_link
        )

    return None

message_handler: MessageHandler = MessageHandler(
    filters= filters.Regex(pattern=r"https:\/\/www.instagram.com\/reel\/"),
    callback=correct_link
)
