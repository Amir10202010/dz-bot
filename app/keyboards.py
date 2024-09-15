from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

back_help = InlineKeyboardMarkup(inline_keyboard = [
    [InlineKeyboardButton(text = 'Назад 🔙', callback_data = 'back_help')]
])

start = InlineKeyboardMarkup(inline_keyboard = [
    [InlineKeyboardButton(text = 'Узнать д/з ✅', callback_data = 'dz')],
    [InlineKeyboardButton(text = 'Подробности ℹ', callback_data = 'help')]
])

dz = InlineKeyboardMarkup(inline_keyboard = [
    [InlineKeyboardButton(text = '1 группа', callback_data = '1'), 
     InlineKeyboardButton(text = '2 группа', callback_data = '2')],
    [InlineKeyboardButton(text = '⬅️', callback_data = '-day'), 
     InlineKeyboardButton(text = '➡️', callback_data = '+day')],
    [InlineKeyboardButton(text = '⏪', callback_data = '-week'),
     InlineKeyboardButton(text = '⏩', callback_data = '+week')],
    [InlineKeyboardButton(text = 'Главная 🏠', callback_data = 'back_help')]
])

admin_dz = InlineKeyboardMarkup(inline_keyboard = [
    [InlineKeyboardButton(text = '1 группа', callback_data = '1'), 
     InlineKeyboardButton(text = '2 группа', callback_data = '2')],
    [InlineKeyboardButton(text = '⬅️', callback_data = '-day'), 
     InlineKeyboardButton(text = '➡️', callback_data = '+day')],
    [InlineKeyboardButton(text = '⏪', callback_data = '-week'),
     InlineKeyboardButton(text = '⏩', callback_data = '+week')],
    [InlineKeyboardButton(text = 'Главная 🏠', callback_data = 'back_help')],
    [InlineKeyboardButton(text = 'Изменить✏️', callback_data = 'edit_dz')]
])

back = InlineKeyboardMarkup(inline_keyboard = [
    [InlineKeyboardButton(text = 'Назад 🔙', callback_data = 'edit_dz')],
    [InlineKeyboardButton(text = 'Главная 🏠', callback_data = 'back_help')]
])
