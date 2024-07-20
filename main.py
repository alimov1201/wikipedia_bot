from aiogram import Bot, Dispatcher, types 
import wikipedia
import asyncio

bot = Bot(token="7456886719:AAFRX69gupXWpCpAGAT3-DsZ5nsHHP05rYs")
dp = Dispatcher(bot=bot)

wikipedia.set_lang('en')

@dp.message()
async def yap(message: types.Message):
    try:
        b = wikipedia.summary(message.text)
        await message.reply(text=f"{b}")
    except:
        await message.reply('information not found!')


async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())