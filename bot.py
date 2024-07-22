from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from buttons import check_sub,button,cancel
from config import *
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext

API_TOKEN = '1786216580:AAE0jLAxr51AD1hHPMQLGjWSmUi-2yZafWE'
bot = Bot(token=API_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot,storage=storage)

class call(StatesGroup):
    text = State()
    
async def on_startup(dp):
    await bot.send_message(chat_id='770608643', text='Бот запущен')

async def on_shutdown(dp):

    await bot.send_message(chat_id='770608643', text='Бот остановлен')

async def check_sub_group(chat_member):
    if chat_member['status'] != 'left':
        return True
    else:
        return False



@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    if message.chat.type == "private":
        chat_member = await bot.get_chat_member(chat_id=channel_id, user_id=message.from_user.id)
        if await check_sub_group(chat_member):  # Используйте await здесь
            await bot.send_message(message.from_user.id, "Assalawma aleykum!", reply_markup=button)
        else:
            await bot.send_message(chat_id=message.from_user.id, text="Botdan paydalaniw ushin gruppamizg`a qosilin",
                                   reply_markup=check_sub)





@dp.message_handler(content_types=['new_chat_members', 'left_chat_member'])
async def handle_new_chat_members(message: types.Message):
    await message.delete()

@dp.callback_query_handler(text="subdone")
async def subgroupdone(message: types.Message):
    await bot.delete_message(message.from_user.id,message.message.message_id)
    chat_member = await bot.get_chat_member(chat_id=channel_id, user_id=message.from_user.id)
    if await check_sub_group(chat_member):
        await bot.send_message(message.from_user.id, "Assalawma aleykum!", reply_markup=button)
    else:
        await bot.send_message(chat_id=message.from_user.id, text="Botdan paydalaniw ushin gruppamizg`a qosilin",
                                   reply_markup=check_sub)
    
@dp.message_handler(text="Profile")
async def handle_new_chat_members(message: types.Message):
    chat_member = await bot.get_chat_member(chat_id=channel_id, user_id=message.from_user.id)
    if await check_sub_group(chat_member):
        first_name = message.from_user.first_name
        last_name = message.from_user.last_name
        username = message.from_user.username
        await message.answer(f"Name: {first_name}\nSurname: {last_name}\nUsername: {username}")
    else:
        await bot.send_message(chat_id=message.from_user.id, text="Botdan paydalaniw ushin gruppamizg`a qosilin",
                                   reply_markup=check_sub)


@dp.message_handler(text="Help")
async def handle_new_chat_members(message: types.Message):
    chat_member = await bot.get_chat_member(chat_id=channel_id, user_id=message.from_user.id)
    if await check_sub_group(chat_member):
        await message.answer("Soraw ham usinislarinizdi bolsa jazip qaldirin",reply_markup=cancel)
        await call.text.set()
    else:
        await bot.send_message(chat_id=message.from_user.id, text="Botdan paydalaniw ushin gruppamizg`a qosilin",
                                   reply_markup=check_sub)

@dp.message_handler(state=call.text)
async def handle_text(message: types.Message,state: FSMContext):
    if message.text == "Cancel":
        await message.answer("Cancelled",reply_markup=button)
        await state.finish()
    else:
        text= message.text
        username = message.from_user.username
        name = message.from_user.first_name
        lastname = message.from_user.last_name
        await bot.send_message(chat_id=admin,text=f"Jana xabar: \n{text} \n\nXabardi jollag`an: \nName: {name} {lastname} \nUsername: @{username}")
        await message.answer("Xabariniz ushin raxmet! \nXabar adminstratorga jetkizildi",reply_markup=button)
        await state.finish()
if __name__ == '__main__':
    from aiogram import executor
    executor.start_polling(dp, skip_updates=True,on_startup=on_startup, on_shutdown=on_shutdown)