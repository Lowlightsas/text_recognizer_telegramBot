import os
from aiogram import Bot, Dispatcher, executor, types
from main import text_recognition
from bot_token import bot_token

bot = Bot(bot_token)
dp = Dispatcher(bot)
help_command = '''
/help - список команд,
/start - запуск бота
'''
new_saved_file = 'C:/Users/fhjj3/Music/testingFaces'

@dp.message_handler(commands=['start'])
async def start_commands(message: types.Message):
    await message.answer(text='Привет ! Кидайте мне фото чека')

@dp.message_handler(content_types=types.ContentTypes.PHOTO)
async def handle_photo(message: types.Message):

    photo = message.photo[-1]

    file_name = 'saved.jpg'

    photo_info = await bot.get_file(photo.file_id)
    file = await bot.download_file(photo_info.file_path)

    with open(file_name,'wb') as new_file:
        new_file.write(file.read())

    await message.answer('Фото сохранена')

    import shutil

    async def SaveFile(src, dst):
        try:
            shutil.copy(src, dst)
        except Exception as e:
            print(f"Ошибка при копировании файла: {e}")
        else:
            print(f"Файл скопирован успешно")

    await SaveFile(file_name, new_saved_file)
    folder_path = 'C:/Users/fhjj3/Music/testingFaces'

    image_files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]

    image_paths = [os.path.join(folder_path, f) for f in image_files]

    async def main(image_path):

        await message.answer(text_recognition(file_path=image_path))
    for image_path in image_paths:
        await main(image_path)

if __name__ == '__main__':

    executor.start_polling(dp,on_startup=None)
