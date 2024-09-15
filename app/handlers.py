from aiogram import Router, F
from aiogram.types import Message, CallbackQuery, FSInputFile, InputMediaPhoto, InlineKeyboardButton
from aiogram.filters import CommandStart
from aiogram.utils.keyboard import InlineKeyboardBuilder
import app.keyboards as kb
from config import ADMIN_ID, users
import main


router = Router()


@router.message(CommandStart())
async def start(message: Message):
    await message.answer_photo(photo=FSInputFile(path='photo1.jpg'), caption=f'Привет <b>{message.from_user.first_name}</b>,\nЭто бот чтобы узнать домашку 📖✍️', reply_markup=kb.start, parse_mode='html')
    users[message.from_user.id] = {'week': 0, 'day': 0, 'group': 2, 'subject': ''}


@router.callback_query(F.data == 'dz')
async def dz(callback: CallbackQuery):
    if callback.from_user.id == ADMIN_ID:
        dzkb = kb.admin_dz
    else:
        dzkb = kb.dz
    main.create_image_from_excel(users[callback.from_user.id]['week'])
    await callback.answer()
    await callback.message.edit_media(InputMediaPhoto(media=FSInputFile(path='week-%d.jpg' % (main.get_week_number() + users[callback.from_user.id]['week']))))
    await callback.message.edit_caption(caption=f'Вот д/з на эту неделю {main.dz_day(users[callback.from_user.id]['day'], users[callback.from_user.id]['week'])} {main.dz_for_day(day=users[callback.from_user.id]['day'], number=users[callback.from_user.id]['week'], group=users[callback.from_user.id]['group'])}', reply_markup=dzkb)


@router.callback_query(F.data == '+week')
async def plus_week(callback: CallbackQuery):
    if callback.from_user.id == ADMIN_ID:
        dzkb = kb.admin_dz
    else:
        dzkb = kb.dz
    users[callback.from_user.id]['day'] = 0
    if users[callback.from_user.id]['week'] == 1:
        await callback.answer(text='Вы на последней неделе, дальше идти вы не можете 🚫', show_alert=True)
    elif users[callback.from_user.id]['week'] == -1:
        users[callback.from_user.id]['week'] += 1
        main.create_image_from_excel(users[callback.from_user.id]['week'])
        await callback.answer()
        await callback.message.edit_media(InputMediaPhoto(media=FSInputFile(path=f'week-{main.get_week_number() + users[callback.from_user.id]['week']}.jpg')))
        await callback.message.edit_caption(caption=f'Вот д/з на эту неделю {main.dz_day(users[callback.from_user.id]['day'], users[callback.from_user.id]['week'])} {main.dz_for_day(day=users[callback.from_user.id]['day'], number=users[callback.from_user.id]['week'], group=users[callback.from_user.id]['group'])}', reply_markup=dzkb)
    else:
        users[callback.from_user.id]['week'] += 1
        main.create_image_from_excel(users[callback.from_user.id]['week'])
        await callback.answer()
        await callback.message.edit_media(InputMediaPhoto(media=FSInputFile(path=f'week-{main.get_week_number() + users[callback.from_user.id]['week']}.jpg')))
        await callback.message.edit_caption(caption=f'Вот д/з на следующую неделю {main.dz_day(users[callback.from_user.id]['day'], users[callback.from_user.id]['week'])} {main.dz_for_day(day=users[callback.from_user.id]['day'], number=users[callback.from_user.id]['week'], group=users[callback.from_user.id]['group'])}', reply_markup=dzkb)


@router.callback_query(F.data == '-week')
async def minus_week(callback: CallbackQuery):
    if callback.from_user.id == ADMIN_ID:
        dzkb = kb.admin_dz
    else:
        dzkb = kb.dz
    users[callback.from_user.id]['day'] = 4
    if users[callback.from_user.id]['week'] == -1:
        await callback.answer(text='Вы на последней неделе, дальше идти вы не можете 🚫', show_alert=True)
    elif users[callback.from_user.id]['week'] == 1:
        users[callback.from_user.id]['week'] -= 1
        main.create_image_from_excel(users[callback.from_user.id]['week'])
        await callback.answer()
        await callback.message.edit_media(InputMediaPhoto(media=FSInputFile(path=f'week-{main.get_week_number() + users[callback.from_user.id]['week']}.jpg')))
        await callback.message.edit_caption(caption=f'Вот д/з на эту неделю {main.dz_day(users[callback.from_user.id]['day'], users[callback.from_user.id]['week'])} {main.dz_for_day(day=users[callback.from_user.id]['day'], number=users[callback.from_user.id]['week'], group=users[callback.from_user.id]['group'])}', reply_markup=dzkb)
    else:
        users[callback.from_user.id]['week'] -= 1
        main.create_image_from_excel(users[callback.from_user.id]['week'])
        await callback.answer()
        await callback.message.edit_media(InputMediaPhoto(media=FSInputFile(path=f'week-{main.get_week_number() + users[callback.from_user.id]['week']}.jpg')))
        await callback.message.edit_caption(caption=f'Вот д/з прошлой недели {main.dz_day(users[callback.from_user.id]['day'], users[callback.from_user.id]['week'])} {main.dz_for_day(day=users[callback.from_user.id]['day'], number=users[callback.from_user.id]['week'], group=users[callback.from_user.id]['group'])}', reply_markup=dzkb)


