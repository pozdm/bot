import json
import re

import requests

from aiogram import Router, types, F
from aiogram.filters import CommandStart, Command, or_f, StateFilter
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from aiogram.types import ReplyKeyboardRemove

from filters.chat_types import ChatTypeFilter
from utils.keyboards import main_kb
from utils.get_stats_from_api import get_stats_from_api

router = Router()
router.message.filter(ChatTypeFilter(["private"]))


class AddData(StatesGroup):
    category = State()
    start_date = State()
    end_date = State()


@router.message(StateFilter(None), CommandStart())
async def start_cmd(message: types.Message, state: FSMContext):
    await message.answer(
        "Выберите направление по которому хотите получить статистику из списка", reply_markup=main_kb
    )
    await state.set_state(AddData.category)


@router.message(StateFilter("*"), Command("exit"))
async def cancel_handler(message: types.Message, state: FSMContext):
    await state.clear()
    await message.answer(
        "Действия отменены"
    )


@router.message(AddData.category)
@router.message(or_f(F.text.lower() == "users statistics"), (F.text.lower() == "views statistics"),
                (F.text.lower() == "chats statistics"), (F.text.lower() == "utm statistics"),
                (F.text.lower() == "subscribers statistics"), (F.text.lower() == "All statistics"))
async def add_cat(message: types.Message, state: FSMContext):
    await state.update_data(category=message.text)
    await message.answer(
        "Введите дату начала показа статистики в формате: yyyy-mm-dd", reply_markup=ReplyKeyboardRemove()
    )
    await state.set_state(AddData.start_date)


@router.message(AddData.category)
async def add_cat(message: types.Message):
    await message.answer(
        "Введены не корректные данные!"
    )


@router.message(AddData.start_date, F.text.regexp(r"^\d{4}-\d{2}-\d{2}$"))
async def add_start_date(message: types.Message, state: FSMContext):
    await state.update_data(start_date=message.text)
    await message.answer(
        "Введите дату конца показа статистики в формате: yyyy-mm-dd"
    )
    await state.set_state(AddData.end_date)


@router.message(AddData.start_date)
async def add_cat(message: types.Message):
    await message.answer(
        "Введены не корректные данные!"
    )


@router.message(AddData.end_date, F.text.regexp(r"^\d{4}-\d{2}-\d{2}$"))
async def add_end_date(message: types.Message, state: FSMContext):
    await state.update_data(end_date=message.text)
    data = await state.get_data()

    cat = data["category"]
    start_date = data["start_date"]
    end_date = data["end_date"]

    await message.answer(
        get_stats_from_api(cat, start_date, end_date)
    )
    await state.clear()


@router.message(AddData.end_date)
async def add_cat(message: types.Message):
    await message.answer(
        "Введены не корректные данные!"
    )

