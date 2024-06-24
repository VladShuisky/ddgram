import re
from telegram.ext import MessageHandler, filters, ContextTypes, CallbackContext, MessageReactionHandler
from telegram import Chat, Update
import config


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


async def redirect_reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    _from = update.message.reply_to_message.from_user.username
    if _from == config.BOT_USERNAME:
        msg_text = update.message.reply_to_message.text
        origin_message_id: int = update.message.reply_to_message.id
        text_for_recipient = update.message.text
        try:
            recipient_nickname: str = re.findall(
                r'\(@[a-zA-z]{1,}\)',
                msg_text
            )[0][1:-1]
            from_user = update.message.from_user
            send_res = await context.bot.send_message(
                reply_to_message_id=origin_message_id,
                text=(
                    f'to {recipient_nickname} '
                    f'от {from_user.first_name} {from_user.last_name}: '
                    f'"{text_for_recipient}"'
                ),
                chat_id=update.message.chat.id
            )
            if send_res:
                await context.bot.delete_message(
                    chat_id=update.message.chat.id,
                    message_id=update.message.id
                )
        except KeyError:
            print(
                f'Попытка ботом сделать reply '
                f'оказалась неудачной, так как'
                f'В сообщении не оказалось (@username) '
                f'чтобы сослаться на пользователя'
            )

reply_handler = MessageHandler(
    filters=filters.REPLY,
    callback=redirect_reply
)