@router.callback_query(F.data == '1')
async def first_group(callback: CallbackQuery):
    if users[callback.from_user.id]['group'] == 1:
        await callback.answer(text='Вы уже выбрали 1 группу 🚫', show_alert=True)
    else:
        if callback.from_user.id == ADMIN_ID:
            dzkb = kb.admin_dz
        else:
            dzkb = kb.dz
        users[callback.from_user.id]['group'] = 1
        main.create_image_from_excel(users[callback.from_user.id]['week'])
        await callback.answer()
        await callback.message.edit_media(InputMediaPhoto(media=FSInputFile(path=f'week-{main.get_week_number() + users[callback.from_user.id]['week']}.jpg')))
        if users[callback.from_user.id]['week'] == 0:
            await callback.message.edit_caption(caption=f'Вот д/з на эту неделю {main.dz_day(users[callback.from_user.id]['day'], users[callback.from_user.id]['week'])} {main.dz_for_day(day=users[callback.from_user.id]['day'], number=users[callback.from_user.id]['week'], group=users[callback.from_user.id]['group'])}', reply_markup=dzkb)
        elif users[callback.from_user.id]['week'] == 1:
            await callback.message.edit_caption(caption=f'Вот д/з на следующую неделю {main.dz_day(users[callback.from_user.id]['day'], users[callback.from_user.id]['week'])} {main.dz_for_day(day=users[callback.from_user.id]['day'], number=users[callback.from_user.id]['week'], group=users[callback.from_user.id]['group'])}', reply_markup=dzkb)
        else:
            await callback.message.edit_caption(caption=f'Вот д/з прошлой недели {main.dz_day(users[callback.from_user.id]['day'], users[callback.from_user.id]['week'])} {main.dz_for_day(day=users[callback.from_user.id]['day'], number=users[callback.from_user.id]['week'], group=users[callback.from_user.id]['group'])}', reply_markup=dzkb)

@router.callback_query(F.data == '2')
async def second_group(callback: CallbackQuery):
    if users[callback.from_user.id]['group'] == 2:
        await callback.answer(text='Вы уже выбрали 2 группу 🚫', show_alert=True)
    else:
        if callback.from_user.id == ADMIN_ID:
            dzkb = kb.admin_dz
        else:
            dzkb = kb.dz
        users[callback.from_user.id]['group'] = 2
        main.create_image_from_excel(users[callback.from_user.id]['week'])
        await callback.answer()
        await callback.message.edit_media(InputMediaPhoto(media=FSInputFile(path=f'week-{main.get_week_number() + users[callback.from_user.id]['week']}.jpg')))
        if users[callback.from_user.id]['week'] == 0:
            await callback.message.edit_caption(caption=f'Вот д/з на эту неделю {main.dz_day(users[callback.from_user.id]['day'], users[callback.from_user.id]['week'])} {main.dz_for_day(day=users[callback.from_user.id]['day'], number=users[callback.from_user.id]['week'], group=users[callback.from_user.id]['group'])}', reply_markup=dzkb)
        elif users[callback.from_user.id]['week'] == 1:
            await callback.message.edit_caption(caption=f'Вот д/з на следующую неделю {main.dz_day(users[callback.from_user.id]['day'], users[callback.from_user.id]['week'])} {main.dz_for_day(day=users[callback.from_user.id]['day'], number=users[callback.from_user.id]['week'], group=users[callback.from_user.id]['group'])}', reply_markup=dzkb)
        else:
            await callback.message.edit_caption(caption=f'Вот д/з прошлой недели {main.dz_day(users[callback.from_user.id]['day'], users[callback.from_user.id]['week'])} {main.dz_for_day(day=users[callback.from_user.id]['day'], number=users[callback.from_user.id]['week'], group=users[callback.from_user.id]['group'])}', reply_markup=dzkb)


@router.callback_query(F.data == '+day')
async def plus_day(callback: CallbackQuery):
    if users[callback.from_user.id]['day'] == 4:
        await callback.answer(text='Вы на последней дне, дальше идти вы не можете 🚫', show_alert=True)
    else:
        if callback.from_user.id == ADMIN_ID:
            dzkb = kb.admin_dz
        else:
            dzkb = kb.dz
        users[callback.from_user.id]['day'] += 1
        await callback.answer()
        if users[callback.from_user.id]['week'] == 0:
            await callback.message.edit_caption(caption=f'Вот д/з на эту неделю {main.dz_day(users[callback.from_user.id]['day'], users[callback.from_user.id]['week'])} {main.dz_for_day(day=users[callback.from_user.id]['day'], number=users[callback.from_user.id]['week'], group=users[callback.from_user.id]['group'])}', reply_markup=dzkb)
        elif users[callback.from_user.id]['week'] == 1:
            await callback.message.edit_caption(caption=f'Вот д/з на следующую неделю {main.dz_day(users[callback.from_user.id]['day'], users[callback.from_user.id]['week'])} {main.dz_for_day(day=users[callback.from_user.id]['day'], number=users[callback.from_user.id]['week'], group=users[callback.from_user.id]['group'])}', reply_markup=dzkb)
        else:
            await callback.message.edit_caption(caption=f'Вот д/з прошлой недели {main.dz_day(users[callback.from_user.id]['day'], users[callback.from_user.id]['week'])} {main.dz_for_day(day=users[callback.from_user.id]['day'], number=users[callback.from_user.id]['week'], group=users[callback.from_user.id]['group'])}', reply_markup=dzkb)


@router.callback_query(F.data == '-day')
async def minus_day(callback: CallbackQuery):
    if users[callback.from_user.id]['day'] == 0:
        await callback.answer(text='Вы на последней дне, дальше идти вы не можете 🚫', show_alert=True)
    else:
        if callback.from_user.id == ADMIN_ID:
            dzkb = kb.admin_dz
        else:
            dzkb = kb.dz
        users[callback.from_user.id]['day'] -= 1
        await callback.answer()
        if users[callback.from_user.id]['week'] == 0:
            await callback.message.edit_caption(caption=f'Вот д/з на эту неделю {main.dz_day(users[callback.from_user.id]['day'], users[callback.from_user.id]['week'])} {main.dz_for_day(day=users[callback.from_user.id]['day'], number=users[callback.from_user.id]['week'], group=users[callback.from_user.id]['group'])}', reply_markup=dzkb)
        elif users[callback.from_user.id]['week'] == 1:
            await callback.message.edit_caption(caption=f'Вот д/з на следующую неделю {main.dz_day(users[callback.from_user.id]['day'], users[callback.from_user.id]['week'])} {main.dz_for_day(day=users[callback.from_user.id]['day'], number=users[callback.from_user.id]['week'], group=users[callback.from_user.id]['group'])}', reply_markup=dzkb)
        else:
            await callback.message.edit_caption(caption=f'Вот д/з прошлой недели {main.dz_day(users[callback.from_user.id]['day'], users[callback.from_user.id]['week'])} {main.dz_for_day(day=users[callback.from_user.id]['day'], number=users[callback.from_user.id]['week'], group=users[callback.from_user.id]['group'])}', reply_markup=dzkb)


@router.callback_query(F.data == 'help')
async def help(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_media(InputMediaPhoto(media=FSInputFile(path='photo2.jpg')))
    await callback.message.edit_caption(caption='Тут все просто,\nУзнаешь дз класса 9E НИШ ФМН Астана 🏫.\nCreator - @Idk_Amir', reply_markup=kb.back_help)


@router.callback_query(F.data == 'back_help')
async def back(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_media(InputMediaPhoto(media=FSInputFile(path='photo1.jpg')))
    await callback.message.edit_caption(caption=f'<b>{callback.from_user.first_name}</b>, можешь посмотреть и узнать домашку 🤓', reply_markup=kb.start, parse_mode='html')
    

@router.callback_query(F.data == 'edit_dz')
async def dz_edit(callback: CallbackQuery):
    await callback.answer()
    day = users[callback.from_user.id]['day']
    number = users[callback.from_user.id]['week']
    group = users[callback.from_user.id]['group']
    subjects = main.subjects_for_day(day, number, group)
    builder = InlineKeyboardBuilder()       
    for subject in subjects:
        builder.row(InlineKeyboardButton(text=subject, callback_data=subject))
    builder.row(InlineKeyboardButton(text='Назад 🔙', callback_data='dz'))
    await callback.message.edit_caption(caption='Выберите предмет:', reply_markup=builder.as_markup())


@router.callback_query(F.data.func(lambda data: ':' in data))
async def select_subject(callback: CallbackQuery):
    await callback.answer()
    users[callback.from_user.id]['subject'] = callback.data
    await callback.message.edit_caption(caption=f'Введите новое значение для {callback.data}', reply_markup=kb.back)


@router.message(F.text)
async def update_dz(message: Message):
    if message.from_user.id == ADMIN_ID:
        new_value = message.text
        day = users[message.from_user.id]['day']
        number = users[message.from_user.id]['week']
        group = users[message.from_user.id]['group']
        subject = users[message.from_user.id]['subject']
        print(users)
        main.edit_dz(day, number, group, subject, new_value)
        await message.answer_photo(photo=FSInputFile(path=f'week-{main.get_week_number() + number}.jpg'), caption=f'Д/з обновлено!✅ ', reply_markup=kb.back)
    else:
        await message.answer_photo(photo=FSInputFile(path='photo1.jpg'), caption=f'<b>{message.from_user.first_name}</b>, я нечего не понял\nЭто бот чтобы узнать домашку 📖✍️', reply_markup=kb.start, parse_mode='html')
