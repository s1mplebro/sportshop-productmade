# -*- coding: utf-8 -*-
import logging
import requests

from config import *
from states import *
from buttons import *
from custom_filters import *
from utils.utils import *
from utils.db_utils import *
from controllers import *

from bs4 import BeautifulSoup

from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import CallbackQuery, LabeledPrice, PreCheckoutQuery

from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.types.message import ContentType


# Configurate our bot
bot = Bot(token=API_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

    
# Start command handler
@dp.message_handler(commands=['start'], state="*")
async def send_welcome(message: types.Message, state: FSMContext):
    await state.finish()
    is_id_exist  = userController.id_user(message.chat.id)

    if is_id_exist:
        await message.answer(f"<b><em>{message.from_user.full_name}</em>, Выберите язык🇷🇺:  \
                            \n<em>{message.from_user.full_name}</em>, Tilni tanlang🇺🇿:</b>",
                            parse_mode='HTML', reply_markup=languag)

    else:
        userController.add_user(message.chat.id, message.from_user.username)
        await message.answer(f"<b><em>{message.from_user.full_name}</em>, Выберите язык🇷🇺:  \
                            \n<em>{message.from_user.full_name}</em>, Tilni tanlang🇺🇿:</b>",
                            parse_mode='HTML', reply_markup=languag)

        await bot.send_message(admin, f"Внимание  админ! к нам присоединился новый пользователь!\
                                        \n id Пользователя: {message.chat.id}\
                                        \n Его юзернейм @{message.from_user.username} ")

# Simple queries handler
@dp.message_handler(IsSimpleQueryFilter(), state="*")
async def simple_query_respond(message: types.Message, state: FSMContext):
    await state.finish()
    respond, keyboard = simple_queries_templates[message.text]

    await message.answer(respond.replace("$USERNAME", message.from_user.full_name),
     parse_mode="HTML", reply_markup=keyboard, disable_web_page_preview=True)


@dp.message_handler(text="✍️ Оставить отзыв", state=None)
async def get_user_reply(message: types.Message):
    await Reply.username.set()
    await message.answer('<b>Здраствуйте, введите свое имя:</b>', parse_mode='HTML', reply_markup=cancel_keyboard)
    
@dp.message_handler(lambda message: message.text != "✍️ Оставить отзыв", state=Reply.username)
async def set_username(message: types.Message, state: FSMContext):
    await get_changed_state(state, message, "username")
    await Reply.next()
    await message.reply('<b>Введите текст отзыва:  </b>', parse_mode='HTML')

@dp.message_handler(lambda message: message.text != "✍️ Оставить отзыв", state=Reply.user_reply)
async def set_user_reply(message: types.Message, state: FSMContext):
    state_data = await get_changed_state(state, message, "user_reply")
    await state.finish()
    await message.answer('Спасибо за отзыв. Администраторы сразу с вами свяжутся.', reply_markup=menu_ru)
    await bot.send_message(admin, f"Пользователь: @{message.from_user.username}\nОтзыв:\
                                \nИмя: {state_data['username']}\nТекст: {state_data['user_reply']} ")
        

@dp.message_handler(text="🛒 Начать новый заказ", state=None)
async def echo(message: types.Message):
    cartController.del_final(message.chat.id)
    await Location.geo.set()
    await message.answer('<b>Для выполнения заказа отправьте местоположение.</b>', parse_mode='HTML', reply_markup=loc)

@dp.message_handler(content_types=['location'],state=Location.geo)
async def load_photo(message: types.Message, state:FSMContext):
    async with state.proxy() as data:
        data['latit'] = float(message.location.latitude)
        data['long'] = float(message.location.longitude)
    await message.answer("""<b>https://sportshopin.uz/</b>""",parse_mode='HTML',reply_markup=menu_ru)
    await message.answer_photo(
        photo = open('img/menu.jpg','rb'),
        caption = """  """,parse_mode='HTML',reply_markup = tovari)

    
    userController.location_update(message.chat.id,data['latit'],data['long'])
    z = userController.sendto_admin(message.chat.id)
    await bot.send_message(admin,f"Зарегистрировался пользователь.  \n Chat id:  {z[0]} \n Username: @{z[1]} ")
    a = float(z[3])
    b = float(z[4])
    await bot.send_location(admin,latitude=a, longitude=b)
    await state.finish()
    

async  def test(url,call,rm):
    url = url
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    section = soup.find_all("div", class_="card-page__top")
    for  products in  section:
        search = products.find('button', class_='shop-product-btn type-3 buy')
        if search is  None:
            await call.message.answer('Извините, данного товара временно нету в наличии')
        else:
            product_name  =  products.find("div", class_="gr-product-name").get_text(strip=True)
            product_price  =  products.find("div", class_="price-current").get_text(strip=True)
            product_photo = products.select('div.card-slider__image a')
            links = [item['href'] for item in product_photo]
            photo  = links[0]
            product_info  =  products.find("div", class_="gr-product-anonce").get_text(strip=True)
            await call.message.answer(f"""  https://sportshopin.uz/{photo}\n \n<b>{product_name}</b> \n \n <em>{product_info}</em> \n \n  <b>{product_price}</b>""",parse_mode='HTML',reply_markup=rm)  

@dp.callback_query_handler(text="optm_nutrition")
async def menu_tanlash(call:CallbackQuery):
    await test(f"https://sportshopin.uz/magazin/product/protein-protein-power",call,protein_korzina())


@dp.callback_query_handler(text="jir")
async def menu_tanlash(call:CallbackQuery):
     await call.message.answer_photo(
        photo = open('img/protein.jpg','rb'),
        caption = """<strong>  Купить жиросжигатели💪 в Ташкенте | Узбекистане🇺🇿  </strong>""",parse_mode='HTML',reply_markup = its_jir)

@dp.callback_query_handler(text="back_to_jir")
async def menu_tanlash(call:CallbackQuery):
     await call.message.answer_photo(
        photo = open('img/protein.jpg','rb'),
        caption = """<strong>  Купить жиросжигатели💪 в Ташкенте | Узбекистане🇺🇿  </strong>""",parse_mode='HTML',reply_markup = its_jir)

@dp.callback_query_handler(text="mor_jir")
async def menu_tanlash(call:CallbackQuery):
     await call.message.answer_photo(
        photo = open('img/protein.jpg','rb'),
        caption = """<strong>  Купить жиросжигатели💪 в Ташкенте | Узбекистане🇺🇿  </strong>""",parse_mode='HTML',reply_markup = jirrr)

@dp.callback_query_handler(text="protein")
async def menu_tanlash(call:CallbackQuery):
     await call.message.answer_photo(
        photo = open('img/protein.jpg','rb'),
        caption = """<strong>  Купить протеины💪 в Ташкенте | Узбекистане🇺🇿  </strong>""",parse_mode='HTML',reply_markup = proteins)

@dp.callback_query_handler(text="kreatin")
async def menu_tanlash(call:CallbackQuery):
     await call.message.answer_photo(
        photo = open('img/protein.jpg','rb'),
        caption = """<strong>  Купить креатин💪 в Ташкенте | Узбекистане🇺🇿  </strong>""",parse_mode='HTML',reply_markup = kre)

@dp.callback_query_handler(text="mor_creatin")
async def menu_tanlash(call:CallbackQuery):
     await call.message.answer_photo(
        photo = open('img/protein.jpg','rb'),
        caption = """<strong>  Купить креатин💪 в Ташкенте | Узбекистане🇺🇿  </strong>""",parse_mode='HTML',reply_markup = mor_creatine)

@dp.callback_query_handler(text="energetic")
async def menu_tanlash(call:CallbackQuery):
     await call.message.answer_photo(
        photo = open('img/protein.jpg','rb'),
        caption = """<strong>  Купить энергетики💪 в Ташкенте | Узбекистане🇺🇿  </strong>""",parse_mode='HTML',reply_markup = energeticss)

@dp.callback_query_handler(text="buster")
async def menu_tanlash(call:CallbackQuery):
     await call.message.answer_photo(
        photo = open('img/protein.jpg','rb'),
        caption = """<strong>  Купить Бустер/Тестостерон💪 в Ташкенте | Узбекистане🇺🇿  </strong>""",parse_mode='HTML',reply_markup = buster_testt)

@dp.callback_query_handler(text="mor_testeoron")
async def menu_tanlash(call:CallbackQuery):
     await call.message.answer_photo(
        photo = open('img/protein.jpg','rb'),
        caption = """<strong>  Купить Бустер/Тестостерон💪 в Ташкенте | Узбекистане🇺🇿  </strong>""",parse_mode='HTML',reply_markup = mor_testoon)


@dp.callback_query_handler(text="back_to_main")
async def menu_tanlash(call:CallbackQuery):
    await call.message.answer("""<b>https://sportshopin.uz/</b>""",parse_mode='HTML',reply_markup=menu_ru)
    await call.message.answer_photo(
        photo = open('img/menu.jpg','rb'),
        caption = """  """,parse_mode='HTML',reply_markup = tovari)

@dp.callback_query_handler(text="prostar1")
async def menu_tanlash(call:CallbackQuery):
    await test("https://sportshopin.uz/magazin/product/syvorotochnyy-protein-diet-protein",call,protein_korzina2())
   
@dp.callback_query_handler(text="wheygold")
async def menu_tanlash(call:CallbackQuery):
    await test("https://sportshopin.uz/magazin/product/proteinovyye-batonchiki-13-protein-bar",call,protein_korzina3())


@dp.callback_query_handler(text="wheygold-1")
async def menu_tanlash(call:CallbackQuery):
    await test("https://sportshopin.uz/magazin/product/100-whey-gold-standard",call,protein_korzina4())

@dp.callback_query_handler(text="atlant")
async def menu_tanlash(call:CallbackQuery):
    await test("https://sportshopin.uz/magazin/product/kazein-100-casein-gold-standard-ot-optimum-nutrition",call,protein_korzina5())


@dp.callback_query_handler(text="bigwhey")
async def menu_tanlash(call:CallbackQuery):
    await test("https://sportshopin.uz/magazin/product/atlant",call,protein_korzina6())


@dp.callback_query_handler(text="carnivor")
async def menu_tanlash(call:CallbackQuery):
    await test("https://sportshopin.uz/magazin/product/atlant-s-kreatinom",call,protein_korzina7())

@dp.callback_query_handler(text="wheyhd")
async def menu_tanlash(call:CallbackQuery):
    await test("https://sportshopin.uz/magazin/product/big-whey",call,protein_korzina8())


@dp.callback_query_handler(text="kevin")
async def menu_tanlash(call:CallbackQuery):
    await test("https://sportshopin.uz/magazin/product/protein-carnivor-ot-musclemeds",call,protein_korzina9())


@dp.callback_query_handler(text="casein")
async def menu_tanlash(call:CallbackQuery):
    await test("https://sportshopin.uz/magazin/product/pure-whey-100-be-perfect-nutrition",call,protein_korzina10())


@dp.callback_query_handler(text="wheyprotein")
async def menu_tanlash(call:CallbackQuery):
    await test("https://sportshopin.uz/magazin/product/whey-hd-ot-bpi-sports",call,protein_korzina11())


@dp.callback_query_handler(text="prostar")
async def menu_tanlash(call:CallbackQuery):
    await test("https://sportshopin.uz/magazin/product/rule-1-whey-blend-chocolate-fudge-68-servings",call,protein_korzina12())


@dp.callback_query_handler(text="prostarkg")
async def menu_tanlash(call:CallbackQuery):
    await test("https://sportshopin.uz/magazin/product/levro-iso-whey-2-kg",call,protein_korzina13())

@dp.callback_query_handler(text="sensation")
async def menu_tanlash(call:CallbackQuery):
    await test("https://sportshopin.uz/magazin/product/r1-rule-one-protein-whey-blend-4-5-kg",call,protein_korzina14())


@dp.callback_query_handler(text="sensationkg")
async def menu_tanlash(call:CallbackQuery):
    await test("https://sportshopin.uz/magazin/product/r1-casein-rule-1",call,protein_korzina15())

@dp.callback_query_handler(text="monsterlabs")
async def menu_tanlash(call:CallbackQuery):
    await test("https://sportshopin.uz/magazin/product/gat-whey-protein",call,protein_korzina16())

@dp.callback_query_handler(text="sticker")
async def menu_tanlash(call:CallbackQuery):
    await test("https://sportshopin.uz/magazin/product/prostar-100-whey-protein-907g-ot-ultimate-nutrition",call,protein_korzina17())

@dp.callback_query_handler(text="superioriso")
async def menu_tanlash(call:CallbackQuery):
    await test("https://sportshopin.uz/magazin/product/superior-14-whey-isolate-iso-pro-2-2kg",call,protein_korzina18())

@dp.callback_query_handler(text="superiorqua")
async def menu_tanlash(call:CallbackQuery):
    await test("https://sportshopin.uz/magazin/product/superior-14-superior-quattro-protein-3000-g",call,protein_korzina19())

@dp.callback_query_handler(text="tesla")
async def menu_tanlash(call:CallbackQuery):
    await test("https://sportshopin.uz/magazin/product/iso-sensation-93-ot-ultimate-nutrition",call,protein_korzina20())

@dp.callback_query_handler(text="teslaiso")
async def menu_tanlash(call:CallbackQuery):
    await test("https://sportshopin.uz/magazin/product/iso-sensation-93-ot-ultimate-nutrition-1",call,protein_korzina21())


@dp.callback_query_handler(text="labsmon")
async def menu_tanlash(call:CallbackQuery):
    await test("https://sportshopin.uz/magazin/product/monster-labs-whey",call,protein_korzina22())

@dp.callback_query_handler(text="syntha6")
async def menu_tanlash(call:CallbackQuery):
    await test("https://sportshopin.uz/magazin/product/protein-syntha-6",call,protein_korzina23())

@dp.callback_query_handler(text="whey_pole")
async def menu_tanlash(call:CallbackQuery):
    await test("https://sportshopin.uz/magazin/product/whey-protein-ot-pole-nutrition",call,protein_korzina24())

@dp.callback_query_handler(text="gold_standard")
async def menu_tanlash(call:CallbackQuery):
    await test("https://sportshopin.uz/magazin/product/swhey-gold-standard-100-so-stikerom",call,protein_korzina25())

@dp.callback_query_handler(text="vegan")
async def menu_tanlash(call:CallbackQuery):
    await test("https://sportshopin.uz/magazin/product/vegan-protein-v-tashkente-rastitelnyj-gorohovyj-protein",call,protein_korzina26())

@dp.callback_query_handler(text="whey_core")
async def menu_tanlash(call:CallbackQuery):
    await test("https://sportshopin.uz/magazin/product/syvorotochnyj-protein-superior-14-whey-core-protein",call,protein_korzina27())

@dp.callback_query_handler(text="tesla_whey_charger")
async def menu_tanlash(call:CallbackQuery):
    await test("https://sportshopin.uz/magazin/product/tesla-whey-charger-100",call,protein_korzina28())

@dp.callback_query_handler(text="tesla_nutrition")
async def menu_tanlash(call:CallbackQuery):
    await test("https://sportshopin.uz/magazin/product/tesla-nutrition-iso-zero-100",call,protein_korzina29())

@dp.callback_query_handler(text="hydro_whey")
async def menu_tanlash(call:CallbackQuery):
    await test("https://sportshopin.uz/magazin/product/superior-14-hydro-whey-zero",call,protein_korzina30())

@dp.callback_query_handler(text="iso_tesla")
async def menu_tanlash(call:CallbackQuery):
    await test("https://sportshopin.uz/magazin/product/iso-zero-100-tesla-nutrition",call,protein_korzina31())

@dp.callback_query_handler(text="rule_plant")
async def menu_tanlash(call:CallbackQuery):
    await test("https://sportshopin.uz/magazin/product/veganskij-protein-ot-rule1-plant-protein-1-26kg",call,protein_korzina32())


@dp.callback_query_handler(text="protein_rule1")
async def menu_tanlash(call:CallbackQuery):
    await test("https://sportshopin.uz/magazin/product/syvorotochnyj-protein-izolyat-r1-protein-2-2kg",call,protein_korzina33())

@dp.callback_query_handler(text="xtendpro")
async def menu_tanlash(call:CallbackQuery):
    await test("https://sportshopin.uz/magazin/product/xtend-pro-whey-isolate-826g",call,protein_korzina34())

@dp.callback_query_handler(text="dymanize")
async def menu_tanlash(call:CallbackQuery):
    await test("https://sportshopin.uz/magazin/product/iso-100",call,protein_korzina35())

@dp.callback_query_handler(text="xtendwhey")
async def menu_tanlash(call:CallbackQuery):
    await test("https://sportshopin.uz/magazin/product/xtend-pro-whey-isolate",call,protein_korzina36())

@dp.callback_query_handler(text="nitro_tech")
async def menu_tanlash(call:CallbackQuery):
    await test("https://sportshopin.uz/magazin/product/nitro-tech-whey-gold",call,protein_korzina37())


@dp.callback_query_handler(text="combat_whey")
async def menu_tanlash(call:CallbackQuery):
    await test("https://sportshopin.uz/magazin/product/combat-100-whey",call,protein_korzina38())

@dp.callback_query_handler(text="elite")
async def menu_tanlash(call:CallbackQuery):
    await test("https://sportshopin.uz/magazin/product/elite-whey-protein",call,protein_korzina39())

@dp.callback_query_handler(text="ultra")
async def menu_tanlash(call:CallbackQuery):
    await test("https://sportshopin.uz/magazin/product/ultra-whey-pro",call,protein_korzina40())

@dp.callback_query_handler(text="mutant")
async def menu_tanlash(call:CallbackQuery):
    await test("https://sportshopin.uz/magazin/product/mutant-whey-protein",call,protein_korzina41())


@dp.callback_query_handler(text="elite_casein")
async def menu_tanlash(call:CallbackQuery):
    await test("https://sportshopin.uz/magazin/product/elite-casein-ot-dymatize",call,protein_korzina42())


@dp.callback_query_handler(text="combat_powder")
async def menu_tanlash(call:CallbackQuery):
    await test("https://sportshopin.uz/magazin/product/combat-protein-powder",call,protein_korzina43())


@dp.callback_query_handler(text="nitro_gold")
async def menu_tanlash(call:CallbackQuery):
    await test("https://sportshopin.uz/magazin/product/nitro-tech-casein-gold",call,protein_korzina44())

@dp.callback_query_handler(text="bombbar")
async def menu_tanlash(call:CallbackQuery):
    await test("https://sportshopin.uz/magazin/product/protein-bombbar-whey-protein-30-g",call,protein_korzina45())

@dp.callback_query_handler(text="badass")
async def menu_tanlash(call:CallbackQuery):
    await test("https://sportshopin.uz/magazin/product/badass-nutrition-whey-protein-2270-g",call,protein_korzina46())


@dp.callback_query_handler(text="levrone")
async def menu_tanlash(call:CallbackQuery):
    await test("https://sportshopin.uz/magazin/product/kevin-levrone-gold-whey-2000-gr",call,protein_korzina47())

@dp.callback_query_handler(text="slow-rel")
async def menu_tanlash(call:CallbackQuery):
    await test("https://sportshopin.uz/magazin/product/slow-release-casein",call,protein_korzina48())

@dp.callback_query_handler(text="viking")
async def menu_tanlash(call:CallbackQuery):
    await test("https://sportshopin.uz/magazin/product/viking-empire-whey",call,protein_korzina49())


@dp.callback_query_handler(text="fitness")
async def menu_tanlash(call:CallbackQuery):
    await test("https://sportshopin.uz/magazin/product/protein-fitness-authority-core-pro",call,protein_korzina50())

@dp.callback_query_handler(text="kevin_anabolic")
async def menu_tanlash(call:CallbackQuery):
    await test("https://sportshopin.uz/magazin/product/protein-kevin-levrone-anabolic-iso-whey",call,protein_korzina51())

@dp.callback_query_handler(text="impact")
async def menu_tanlash(call:CallbackQuery):
    await test("https://sportshopin.uz/magazin/product/impact-whey-protein-ot-myproyein",call,protein_korzina52())

@dp.callback_query_handler(text="hydra_tesla")
async def menu_tanlash(call:CallbackQuery):
    await test("https://sportshopin.uz/magazin/product/syvorotochnyj-protein-gidrolizat-tesla-hydro-whey-zero",call,protein_korzina53())

@dp.callback_query_handler(text="appe")
async def menu_tanlash(call:CallbackQuery):
    await test("https://sportshopin.uz/magazin/product/ape-shit-cutz",call,jirfire1())

@dp.callback_query_handler(text="asi")
async def menu_tanlash(call:CallbackQuery):
    await test("https://sportshopin.uz/magazin/product/asia-black-25",call,jirfire2())

@dp.callback_query_handler(text="pauk")
async def menu_tanlash(call:CallbackQuery):
    await test("https://sportshopin.uz/magazin/product/zhiroszhigatel-define-it-lady",call,jirfire3())

@dp.callback_query_handler(text="widow")
async def menu_tanlash(call:CallbackQuery):
    await test("https://sportshopin.uz/magazin/product/black-widow-25-zhiroszhigatel-ot-hi-tech-pharmaceuticals",call,jirfire4())

@dp.callback_query_handler(text="keto")
async def menu_tanlash(call:CallbackQuery):
    await test("https://sportshopin.uz/magazin/product/burn-on-keto-60-caps",call,jirfire5())

@dp.callback_query_handler(text="cell")
async def menu_tanlash(call:CallbackQuery):
    await test("https://sportshopin.uz/magazin/product/cellucor-super-hd",call,jirfire6())

@dp.callback_query_handler(text="china")
async def menu_tanlash(call:CallbackQuery):
    await test("https://sportshopin.uz/magazin/product/china-white",call,jirfire7())

@dp.callback_query_handler(text="cla1250")
async def menu_tanlash(call:CallbackQuery):
    await test("https://sportshopin.uz/magazin/product/cla-1250",call,jirfire8())

@dp.callback_query_handler(text="cla_rsp")
async def menu_tanlash(call:CallbackQuery):
    await test("https://sportshopin.uz/magazin/product/cla-ot-rsp-nutrition",call,jirfire9())
@dp.callback_query_handler(text="guggul")
async def menu_tanlash(call:CallbackQuery):
    await test("https://sportshopin.uz/magazin/product/guggul-ultimate-nutrition",call,jirfire10())

@dp.callback_query_handler(text="leanmode")
async def menu_tanlash(call:CallbackQuery):
    await test("https://sportshopin.uz/magazin/product/lean-mode",call,jirfire11())

@dp.callback_query_handler(text="leanfire")
async def menu_tanlash(call:CallbackQuery):
    await test("https://sportshopin.uz/magazin/product/leanlfire-moshchnejshij-termogennyj-zhiroszhigatel",call,jirfire12())

@dp.callback_query_handler(text="nutrex")
async def menu_tanlash(call:CallbackQuery):
    await test("https://sportshopin.uz/magazin/product/lipo-6-black-maximum",call,jirfire13())

@dp.callback_query_handler(text="black_hers")
async def menu_tanlash(call:CallbackQuery):
    await test("https://sportshopin.uz/magazin/product/lipo-6-black-hers",call,jirfire14())

@dp.callback_query_handler(text="methyldrene")
async def menu_tanlash(call:CallbackQuery):
    await test("https://sportshopin.uz/magazin/product/termogenik-lipo-6-black-hers-us",call,jirfire15())

@dp.callback_query_handler(text="pure_cla")
async def menu_tanlash(call:CallbackQuery):
    await test("https://sportshopin.uz/magazin/product/platinum-pure-cla",call,jirfire16())

@dp.callback_query_handler(text="roxylean")
async def menu_tanlash(call:CallbackQuery):
    await test("https://sportshopin.uz/magazin/product/roxylean-60-caps",call,jirfire17())

@dp.callback_query_handler(text="animals_curs")
async def menu_tanlash(call:CallbackQuery):
    await test("https://sportshopin.uz/magazin/product/animal-cuts",call,jirfire18())

@dp.callback_query_handler(text="black_mamba")
async def menu_tanlash(call:CallbackQuery):
    await test("https://sportshopin.uz/magazin/product/black-mamba",call,jirfire19())

@dp.callback_query_handler(text="cla_pure_1000")
async def menu_tanlash(call:CallbackQuery):
    await test("https://sportshopin.uz/magazin/product/cla-pure-1000",call,jirfire20())

@dp.callback_query_handler(text="fat_burner")
async def menu_tanlash(call:CallbackQuery):
    await test("https://sportshopin.uz/magazin/product/fat-burner-daily",call,jirfire21())

@dp.callback_query_handler(text="hell_fire")
async def menu_tanlash(call:CallbackQuery):
    await test("https://sportshopin.uz/magazin/product/hell-fire",call,jirfire22())

@dp.callback_query_handler(text="hydroxycut")
async def menu_tanlash(call:CallbackQuery):
    await test("https://sportshopin.uz/magazin/product/hydroxycut-black",call,jirfire23())

@dp.callback_query_handler(text="hardcor_elite")
async def menu_tanlash(call:CallbackQuery):
    await test("https://sportshopin.uz/magazin/product/hydroxycut-hardcore-elite",call,jirfire24())

@dp.callback_query_handler(text="next_gen")
async def menu_tanlash(call:CallbackQuery):
    await test("https://sportshopin.uz/magazin/product/hydroxycut-hardcore-next-gen",call,jirfire25())

@dp.callback_query_handler(text="max_forwomen")
async def menu_tanlash(call:CallbackQuery):
    await test("https://sportshopin.uz/magazin/product/hydroxycut-max-for-women",call,jirfire26())

@dp.callback_query_handler(text="hydro_platinum")
async def menu_tanlash(call:CallbackQuery):
    await test("https://sportshopin.uz/magazin/product/hydroxycut-platinum",call,jirfire27())

@dp.callback_query_handler(text="jetful_super")
async def menu_tanlash(call:CallbackQuery):
    await test("https://sportshopin.uz/magazin/product/jetfuel-superburn",call,jirfire28())

@dp.callback_query_handler(text="ketto_elite")
async def menu_tanlash(call:CallbackQuery):
    await test("https://sportshopin.uz/magazin/product/keto-elite",call,jirfire29())

@dp.callback_query_handler(text="keto_karma")
async def menu_tanlash(call:CallbackQuery):
    await test("https://sportshopin.uz/magazin/product/irwin-naturals-keto-karma-burn-fat-red",call,jirfire30())

@dp.callback_query_handler(text="lipo_natural")
async def menu_tanlash(call:CallbackQuery):
    await test("https://sportshopin.uz/magazin/product/lipo-6-natural",call,jirfire31())

@dp.callback_query_handler(text="nutrex_lipo6")
async def menu_tanlash(call:CallbackQuery):
    await test("https://sportshopin.uz/magazin/product/lipo-6-rx-60-cap",call,jirfire32())

@dp.callback_query_handler(text="fat_burner_plus")
async def menu_tanlash(call:CallbackQuery):
    await test("https://sportshopin.uz/magazin/product/mason-natural-fat-burner-plus-super-citrimax-60-tablets",call,jirfire33())

@dp.callback_query_handler(text="weight_control")
async def menu_tanlash(call:CallbackQuery):
    await test("https://sportshopin.uz/magazin/product/metabolism-weight-control",call,jirfire34())

@dp.callback_query_handler(text="nobii")
async def menu_tanlash(call:CallbackQuery):
    await test("https://sportshopin.uz/magazin/product/nobi-nutrition-premium-womens-fat-burner-60-cap",call,jirfire35())

@dp.callback_query_handler(text="rapiducuts")
async def menu_tanlash(call:CallbackQuery):
    await test("https://sportshopin.uz/magazin/product/termogenik-slim-core",call,jirfire36())

@dp.callback_query_handler(text="ripped_fast")
async def menu_tanlash(call:CallbackQuery):
    await test("https://sportshopin.uz/magazin/product/ripped-fast",call,jirfire37())

@dp.callback_query_handler(text="terra_origgin")
async def menu_tanlash(call:CallbackQuery):
    await test("https://sportshopin.uz/magazin/product/terra-origin-terra-origin-healthy-fat-burner-60-caps",call,jirfire38())

@dp.callback_query_handler(text="the_omen")
async def menu_tanlash(call:CallbackQuery):
    await test("https://sportshopin.uz/magazin/product/the-omen",call,jirfire39())

@dp.callback_query_handler(text="hyper_mass_prof")
async def menu_tanlash(call:CallbackQuery):
    await test("https://sportshopin.uz/magazin/product/14-superior-hyper-mass-professional",call,geynerr1())

@dp.callback_query_handler(text="superoir_mass_prof")
async def menu_tanlash(call:CallbackQuery):
    await test("https://sportshopin.uz/magazin/product/14-superior-superior-mass-professional",call,geynerr2())

@dp.callback_query_handler(text="Applied_Critical")
async def menu_tanlash(call:CallbackQuery):
    await test("https://sportshopin.uz/magazin/product/applied-critical-mass-original-6kg",call,geynerr3())

@dp.callback_query_handler(text="big_mass_big_man")
async def menu_tanlash(call:CallbackQuery):
    await test("https://sportshopin.uz/magazin/product/big-mass-gejner",call,geynerr4())

@dp.callback_query_handler(text="Carbs_Pro_Matrix")
async def menu_tanlash(call:CallbackQuery):
    await test("https://sportshopin.uz/magazin/product/carbs-pro-matrix-sbalansirovannaya-uglevodnaya-dobavka",call,geynerr5())

@dp.callback_query_handler(text="Kevin_Levrone_Anabolic_Mass")
async def menu_tanlash(call:CallbackQuery):
    await test("https://sportshopin.uz/magazin/product/kevin-levrone-anabolic-mass",call,geynerr6())

@dp.callback_query_handler(text="megamass400weider")
async def menu_tanlash(call:CallbackQuery):
    await test("https://sportshopin.uz/magazin/product/vysokokaloriynyye-geynery-mass-builder",call,geynerr7())

@dp.callback_query_handler(text="Monster_Lab_Real_Mass_Gainer")
async def menu_tanlash(call:CallbackQuery):
    await test("https://sportshopin.uz/magazin/product/monster-lab-real-mass-gainer",call,geynerr8())

@dp.callback_query_handler(text="PLATINUM_MASS_14_Superior")
async def menu_tanlash(call:CallbackQuery):
    await test("https://sportshopin.uz/magazin/product/platinum-mass-14-superior",call,geynerr9())

@dp.callback_query_handler(text="r1_gainer_lbs")
async def menu_tanlash(call:CallbackQuery):
    await test("https://sportshopin.uz/magazin/product/r1-gainer-lbs-2-75-kg",call,geynerr10())

@dp.callback_query_handler(text="rule1_r1_54")
async def menu_tanlash(call:CallbackQuery):
    await test("https://sportshopin.uz/magazin/product/rule-1-r1-prevoshodnyj-gejner",call,geynerr11())

@dp.callback_query_handler(text="serious_mass_optimuim")
async def menu_tanlash(call:CallbackQuery):
    await test("https://sportshopin.uz/magazin/product/serios-mass",call,geynerr12())

@dp.callback_query_handler(text="serious_mass_1250")
async def menu_tanlash(call:CallbackQuery):
    await test("https://sportshopin.uz/magazin/product/serious-mass",call,geynerr13())

@dp.callback_query_handler(text="Super_Mass_Gainer")
async def menu_tanlash(call:CallbackQuery):
    await test("https://sportshopin.uz/magazin/product/super-mass-gainer-ot-dymatize",call,geynerr14())

@dp.callback_query_handler(text="Superior_14_Platinum_Mass")
async def menu_tanlash(call:CallbackQuery):
    await test("https://sportshopin.uz/magazin/product/superior-14-platinum-mass",call,geynerr15())

@dp.callback_query_handler(text="True_Mass_1200")
async def menu_tanlash(call:CallbackQuery):
    await test("https://sportshopin.uz/magazin/product/sbalansirovannyye-geynery-true-mass",call,geynerr16())

@dp.callback_query_handler(text="Up_Your_Mass_1200")
async def menu_tanlash(call:CallbackQuery):
    await test("https://sportshopin.uz/magazin/product/up-your-mass-1200",call,geynerr17())

@dp.callback_query_handler(text="MassTechExtreme2000")
async def menu_tanlash(call:CallbackQuery):
    await test("https://sportshopin.uz/magazin/product/vysokokaloriynyye-geynery-mass",call,geynerr18())

@dp.callback_query_handler(text="hyper_gain")
async def menu_tanlash(call:CallbackQuery):
    await test("https://sportshopin.uz/magazin/product/gejner-hyper-gain-1",call,geynerr19())

@dp.callback_query_handler(text="mutant_mass_68kg")
async def menu_tanlash(call:CallbackQuery):
    await test("https://sportshopin.uz/magazin/product/gejner-mutant-mass-6-8-kg",call,geynerr20())

@dp.callback_query_handler(text="Myprotein_Impact_Weight_Gainer")
async def menu_tanlash(call:CallbackQuery):
    await test("https://sportshopin.uz/magazin/product/gejner-myprotein-impact-weight-gainer",call,geynerr21())

@dp.callback_query_handler(text="Anabolic_Mass")
async def menu_tanlash(call:CallbackQuery):
    await test("https://sportshopin.uz/magazin/product/anabolic-mass-premium-gejner-dlya-nabora-massy",call,geynerr22())

@dp.callback_query_handler(text="ATLETHARDMASS")
async def menu_tanlash(call:CallbackQuery):
    await test("https://sportshopin.uz/magazin/product/atlet-hard-mass",call,geynerr23())

@dp.callback_query_handler(text="bulk_muscle_bpisports")
async def menu_tanlash(call:CallbackQuery):
    await test("https://sportshopin.uz/magazin/product/bulk-muscle-ot-bpi-sports-6-8-kg",call,geynerr24())

@dp.callback_query_handler(text="Carnivor_Mass_MuscleMeds")
async def menu_tanlash(call:CallbackQuery):
    await test("https://sportshopin.uz/magazin/product/carnivor-mass-ot-musclemeds-massa-v-predelno-korotkie-sroki",call,geynerr25())

@dp.callback_query_handler(text="Gain_Fast_Universal_Nutrition")
async def menu_tanlash(call:CallbackQuery):
    await test("https://sportshopin.uz/magazin/product/gain-fast-ot-universal-nutrition",call,geynerr26())

@dp.callback_query_handler(text="HardcoreMassPhase")
async def menu_tanlash(call:CallbackQuery):
    await test("https://sportshopin.uz/magazin/product/hardcore-mass-phase",call,geynerr27())

@dp.callback_query_handler(text="pzds_slojniy_cbl")
async def menu_tanlash(call:CallbackQuery):
    await test("https://sportshopin.uz/magazin/product/healthxp-essential-series-weight-gainers-mass-gainers-5kg-chocolate",call,geynerr28())

@dp.callback_query_handler(text="HyperBolicMass")
async def menu_tanlash(call:CallbackQuery):
    await test("https://sportshopin.uz/magazin/product/hyperbolic-mass-gh-usn",call,geynerr29())

@dp.callback_query_handler(text="kevin_radnoy_geyner_7kg")
async def menu_tanlash(call:CallbackQuery):
    await test("https://sportshopin.uz/magazin/product/kevin-levrone-anabolic-mass-7-kg",call,geynerr30())

@dp.callback_query_handler(text="yMASSKEVINLEVRONE")
async def menu_tanlash(call:CallbackQuery):
    await test("https://sportshopin.uz/magazin/product/levro-legendary-mass-ot-kevin-levro",call,geynerr31())

@dp.callback_query_handler(text="kevin_levrone_legen_mass68")
async def menu_tanlash(call:CallbackQuery):
    await test("https://sportshopin.uz/magazin/product/kevin-levrone-legendary-mass-6800-gr",call,geynerr32())

@dp.callback_query_handler(text="MassGainerGeneticlab")
async def menu_tanlash(call:CallbackQuery):
    await test("https://sportshopin.uz/magazin/product/mass-gainer-geneticlab-nutrition",call,geynerr33())

@dp.callback_query_handler(text="muscle_mathchgeinre")
async def menu_tanlash(call:CallbackQuery):
    await test("https://sportshopin.uz/magazin/product/mass-gainer-muscle-tech",call,geynerr34())

@dp.callback_query_handler(text="MASSINFUSION")
async def menu_tanlash(call:CallbackQuery):
    await test("https://sportshopin.uz/magazin/product/mass-infusion",call,geynerr35())

@dp.callback_query_handler(text="muscle_juice_revolution")
async def menu_tanlash(call:CallbackQuery):
    await test("https://sportshopin.uz/magazin/product/muscle-juice-revolution-2600",call,geynerr36())

@dp.callback_query_handler(text="combat_xlmass_gainer")
async def menu_tanlash(call:CallbackQuery):
    await test("https://sportshopin.uz/magazin/product/vysokokaloriynyye-geynery-serious-mass",call,geynerr37())

@dp.callback_query_handler(text="mutant_mass_227")
async def menu_tanlash(call:CallbackQuery):
    await test("https://sportshopin.uz/magazin/product/mutant-mass-2-27kg",call,geynerr38())

@dp.callback_query_handler(text="special_mass_geiner")
async def menu_tanlash(call:CallbackQuery):
    await test("https://sportshopin.uz/magazin/product/special-mass-gainer-maxler",call,geynerr39())


@dp.callback_query_handler(text="Creatine_Monohydrate")
async def menu_tanlash(call:CallbackQuery):
    await test("https://sportshopin.uz/magazin/product/100-creatine-monohydrate",call,creat1())

@dp.callback_query_handler(text="Chargedcreatinerule1")
async def menu_tanlash(call:CallbackQuery):
    await test("https://sportshopin.uz/magazin/product/charged-creatine-rule-1",call,creat2())

@dp.callback_query_handler(text="Creatine120serv")
async def menu_tanlash(call:CallbackQuery):
    await test("https://sportshopin.uz/magazin/product/creatine-120-serv-optimum-nutrition",call,creat3())

@dp.callback_query_handler(text="Creatine60servOptimum")
async def menu_tanlash(call:CallbackQuery):
    await test("https://sportshopin.uz/magazin/product/creatine-on",call,creat4())

@dp.callback_query_handler(text="CreatineMicronizedDymatize")
async def menu_tanlash(call:CallbackQuery):
    await test("https://sportshopin.uz/magazin/product/creatine-micronized-ot-dymatize",call,creat5())

@dp.callback_query_handler(text="CreatineMonohydratepowder")
async def menu_tanlash(call:CallbackQuery):
    await test("https://sportshopin.uz/magazin/product/creatine-monohydrate-powder-300g",call,creat6())

@dp.callback_query_handler(text="creatine_crea_badass")
async def menu_tanlash(call:CallbackQuery):
    await test("https://sportshopin.uz/magazin/product/creatine-crea-bad-ass-300g",call,creat7())
    
@dp.callback_query_handler(text="Muscle_techcell272")
async def menu_tanlash(call:CallbackQuery):
    await test("https://sportshopin.uz/magazin/product/muscle-tech-kreatin-cell-tech-2-72kg",call,creat8())

@dp.callback_query_handler(text="pole_nutrition_creas_mono")
async def menu_tanlash(call:CallbackQuery):
    await test("https://sportshopin.uz/magazin/product/pole-nutrition-creatine-monohydrate-300-grams",call,creat9())

@dp.callback_query_handler(text="prometa_sports_concret")
async def menu_tanlash(call:CallbackQuery):
    await test("https://sportshopin.uz/magazin/product/promera-sports-con-cret-64-serv",call,creat10())

@dp.callback_query_handler(text="sunline_alaska")
async def menu_tanlash(call:CallbackQuery):
    await test("https://sportshopin.uz/magazin/product/sunline-alaska-kreatin-monogidrat",call,creat11())

@dp.callback_query_handler(text="fitness_authority_ice_creatine")
async def menu_tanlash(call:CallbackQuery):
    await test("https://sportshopin.uz/magazin/product/kreatin-fitness-authority-ice-creatine",call,creat12())

@dp.callback_query_handler(text="kevin_levrone_gold_creatine")
async def menu_tanlash(call:CallbackQuery):
    await test("https://sportshopin.uz/magazin/product/kreatin-v-poroshke-kevin-levrone-gold-creatine",call,creat13())

@dp.callback_query_handler(text="anabolic_creatine_kevin_levorne")
async def menu_tanlash(call:CallbackQuery):
    await test("https://sportshopin.uz/magazin/product/anabolic-creatine-ot-kevin-levrone",call,creat14())

@dp.callback_query_handler(text="creagen")
async def menu_tanlash(call:CallbackQuery):
    await test("https://sportshopin.uz/magazin/product/creagen-kreatin",call,creat15())

@dp.callback_query_handler(text="crea_kong")
async def menu_tanlash(call:CallbackQuery):
    await test("https://sportshopin.uz/magazin/product/creakong",call,creat16())

@dp.callback_query_handler(text="creatine_3000_allmax")
async def menu_tanlash(call:CallbackQuery):
    await test("https://sportshopin.uz/magazin/product/creatine-3000-all-max",call,creat17())

@dp.callback_query_handler(text="creatine_dna")
async def menu_tanlash(call:CallbackQuery):
    await test("https://sportshopin.uz/magazin/product/kreatinovyy-kompleks-vitargo-crx-2-0",call,creat18())

@dp.callback_query_handler(text="creatine_drive_nutrex")
async def menu_tanlash(call:CallbackQuery):
    await test("https://sportshopin.uz/magazin/product/creatine-drive",call,creat19())

@dp.callback_query_handler(text="creatine_monohydrate")
async def menu_tanlash(call:CallbackQuery):
    await test("https://sportshopin.uz/magazin/product/creatine-monohydrate",call,creat20())

@dp.callback_query_handler(text="CreatinemyMonohydrate")
async def menu_tanlash(call:CallbackQuery):
    await test("https://sportshopin.uz/magazin/product/creatine-monohydrate-myprotein",call,creat21())

@dp.callback_query_handler(text="creatine_pwoder300g")
async def menu_tanlash(call:CallbackQuery):
    await test("https://sportshopin.uz/magazin/product/creatine-powder-300g-100-porcij-ot-optimum-nutrition",call,creat22())

@dp.callback_query_handler(text="creatine_xsmaxip")
async def menu_tanlash(call:CallbackQuery):
    await test("https://sportshopin.uz/magazin/product/creatine-xs",call,creat23())

@dp.callback_query_handler(text="dexer_molody_jackson")
async def menu_tanlash(call:CallbackQuery):
    await test("https://sportshopin.uz/magazin/product/dexer-jackson-micronized-creatine-buld-muscle-endurance-300gm",call,creat24())
   
@dp.callback_query_handler(text="gat_creatin_powder")
async def menu_tanlash(call:CallbackQuery):
    await test("https://sportshopin.uz/magazin/product/gat-creatine-powder",call,creat25())

@dp.callback_query_handler(text="MICRONIZED_MONOHYDRATe")
async def menu_tanlash(call:CallbackQuery):
    await test("https://sportshopin.uz/magazin/product/kevin-levrone-micronized-creatine-monohydrate-300g",call,creat26())

@dp.callback_query_handler(text="workout_pilesosramhav")
async def menu_tanlash(call:CallbackQuery):
    await test("https://sportshopin.uz/magazin/product/promera-sports-con-cret-pre-workout",call,creat27())

@dp.callback_query_handler(text="Skulls_labs_angels")
async def menu_tanlash(call:CallbackQuery):
    await test("https://sportshopin.uz/magazin/product/kreatin-fa-scull-labs",call,creat28())

@dp.callback_query_handler(text="inner_armour")
async def menu_tanlash(call:CallbackQuery):
    await test("https://sportshopin.uz/magazin/product/kreatin-monogidrat-inner-armour",call,creat29())

@dp.callback_query_handler(text="apeshit_untamed_40servicious")
async def menu_tanlash(call:CallbackQuery):
    await test("https://sportshopin.uz/magazin/product/apeshit-untamed-40-servicios",call,enr1())

@dp.callback_query_handler(text="Apshit_pumps_energetic")
async def menu_tanlash(call:CallbackQuery):
    await test("https://sportshopin.uz/magazin/product/apshit-pumps",call,enr2())

@dp.callback_query_handler(text="citurulline_pure_ener")
async def menu_tanlash(call:CallbackQuery):
    await test("https://sportshopin.uz/magazin/product/citrulline-pure-ot-extrifit",call,enr3())


@dp.callback_query_handler(text="HEMORAGEUNLEASHED")
async def menu_tanlash(call:CallbackQuery):
    await test("https://sportshopin.uz/magazin/product/hemo-rage-unleashed-ot-nutrex",call,enr4())


@dp.callback_query_handler(text="noxplode_ener")
async def menu_tanlash(call:CallbackQuery):
    await test("https://sportshopin.uz/magazin/product/n-o-xplode",call,enr5())

@dp.callback_query_handler(text="pole_nutrtut_teazere_prom")
async def menu_tanlash(call:CallbackQuery):
    await test("https://sportshopin.uz/magazin/product/pole-nutrition-teazer-pre",call,enr6())



@dp.callback_query_handler(text="PreSweat_AdvancedPreWorkout")
async def menu_tanlash(call:CallbackQuery):
    await test("https://sportshopin.uz/magazin/product/pre-sweat-advanced-pre-workout",call,enr7())

@dp.callback_query_handler(text="curse_cobra_nutrtitionener")
async def menu_tanlash(call:CallbackQuery):
    await test("https://sportshopin.uz/magazin/product/the-curse-ot-cobra-nutrition",call,enr8())



@dp.callback_query_handler(text="xzchtortopomogibly")
async def menu_tanlash(call:CallbackQuery):
    await test("https://sportshopin.uz/magazin/product/c4-original",call,enr9())

@dp.callback_query_handler(text="cellucor_extreme_energ")
async def menu_tanlash(call:CallbackQuery):
    await test("https://sportshopin.uz/magazin/product/cellucor-c4-extreme-energy-270g",call,enr10())


@dp.callback_query_handler(text="guarana_energe")
async def menu_tanlash(call:CallbackQuery):
    await test("https://sportshopin.uz/magazin/product/guarana",call,enr11())


@dp.callback_query_handler(text="moons_truck_zoomad_ener")
async def menu_tanlash(call:CallbackQuery):
    await test("https://sportshopin.uz/magazin/product/the-curse-ot-cobra-nutrition",call,enr12())

@dp.callback_query_handler(text="orange_napitka")
async def menu_tanlash(call:CallbackQuery):
    await test("https://sportshopin.uz/magazin/product/energeticheskij-napitok-apelsin-500-ml",call,enr13())

@dp.callback_query_handler(text="tribilus_testoron_damn")
async def menu_tanlash(call:CallbackQuery):
    await test("https://sportshopin.uz/magazin/product/tribulus-ot-bpi-sports-180-kapsul",call,bbst1())

@dp.callback_query_handler(text="primeval_labs_alphha")
async def menu_tanlash(call:CallbackQuery):
    await test("https://sportshopin.uz/magazin/product/primeval-labs-apesh-t-alfa",call,bbst2())

@dp.callback_query_handler(text="primeval_labs_apesh_test")
async def menu_tanlash(call:CallbackQuery):
    await test("https://sportshopin.uz/magazin/product/test-primeval-labs-apesh-t",call,bbst3())

@dp.callback_query_handler(text="ultimate_nutrition_testoron_grow")
async def menu_tanlash(call:CallbackQuery):
    await test("https://sportshopin.uz/magazin/product/ultimate-nutrition-testostron-grow-hp-126-tablets",call,bbst4())

@dp.callback_query_handler(text="tribulus_testoronn")
async def menu_tanlash(call:CallbackQuery):
    await test("https://sportshopin.uz/magazin/product/tribulus-terrestris-ot-vplab",call,bbst5())

@dp.callback_query_handler(text="force_factor_testoron")
async def menu_tanlash(call:CallbackQuery):
    await test("https://sportshopin.uz/magazin/product/force-factor-tribulus-mega-tribulus",call,bbst6())

@dp.callback_query_handler(text="levrone_tribulusss")
async def menu_tanlash(call:CallbackQuery):
    await test("https://sportshopin.uz/magazin/product/tribuluskl",call,bbst7())

@dp.callback_query_handler(text="testoroline_elite_gatt")
async def menu_tanlash(call:CallbackQuery):
    await test("https://sportshopin.uz/magazin/product/testrol-elite",call,bbst8())

@dp.callback_query_handler(text="Mrm_tribuplex_testoronn")
async def menu_tanlash(call:CallbackQuery):
    await test("https://sportshopin.uz/magazin/product/tribuplex-750-effektivnyj-kompleks-steroidnyh-saponinov-i-adaptogenov",call,bbst9())

@dp.callback_query_handler(text="nugenix_natural_testerone")
async def menu_tanlash(call:CallbackQuery):
    await test("https://sportshopin.uz/magazin/product/nugenix-natural-testosterone-booster-42-kapsul",call,bbst10())

@dp.callback_query_handler(text="test_thermo_muscletech")
async def menu_tanlash(call:CallbackQuery):
    await test("https://sportshopin.uz/magazin/product/test-hd-termo-test-hd-thermo-muscletech-90-kapsul",call,bbst11())

@dp.callback_query_handler(text="tribx90_salomm")
async def menu_tanlash(call:CallbackQuery):
    await test("https://sportshopin.uz/magazin/product/tribx90",call,bbst12())

@dp.callback_query_handler(text="tribulus_100mg_ener")
async def menu_tanlash(call:CallbackQuery):
    await test("https://sportshopin.uz/magazin/product/tribulus-1000-mg",call,bbst13())

@dp.callback_query_handler(text="anabolic_pak_animal_mmm")
async def menu_tanlash(call:CallbackQuery):
    await test("https://sportshopin.uz/magazin/product/universal-nutrition-animal-m-stak-21-packs",call,bbst14())

@dp.callback_query_handler(text="nutrex_tribulus_black1399")
async def menu_tanlash(call:CallbackQuery):
    await test("https://sportshopin.uz/magazin/product/tribulus-black-1300",call,bbst15())

@dp.callback_query_handler(text="tesla_turbo_testor")
async def menu_tanlash(call:CallbackQuery):
    await test("https://sportshopin.uz/magazin/product/turbo-x-testosteron-booster-by-tesla-sports-nutrition",call,bbst16())

@dp.callback_query_handler(text="kevin_levrone_anabloc90testor")
async def menu_tanlash(call:CallbackQuery):
    await test("https://sportshopin.uz/magazin/product/anabolic-test",call,bbst17())

@dp.callback_query_handler(text="evl_tribulus_testoron")
async def menu_tanlash(call:CallbackQuery):
    await test("https://sportshopin.uz/magazin/product/evl",call,bbst18())

@dp.callback_query_handler(text="tribulus_xs_120capss")
async def menu_tanlash(call:CallbackQuery):
    await test("https://sportshopin.uz/magazin/product/tribulus-xs-120-caps",call,bbst19())

@dp.callback_query_handler(text="animal_test_universal_tets")
async def menu_tanlash(call:CallbackQuery):
    await test("https://sportshopin.uz/magazin/product/universal-nutrition-animal-test-samyj-moshchnyj-buster-testesterona",call,bbst20())

@dp.callback_query_handler(text="mensmulti_testoron")
async def menu_tanlash(call:CallbackQuery):
    await test("https://sportshopin.uz/magazin/product/mens-multi-test",call,bbst21())

@dp.callback_query_handler(text="gat_sport_testorol655")
async def menu_tanlash(call:CallbackQuery):
    await test("https://sportshopin.uz/magazin/product/gat-sport-testrol65",call,bbst22())

@dp.callback_query_handler(text="bodybuilding_signaturee")
async def menu_tanlash(call:CallbackQuery):
    await test("https://sportshopin.uz/magazin/product/bodybuilding-signature-testosterone-booster",call,bbst23())

@dp.callback_query_handler(text="tribulus_elite_testoron")
async def menu_tanlash(call:CallbackQuery):
    await test("https://sportshopin.uz/magazin/product/tribulus-elite",call,bbst24())

@dp.callback_query_handler(text="ribulus_source_naturals_testor")
async def menu_tanlash(call:CallbackQuery):
    await test("https://sportshopin.uz/magazin/product/tribulus-750-mg",call,bbst25())

@dp.callback_query_handler(text="universal_pro_testoron")
async def menu_tanlash(call:CallbackQuery):
    await test("https://sportshopin.uz/magazin/product/universal-pro",call,bbst26())

@dp.callback_query_handler(text="tribuvar_1000_testoron")
async def menu_tanlash(call:CallbackQuery):
    await test("https://sportshopin.uz/magazin/product/tribuvar-1000",call,bbst27())

@dp.callback_query_handler(text="tribulus_625_on_testoron")
async def menu_tanlash(call:CallbackQuery):
    await test("https://sportshopin.uz/magazin/product/tribulus-625-on",call,bbst28())

@dp.callback_query_handler(text="tribulus_1100_1125mg")
async def menu_tanlash(call:CallbackQuery):
    await test("https://sportshopin.uz/magazin/product/tribulus-1100",call,bbst29())

@dp.callback_query_handler(text="testorone_booster_sixstar")
async def menu_tanlash(call:CallbackQuery):
    await test("https://sportshopin.uz/magazin/product/testosterone-booster-six-star",call,bbst30())

@dp.callback_query_handler(text="test_hd_testorone")
async def menu_tanlash(call:CallbackQuery):
    await test("https://sportshopin.uz/magazin/product/test-hd",call,bbst31())

@dp.callback_query_handler(text="p6_pm_testorone")
async def menu_tanlash(call:CallbackQuery):
    await test("https://sportshopin.uz/magazin/product/p6-pm-testosterone-booster",call,bbst32())

@dp.callback_query_handler(text="now_tribulus_testoron500mgg")
async def menu_tanlash(call:CallbackQuery):
    await test("https://sportshopin.uz/magazin/product/now-tribulus-500mg",call,bbst33())

@dp.callback_query_handler(text="n1_t_universtjkwehew")
async def menu_tanlash(call:CallbackQuery):
    await test("https://sportshopin.uz/magazin/product/n1-t-universal",call,bbst34())

@dp.callback_query_handler(text="evltest_evolution_nutrurthj")
async def menu_tanlash(call:CallbackQuery):
    await test("https://sportshopin.uz/magazin/product/evl-test",call,bbst35())

@dp.callback_query_handler(text="alpha-Testststsor")
async def menu_tanlash(call:CallbackQuery):
    await test("https://sportshopin.uz/magazin/product/alpha-test",call,bbst36())

@dp.callback_query_handler(text="black_tigwer_tesatorom")
async def menu_tanlash(call:CallbackQuery):
    await test("https://sportshopin.uz/magazin/product/black-tiger",call,bbst37())


@dp.callback_query_handler(text="more_proteinlar")
async def menu_tanlash(call:CallbackQuery):
     await call.message.answer_photo(
        photo = open('img/protein.jpg','rb'),
        caption = """<strong>  Купить протеины💪 в Ташкенте | Узбекистане🇺🇿  </strong>""",parse_mode='HTML',reply_markup = mor_proteins)


@dp.callback_query_handler(text="back_to_prot")
async def menu_tanlash(call:CallbackQuery):
     await call.message.answer_photo(
        photo = open('img/protein.jpg','rb'),
        caption = """<strong>  Купить протеины💪 в Ташкенте | Узбекистане🇺🇿  </strong>""",parse_mode='HTML',reply_markup = proteins)

@dp.callback_query_handler(text="back_from_protein")
async def menu_tanlash(call:CallbackQuery):
     await call.message.answer_photo(
        photo = open('img/protein.jpg','rb'),
        caption = """<strong>  Купить протеины💪 в Ташкенте | Узбекистане🇺🇿  </strong>""",parse_mode='HTML',reply_markup = proteins)

@dp.callback_query_handler(text="clean")
async def menu_tanlash(call:CallbackQuery):
    cartController.del_final(call.message.chat.id)
    await call.message.answer_photo(
        photo = open('img/protein.jpg','rb'),
        caption = """<strong>  Купить протеины💪 в Ташкенте | Узбекистане🇺🇿  </strong>""",parse_mode='HTML',reply_markup = proteins)

@dp.callback_query_handler(text="geyner")
async def menu_tanlash(call:CallbackQuery):
    await call.message.answer_photo(
        photo = open('img/protein.jpg','rb'),
        caption = """<strong>  Купить гейнеры💪 в Ташкенте | Узбекистане🇺🇿  </strong>""",parse_mode='HTML',reply_markup = its_geyner)

@dp.callback_query_handler(text="mor_geyner")
async def menu_tanlash(call:CallbackQuery):
    await call.message.answer_photo(
        photo = open('img/protein.jpg','rb'),
        caption = """<strong>  Купить гейнеры💪 в Ташкенте | Узбекистане🇺🇿  </strong>""",parse_mode='HTML',reply_markup = geynerrr)


@dp.callback_query_handler(cb.filter(id='1'))
async def menu_tanlash(call:CallbackQuery,  callback_data:dict):
    await call.answer(cache_time=18)

    product_id = callback_data.get('id')
    user = call.message.chat.id
    cartController.add_cart(user,product_id)
    await  call.message.answer('Товар добавлен в  корзину.',reply_markup=nazad_korzina())

@dp.callback_query_handler(cb.filter(id='2'))
async def menu_tanlash(call:CallbackQuery,  callback_data:dict):
    await call.answer(cache_time=18)

    product_id = callback_data.get('id')
    user = call.message.chat.id
    cartController.add_cart(user,product_id)
    await  call.message.answer('Товар добавлен в  корзину.',reply_markup=nazad_korzina())

@dp.callback_query_handler(cb.filter(id='3'))
async def menu_tanlash(call:CallbackQuery,  callback_data:dict):
    await call.answer(cache_time=18)

    product_id = callback_data.get('id')
    user = call.message.chat.id
    cartController.add_cart(user,product_id)
    await  call.message.answer('Товар добавлен в  корзину.',reply_markup=nazad_korzina())

@dp.callback_query_handler(cb.filter(id='4'))
async def menu_tanlash(call:CallbackQuery,  callback_data:dict):
    await call.answer(cache_time=18)

    product_id = callback_data.get('id')
    user = call.message.chat.id
    cartController.add_cart(user,product_id)
    await  call.message.answer('Товар добавлен в  корзину.',reply_markup=nazad_korzina())

@dp.callback_query_handler(cb.filter(id='5'))
async def menu_tanlash(call:CallbackQuery,  callback_data:dict):
    await call.answer(cache_time=18)

    product_id = callback_data.get('id')
    user = call.message.chat.id
    cartController.add_cart(user,product_id)
    await  call.message.answer('Товар добавлен в  корзину.',reply_markup=nazad_korzina())

@dp.callback_query_handler(cb.filter(id='6'))
async def menu_tanlash(call:CallbackQuery,  callback_data:dict):
    await call.answer(cache_time=18)

    product_id = callback_data.get('id')
    user = call.message.chat.id
    cartController.add_cart(user,product_id)
    await  call.message.answer('Товар добавлен в  корзину.',reply_markup=nazad_korzina())

@dp.callback_query_handler(cb.filter(id='7'))
async def menu_tanlash(call:CallbackQuery,  callback_data:dict):
    await call.answer(cache_time=18)

    product_id = callback_data.get('id')
    user = call.message.chat.id
    cartController.add_cart(user,product_id)
    await  call.message.answer('Товар добавлен в  корзину.',reply_markup=nazad_korzina())

@dp.callback_query_handler(cb.filter(id='8'))
async def menu_tanlash(call:CallbackQuery,  callback_data:dict):
    await call.answer(cache_time=18)

    product_id = callback_data.get('id')
    user = call.message.chat.id
    cartController.add_cart(user,product_id)
    await  call.message.answer('Товар добавлен в  корзину.',reply_markup=nazad_korzina())

@dp.callback_query_handler(cb.filter(id='9'))
async def menu_tanlash(call:CallbackQuery,  callback_data:dict):
    await call.answer(cache_time=18)

    product_id = callback_data.get('id')
    user = call.message.chat.id
    cartController.add_cart(user,product_id)
    await  call.message.answer('Товар добавлен в  корзину.',reply_markup=nazad_korzina())

@dp.callback_query_handler(cb.filter(id='10'))
async def menu_tanlash(call:CallbackQuery,  callback_data:dict):
    await call.answer(cache_time=18)

    product_id = callback_data.get('id')
    user = call.message.chat.id
    cartController.add_cart(user,product_id)
    await  call.message.answer('Товар добавлен в  корзину.',reply_markup=nazad_korzina())

@dp.callback_query_handler(cb.filter(id='11'))
async def menu_tanlash(call:CallbackQuery,  callback_data:dict):
    await call.answer(cache_time=18)

    product_id = callback_data.get('id')
    user = call.message.chat.id
    cartController.add_cart(user,product_id)
    await  call.message.answer('Товар добавлен в  корзину.',reply_markup=nazad_korzina())
    

@dp.callback_query_handler(cb.filter(id='12'))
async def menu_tanlash(call:CallbackQuery,  callback_data:dict):
    await call.answer(cache_time=18)

    product_id = callback_data.get('id')
    user = call.message.chat.id
    cartController.add_cart(user,product_id)
    await  call.message.answer('Товар добавлен в  корзину.',reply_markup=nazad_korzina())

@dp.callback_query_handler(cb.filter(id='13'))
async def menu_tanlash(call:CallbackQuery,  callback_data:dict):
    await call.answer(cache_time=18)

    product_id = callback_data.get('id')
    user = call.message.chat.id
    cartController.add_cart(user,product_id)
    await  call.message.answer('Товар добавлен в  корзину.',reply_markup=nazad_korzina())

@dp.callback_query_handler(cb.filter(id='14'))
async def menu_tanlash(call:CallbackQuery,  callback_data:dict):
    await call.answer(cache_time=18)

    product_id = callback_data.get('id')
    user = call.message.chat.id
    cartController.add_cart(user,product_id)
    await  call.message.answer('Товар добавлен в  корзину.',reply_markup=nazad_korzina())

@dp.callback_query_handler(cb.filter(id='15'))
async def menu_tanlash(call:CallbackQuery,  callback_data:dict):
    await call.answer(cache_time=18)

    product_id = callback_data.get('id')
    user = call.message.chat.id
    cartController.add_cart(user,product_id)
    await  call.message.answer('Товар добавлен в  корзину.',reply_markup=nazad_korzina())

@dp.callback_query_handler(cb.filter(id='16'))
async def menu_tanlash(call:CallbackQuery,  callback_data:dict):
    await call.answer(cache_time=18)

    product_id = callback_data.get('id')
    user = call.message.chat.id
    cartController.add_cart(user,product_id)
    await  call.message.answer('Товар добавлен в  корзину.',reply_markup=nazad_korzina())

@dp.callback_query_handler(cb.filter(id='17'))
async def menu_tanlash(call:CallbackQuery,  callback_data:dict):
    await call.answer(cache_time=18)

    product_id = callback_data.get('id')
    user = call.message.chat.id
    cartController.add_cart(user,product_id)
    await  call.message.answer('Товар добавлен в  корзину.',reply_markup=nazad_korzina())

@dp.callback_query_handler(cb.filter(id='18'))
async def menu_tanlash(call:CallbackQuery,  callback_data:dict):
    await call.answer(cache_time=18)

    product_id = callback_data.get('id')
    user = call.message.chat.id
    cartController.add_cart(user,product_id)
    await  call.message.answer('Товар добавлен в  корзину.',reply_markup=nazad_korzina())

@dp.callback_query_handler(cb.filter(id='19'))
async def menu_tanlash(call:CallbackQuery,  callback_data:dict):
    await call.answer(cache_time=18)

    product_id = callback_data.get('id')
    user = call.message.chat.id
    cartController.add_cart(user,product_id)
    await  call.message.answer('Товар добавлен в  корзину.',reply_markup=nazad_korzina())

@dp.callback_query_handler(cb.filter(id='20'))
async def menu_tanlash(call:CallbackQuery,  callback_data:dict):
    await call.answer(cache_time=18)

    product_id = callback_data.get('id')
    user = call.message.chat.id
    cartController.add_cart(user,product_id)
    await  call.message.answer('Товар добавлен в  корзину.',reply_markup=nazad_korzina())

@dp.callback_query_handler(cb.filter(id='21'))
async def menu_tanlash(call:CallbackQuery,  callback_data:dict):
    await call.answer(cache_time=18)

    product_id = callback_data.get('id')
    user = call.message.chat.id
    cartController.add_cart(user,product_id)
    await  call.message.answer('Товар добавлен в  корзину.',reply_markup=nazad_korzina())

@dp.callback_query_handler(cb.filter(id='22'))
async def menu_tanlash(call:CallbackQuery,  callback_data:dict):
    await call.answer(cache_time=18)

    product_id = callback_data.get('id')
    user = call.message.chat.id
    cartController.add_cart(user,product_id)
    await  call.message.answer('Товар добавлен в  корзину.',reply_markup=nazad_korzina())

@dp.callback_query_handler(cb.filter(id='23'))
async def menu_tanlash(call:CallbackQuery,  callback_data:dict):
    await call.answer(cache_time=18)

    product_id = callback_data.get('id')
    user = call.message.chat.id
    cartController.add_cart(user,product_id)
    await  call.message.answer('Товар добавлен в  корзину.',reply_markup=nazad_korzina())

@dp.callback_query_handler(cb.filter(id='24'))
async def menu_tanlash(call:CallbackQuery,  callback_data:dict):
    await call.answer(cache_time=18)

    product_id = callback_data.get('id')
    user = call.message.chat.id
    cartController.add_cart(user,product_id)
    await  call.message.answer('Товар добавлен в  корзину.',reply_markup=nazad_korzina())

@dp.callback_query_handler(cb.filter(id='25'))
async def menu_tanlash(call:CallbackQuery,  callback_data:dict):
    await call.answer(cache_time=18)

    product_id = callback_data.get('id')
    user = call.message.chat.id
    cartController.add_cart(user,product_id)
    await  call.message.answer('Товар добавлен в  корзину.',reply_markup=nazad_korzina())

@dp.callback_query_handler(cb.filter(id='26'))
async def menu_tanlash(call:CallbackQuery,  callback_data:dict):
    await call.answer(cache_time=18)

    product_id = callback_data.get('id')
    user = call.message.chat.id
    cartController.add_cart(user,product_id)
    await  call.message.answer('Товар добавлен в  корзину.',reply_markup=nazad_korzina())

@dp.callback_query_handler(cb.filter(id='27'))
async def menu_tanlash(call:CallbackQuery,  callback_data:dict):
    await call.answer(cache_time=18)

    product_id = callback_data.get('id')
    user = call.message.chat.id
    cartController.add_cart(user,product_id)
    await  call.message.answer('Товар добавлен в  корзину.',reply_markup=nazad_korzina())

@dp.callback_query_handler(cb.filter(id='28'))
async def menu_tanlash(call:CallbackQuery,  callback_data:dict):
    await call.answer(cache_time=18)

    product_id = callback_data.get('id')
    user = call.message.chat.id
    cartController.add_cart(user,product_id)
    await  call.message.answer('Товар добавлен в  корзину.',reply_markup=nazad_korzina())

@dp.callback_query_handler(cb.filter(id='29'))
async def menu_tanlash(call:CallbackQuery,  callback_data:dict):
    await call.answer(cache_time=18)

    product_id = callback_data.get('id')
    user = call.message.chat.id
    cartController.add_cart(user,product_id)
    await  call.message.answer('Товар добавлен в  корзину.',reply_markup=nazad_korzina())

@dp.callback_query_handler(cb.filter(id='30'))
async def menu_tanlash(call:CallbackQuery,  callback_data:dict):
    await call.answer(cache_time=18)

    product_id = callback_data.get('id')
    user = call.message.chat.id
    cartController.add_cart(user,product_id)
    await  call.message.answer('Товар добавлен в  корзину.',reply_markup=nazad_korzina())

@dp.callback_query_handler(cb.filter(id='31'))
async def menu_tanlash(call:CallbackQuery,  callback_data:dict):
    await call.answer(cache_time=18)

    product_id = callback_data.get('id')
    user = call.message.chat.id
    cartController.add_cart(user,product_id)
    await  call.message.answer('Товар добавлен в  корзину.',reply_markup=nazad_korzina())

@dp.callback_query_handler(cb.filter(id='32'))
async def menu_tanlash(call:CallbackQuery,  callback_data:dict):
    await call.answer(cache_time=18)

    product_id = callback_data.get('id')
    user = call.message.chat.id
    cartController.add_cart(user,product_id)
    await  call.message.answer('Товар добавлен в  корзину.',reply_markup=nazad_korzina())

@dp.callback_query_handler(cb.filter(id='33'))
async def menu_tanlash(call:CallbackQuery,  callback_data:dict):
    await call.answer(cache_time=18)

    product_id = callback_data.get('id')
    user = call.message.chat.id
    cartController.add_cart(user,product_id)
    await  call.message.answer('Товар добавлен в  корзину.',reply_markup=nazad_korzina())

@dp.callback_query_handler(cb.filter(id='34'))
async def menu_tanlash(call:CallbackQuery,  callback_data:dict):
    await call.answer(cache_time=18)

    product_id = callback_data.get('id')
    user = call.message.chat.id
    cartController.add_cart(user,product_id)
    await  call.message.answer('Товар добавлен в  корзину.',reply_markup=nazad_korzina())

@dp.callback_query_handler(cb.filter(id='35'))
async def menu_tanlash(call:CallbackQuery,  callback_data:dict):
    await call.answer(cache_time=18)

    product_id = callback_data.get('id')
    user = call.message.chat.id
    cartController.add_cart(user,product_id)
    await  call.message.answer('Товар добавлен в  корзину.',reply_markup=nazad_korzina())

@dp.callback_query_handler(cb.filter(id='36'))
async def menu_tanlash(call:CallbackQuery,  callback_data:dict):
    await call.answer(cache_time=18)

    product_id = callback_data.get('id')
    user = call.message.chat.id
    cartController.add_cart(user,product_id)
    await  call.message.answer('Товар добавлен в  корзину.',reply_markup=nazad_korzina())

@dp.callback_query_handler(cb.filter(id='37'))
async def menu_tanlash(call:CallbackQuery,  callback_data:dict):
    await call.answer(cache_time=18)

    product_id = callback_data.get('id')
    user = call.message.chat.id
    cartController.add_cart(user,product_id)
    await  call.message.answer('Товар добавлен в  корзину.',reply_markup=nazad_korzina())

@dp.callback_query_handler(cb.filter(id='38'))
async def menu_tanlash(call:CallbackQuery,  callback_data:dict):
    await call.answer(cache_time=18)

    product_id = callback_data.get('id')
    user = call.message.chat.id
    cartController.add_cart(user,product_id)
    await  call.message.answer('Товар добавлен в  корзину.',reply_markup=nazad_korzina())

@dp.callback_query_handler(cb.filter(id='39'))
async def menu_tanlash(call:CallbackQuery,  callback_data:dict):
    await call.answer(cache_time=18)

    product_id = callback_data.get('id')
    user = call.message.chat.id
    cartController.add_cart(user,product_id)
    await  call.message.answer('Товар добавлен в  корзину.',reply_markup=nazad_korzina())

@dp.callback_query_handler(cb.filter(id='40'))
async def menu_tanlash(call:CallbackQuery,  callback_data:dict):
    await call.answer(cache_time=18)

    product_id = callback_data.get('id')
    user = call.message.chat.id
    cartController.add_cart(user,product_id)
    await  call.message.answer('Товар добавлен в  корзину.',reply_markup=nazad_korzina())

@dp.callback_query_handler(cb.filter(id='41'))
async def menu_tanlash(call:CallbackQuery,  callback_data:dict):
    await call.answer(cache_time=18)

    product_id = callback_data.get('id')
    user = call.message.chat.id
    cartController.add_cart(user,product_id)
    await  call.message.answer('Товар добавлен в  корзину.',reply_markup=nazad_korzina())

@dp.callback_query_handler(cb.filter(id='42'))
async def menu_tanlash(call:CallbackQuery,  callback_data:dict):
    await call.answer(cache_time=18)

    product_id = callback_data.get('id')
    user = call.message.chat.id
    cartController.add_cart(user,product_id)
    await  call.message.answer('Товар добавлен в  корзину.',reply_markup=nazad_korzina())

@dp.callback_query_handler(cb.filter(id='43'))
async def menu_tanlash(call:CallbackQuery,  callback_data:dict):
    await call.answer(cache_time=18)

    product_id = callback_data.get('id')
    user = call.message.chat.id
    cartController.add_cart(user,product_id)
    await  call.message.answer('Товар добавлен в  корзину.',reply_markup=nazad_korzina())


@dp.callback_query_handler(cb.filter(id='44'))
async def menu_tanlash(call:CallbackQuery,  callback_data:dict):
    await call.answer(cache_time=18)

    product_id = callback_data.get('id')
    user = call.message.chat.id
    cartController.add_cart(user,product_id)
    await  call.message.answer('Товар добавлен в  корзину.',reply_markup=nazad_korzina())

@dp.callback_query_handler(cb.filter(id='45'))
async def menu_tanlash(call:CallbackQuery,  callback_data:dict):
    await call.answer(cache_time=18)

    product_id = callback_data.get('id')
    user = call.message.chat.id
    cartController.add_cart(user,product_id)
    await  call.message.answer('Товар добавлен в  корзину.',reply_markup=nazad_korzina())

@dp.callback_query_handler(cb.filter(id='46'))
async def menu_tanlash(call:CallbackQuery,  callback_data:dict):
    await call.answer(cache_time=18)

    product_id = callback_data.get('id')
    user = call.message.chat.id
    cartController.add_cart(user,product_id)
    await  call.message.answer('Товар добавлен в  корзину.',reply_markup=nazad_korzina())

@dp.callback_query_handler(cb.filter(id='47'))
async def menu_tanlash(call:CallbackQuery,  callback_data:dict):
    await call.answer(cache_time=18)

    product_id = callback_data.get('id')
    user = call.message.chat.id
    cartController.add_cart(user,product_id)
    await  call.message.answer('Товар добавлен в  корзину.',reply_markup=nazad_korzina())

@dp.callback_query_handler(cb.filter(id='48'))
async def menu_tanlash(call:CallbackQuery,  callback_data:dict):
    await call.answer(cache_time=18)

    product_id = callback_data.get('id')
    user = call.message.chat.id
    cartController.add_cart(user,product_id)
    await  call.message.answer('Товар добавлен в  корзину.',reply_markup=nazad_korzina())

@dp.callback_query_handler(cb.filter(id='49'))
async def menu_tanlash(call:CallbackQuery,  callback_data:dict):
    await call.answer(cache_time=18)

    product_id = callback_data.get('id')
    user = call.message.chat.id
    cartController.add_cart(user,product_id)
    await  call.message.answer('Товар добавлен в  корзину.',reply_markup=nazad_korzina())

@dp.callback_query_handler(cb.filter(id='50'))
async def menu_tanlash(call:CallbackQuery,  callback_data:dict):
    await call.answer(cache_time=18)

    product_id = callback_data.get('id')
    user = call.message.chat.id
    cartController.add_cart(user,product_id)
    await  call.message.answer('Товар добавлен в  корзину.',reply_markup=nazad_korzina())

@dp.callback_query_handler(cb.filter(id='51'))
async def menu_tanlash(call:CallbackQuery,  callback_data:dict):
    await call.answer(cache_time=18)

    product_id = callback_data.get('id')
    user = call.message.chat.id
    cartController.add_cart(user,product_id)
    await  call.message.answer('Товар добавлен в  корзину.',reply_markup=nazad_korzina())

@dp.callback_query_handler(cb.filter(id='52'))
async def menu_tanlash(call:CallbackQuery,  callback_data:dict):
    await call.answer(cache_time=18)

    product_id = callback_data.get('id')
    user = call.message.chat.id
    cartController.add_cart(user,product_id)
    await  call.message.answer('Товар добавлен в  корзину.',reply_markup=nazad_korzina())

@dp.callback_query_handler(cb.filter(id='53'))
async def menu_tanlash(call:CallbackQuery,  callback_data:dict):
    await call.answer(cache_time=18)

    product_id = callback_data.get('id')
    user = call.message.chat.id
    cartController.add_cart(user,product_id)
    await  call.message.answer('Товар добавлен в  корзину.',reply_markup=nazad_korzina())

@dp.callback_query_handler(cb.filter(id='54'))
async def menu_tanlash(call:CallbackQuery,  callback_data:dict):
    await call.answer(cache_time=18)

    product_id = callback_data.get('id')
    user = call.message.chat.id
    cartController.add_cart(user,product_id)
    await  call.message.answer('Товар добавлен в  корзину.',reply_markup=nazad_korzina())

@dp.callback_query_handler(cb.filter(id='55'))
async def menu_tanlash(call:CallbackQuery,  callback_data:dict):
    await call.answer(cache_time=18)

    product_id = callback_data.get('id')
    user = call.message.chat.id
    cartController.add_cart(user,product_id)
    await  call.message.answer('Товар добавлен в  корзину.',reply_markup=nazad_korzina())

@dp.callback_query_handler(cb.filter(id='56'))
async def menu_tanlash(call:CallbackQuery,  callback_data:dict):
    await call.answer(cache_time=18)

    product_id = callback_data.get('id')
    user = call.message.chat.id
    cartController.add_cart(user,product_id)
    await  call.message.answer('Товар добавлен в  корзину.',reply_markup=nazad_korzina())

@dp.callback_query_handler(cb.filter(id='57'))
async def menu_tanlash(call:CallbackQuery,  callback_data:dict):
    await call.answer(cache_time=18)

    product_id = callback_data.get('id')
    user = call.message.chat.id
    cartController.add_cart(user,product_id)
    await  call.message.answer('Товар добавлен в  корзину.',reply_markup=nazad_korzina())

@dp.callback_query_handler(cb.filter(id='58'))
async def menu_tanlash(call:CallbackQuery,  callback_data:dict):
    await call.answer(cache_time=18)

    product_id = callback_data.get('id')
    user = call.message.chat.id
    cartController.add_cart(user,product_id)
    await  call.message.answer('Товар добавлен в  корзину.',reply_markup=nazad_korzina())

@dp.callback_query_handler(cb.filter(id='59'))
async def menu_tanlash(call:CallbackQuery,  callback_data:dict):
    await call.answer(cache_time=18)

    product_id = callback_data.get('id')
    user = call.message.chat.id
    cartController.add_cart(user,product_id)
    await  call.message.answer('Товар добавлен в  корзину.',reply_markup=nazad_korzina())

@dp.callback_query_handler(cb.filter(id='60'))
async def menu_tanlash(call:CallbackQuery,  callback_data:dict):
    await call.answer(cache_time=18)

    product_id = callback_data.get('id')
    user = call.message.chat.id
    cartController.add_cart(user,product_id)
    await  call.message.answer('Товар добавлен в  корзину.',reply_markup=nazad_korzina())

@dp.callback_query_handler(cb.filter(id='61'))
async def menu_tanlash(call:CallbackQuery,  callback_data:dict):
    await call.answer(cache_time=18)

    product_id = callback_data.get('id')
    user = call.message.chat.id
    cartController.add_cart(user,product_id)
    await  call.message.answer('Товар добавлен в  корзину.',reply_markup=nazad_korzina())

@dp.callback_query_handler(cb.filter(id='62'))
async def menu_tanlash(call:CallbackQuery,  callback_data:dict):
    await call.answer(cache_time=18)

    product_id = callback_data.get('id')
    user = call.message.chat.id
    cartController.add_cart(user,product_id)
    await  call.message.answer('Товар добавлен в  корзину.',reply_markup=nazad_korzina())

@dp.callback_query_handler(cb.filter(id='63'))
async def menu_tanlash(call:CallbackQuery,  callback_data:dict):
    await call.answer(cache_time=18)

    product_id = callback_data.get('id')
    user = call.message.chat.id
    cartController.add_cart(user,product_id)
    await  call.message.answer('Товар добавлен в  корзину.',reply_markup=nazad_korzina())

@dp.callback_query_handler(cb.filter(id='64'))
async def menu_tanlash(call:CallbackQuery,  callback_data:dict):
    await call.answer(cache_time=18)

    product_id = callback_data.get('id')
    user = call.message.chat.id
    cartController.add_cart(user,product_id)
    await  call.message.answer('Товар добавлен в  корзину.',reply_markup=nazad_korzina())

@dp.callback_query_handler(cb.filter(id='65'))
async def menu_tanlash(call:CallbackQuery,  callback_data:dict):
    await call.answer(cache_time=18)

    product_id = callback_data.get('id')
    user = call.message.chat.id
    cartController.add_cart(user,product_id)
    await  call.message.answer('Товар добавлен в  корзину.',reply_markup=nazad_korzina())

@dp.callback_query_handler(cb.filter(id='66'))
async def menu_tanlash(call:CallbackQuery,  callback_data:dict):
    await call.answer(cache_time=18)

    product_id = callback_data.get('id')
    user = call.message.chat.id
    cartController.add_cart(user,product_id)
    await  call.message.answer('Товар добавлен в  корзину.',reply_markup=nazad_korzina())

@dp.callback_query_handler(cb.filter(id='67'))
async def menu_tanlash(call:CallbackQuery,  callback_data:dict):
    await call.answer(cache_time=18)

    product_id = callback_data.get('id')
    user = call.message.chat.id
    cartController.add_cart(user,product_id)
    await  call.message.answer('Товар добавлен в  корзину.',reply_markup=nazad_korzina())

@dp.callback_query_handler(cb.filter(id='68'))
async def menu_tanlash(call:CallbackQuery,  callback_data:dict):
    await call.answer(cache_time=18)

    product_id = callback_data.get('id')
    user = call.message.chat.id
    cartController.add_cart(user,product_id)
    await  call.message.answer('Товар добавлен в  корзину.',reply_markup=nazad_korzina())

@dp.callback_query_handler(cb.filter(id='69'))
async def menu_tanlash(call:CallbackQuery,  callback_data:dict):
    await call.answer(cache_time=18)

    product_id = callback_data.get('id')
    user = call.message.chat.id
    cartController.add_cart(user,product_id)
    await  call.message.answer('Товар добавлен в  корзину.',reply_markup=nazad_korzina())

@dp.callback_query_handler(cb.filter(id='70'))
async def menu_tanlash(call:CallbackQuery,  callback_data:dict):
    await call.answer(cache_time=18)

    product_id = callback_data.get('id')
    user = call.message.chat.id
    cartController.add_cart(user,product_id)
    await  call.message.answer('Товар добавлен в  корзину.',reply_markup=nazad_korzina())

@dp.callback_query_handler(cb.filter(id='71'))
async def menu_tanlash(call:CallbackQuery,  callback_data:dict):
    await call.answer(cache_time=18)

    product_id = callback_data.get('id')
    user = call.message.chat.id
    cartController.add_cart(user,product_id)
    await  call.message.answer('Товар добавлен в  корзину.',reply_markup=nazad_korzina())

@dp.callback_query_handler(cb.filter(id='72'))
async def menu_tanlash(call:CallbackQuery,  callback_data:dict):
    await call.answer(cache_time=18)

    product_id = callback_data.get('id')
    user = call.message.chat.id
    cartController.add_cart(user,product_id)
    await  call.message.answer('Товар добавлен в  корзину.',reply_markup=nazad_korzina())

@dp.callback_query_handler(cb.filter(id='73'))
async def menu_tanlash(call:CallbackQuery,  callback_data:dict):
    await call.answer(cache_time=18)

    product_id = callback_data.get('id')
    user = call.message.chat.id
    cartController.add_cart(user,product_id)
    await  call.message.answer('Товар добавлен в  корзину.',reply_markup=nazad_korzina())

@dp.callback_query_handler(cb.filter(id='74'))
async def menu_tanlash(call:CallbackQuery,  callback_data:dict):
    await call.answer(cache_time=18)

    product_id = callback_data.get('id')
    user = call.message.chat.id
    cartController.add_cart(user,product_id)
    await  call.message.answer('Товар добавлен в  корзину.',reply_markup=nazad_korzina())

@dp.callback_query_handler(cb.filter(id='75'))
async def menu_tanlash(call:CallbackQuery,  callback_data:dict):
    await call.answer(cache_time=18)

    product_id = callback_data.get('id')
    user = call.message.chat.id
    cartController.add_cart(user,product_id)
    await  call.message.answer('Товар добавлен в  корзину.',reply_markup=nazad_korzina())

@dp.callback_query_handler(cb.filter(id='76'))
async def menu_tanlash(call:CallbackQuery,  callback_data:dict):
    await call.answer(cache_time=18)

    product_id = callback_data.get('id')
    user = call.message.chat.id
    cartController.add_cart(user,product_id)
    await  call.message.answer('Товар добавлен в  корзину.',reply_markup=nazad_korzina())

@dp.callback_query_handler(cb.filter(id='77'))
async def menu_tanlash(call:CallbackQuery,  callback_data:dict):
    await call.answer(cache_time=18)

    product_id = callback_data.get('id')
    user = call.message.chat.id
    cartController.add_cart(user,product_id)
    await  call.message.answer('Товар добавлен в  корзину.',reply_markup=nazad_korzina())

@dp.callback_query_handler(cb.filter(id='78'))
async def menu_tanlash(call:CallbackQuery,  callback_data:dict):
    await call.answer(cache_time=18)

    product_id = callback_data.get('id')
    user = call.message.chat.id
    cartController.add_cart(user,product_id)
    await  call.message.answer('Товар добавлен в  корзину.',reply_markup=nazad_korzina())

@dp.callback_query_handler(cb.filter(id='79'))
async def menu_tanlash(call:CallbackQuery,  callback_data:dict):
    await call.answer(cache_time=18)

    product_id = callback_data.get('id')
    user = call.message.chat.id
    cartController.add_cart(user,product_id)
    await  call.message.answer('Товар добавлен в  корзину.',reply_markup=nazad_korzina())

@dp.callback_query_handler(cb.filter(id='80'))
async def menu_tanlash(call:CallbackQuery,  callback_data:dict):
    await call.answer(cache_time=18)

    product_id = callback_data.get('id')
    user = call.message.chat.id
    cartController.add_cart(user,product_id)
    await  call.message.answer('Товар добавлен в  корзину.',reply_markup=nazad_korzina())

@dp.callback_query_handler(cb.filter(id='81'))
async def menu_tanlash(call:CallbackQuery,  callback_data:dict):
    await call.answer(cache_time=18)

    product_id = callback_data.get('id')
    user = call.message.chat.id
    cartController.add_cart(user,product_id)
    await  call.message.answer('Товар добавлен в  корзину.',reply_markup=nazad_korzina())

@dp.callback_query_handler(cb.filter(id='82'))
async def menu_tanlash(call:CallbackQuery,  callback_data:dict):
    await call.answer(cache_time=18)

    product_id = callback_data.get('id')
    user = call.message.chat.id
    cartController.add_cart(user,product_id)
    await  call.message.answer('Товар добавлен в  корзину.',reply_markup=nazad_korzina())

@dp.callback_query_handler(cb.filter(id='83'))
async def menu_tanlash(call:CallbackQuery,  callback_data:dict):
    await call.answer(cache_time=18)

    product_id = callback_data.get('id')
    user = call.message.chat.id
    cartController.add_cart(user,product_id)
    await  call.message.answer('Товар добавлен в  корзину.',reply_markup=nazad_korzina())

@dp.callback_query_handler(cb.filter(id='84'))
async def menu_tanlash(call:CallbackQuery,  callback_data:dict):
    await call.answer(cache_time=18)

    product_id = callback_data.get('id')
    user = call.message.chat.id
    cartController.add_cart(user,product_id)
    await  call.message.answer('Товар добавлен в  корзину.',reply_markup=nazad_korzina())

@dp.callback_query_handler(cb.filter(id='85'))
async def menu_tanlash(call:CallbackQuery,  callback_data:dict):
    await call.answer(cache_time=18)

    product_id = callback_data.get('id')
    user = call.message.chat.id
    cartController.add_cart(user,product_id)
    await  call.message.answer('Товар добавлен в  корзину.',reply_markup=nazad_korzina())

@dp.callback_query_handler(cb.filter(id='86'))
async def menu_tanlash(call:CallbackQuery,  callback_data:dict):
    await call.answer(cache_time=18)

    product_id = callback_data.get('id')
    user = call.message.chat.id
    cartController.add_cart(user,product_id)
    await  call.message.answer('Товар добавлен в  корзину.',reply_markup=nazad_korzina())

@dp.callback_query_handler(cb.filter(id='87'))
async def menu_tanlash(call:CallbackQuery,  callback_data:dict):
    await call.answer(cache_time=18)

    product_id = callback_data.get('id')
    user = call.message.chat.id
    cartController.add_cart(user,product_id)
    await  call.message.answer('Товар добавлен в  корзину.',reply_markup=nazad_korzina())

@dp.callback_query_handler(cb.filter(id='88'))
async def menu_tanlash(call:CallbackQuery,  callback_data:dict):
    await call.answer(cache_time=18)

    product_id = callback_data.get('id')
    user = call.message.chat.id
    cartController.add_cart(user,product_id)
    await  call.message.answer('Товар добавлен в  корзину.',reply_markup=nazad_korzina())

@dp.callback_query_handler(cb.filter(id='89'))
async def menu_tanlash(call:CallbackQuery,  callback_data:dict):
    await call.answer(cache_time=18)

    product_id = callback_data.get('id')
    user = call.message.chat.id
    cartController.add_cart(user,product_id)
    await  call.message.answer('Товар добавлен в  корзину.',reply_markup=nazad_korzina())

@dp.callback_query_handler(cb.filter(id='90'))
async def menu_tanlash(call:CallbackQuery,  callback_data:dict):
    await call.answer(cache_time=18)

    product_id = callback_data.get('id')
    user = call.message.chat.id
    cartController.add_cart(user,product_id)
    await  call.message.answer('Товар добавлен в  корзину.',reply_markup=nazad_korzina())

@dp.callback_query_handler(cb.filter(id='91'))
async def menu_tanlash(call:CallbackQuery,  callback_data:dict):
    await call.answer(cache_time=18)

    product_id = callback_data.get('id')
    user = call.message.chat.id
    cartController.add_cart(user,product_id)
    await  call.message.answer('Товар добавлен в  корзину.',reply_markup=nazad_korzina())

@dp.callback_query_handler(cb.filter(id='92'))
async def menu_tanlash(call:CallbackQuery,  callback_data:dict):
    await call.answer(cache_time=18)

    product_id = callback_data.get('id')
    user = call.message.chat.id
    cartController.add_cart(user,product_id)
    await  call.message.answer('Товар добавлен в  корзину.',reply_markup=nazad_korzina())

@dp.callback_query_handler(cb.filter(id='93'))
async def menu_tanlash(call:CallbackQuery,  callback_data:dict):
    await call.answer(cache_time=18)

    product_id = callback_data.get('id')
    user = call.message.chat.id
    cartController.add_cart(user,product_id)
    await  call.message.answer('Товар добавлен в  корзину.',reply_markup=nazad_korzina())

@dp.callback_query_handler(cb.filter(id='94'))
async def menu_tanlash(call:CallbackQuery,  callback_data:dict):
    await call.answer(cache_time=18)

    product_id = callback_data.get('id')
    user = call.message.chat.id
    cartController.add_cart(user,product_id)
    await  call.message.answer('Товар добавлен в  корзину.',reply_markup=nazad_korzina())

@dp.callback_query_handler(cb.filter(id='95'))
async def menu_tanlash(call:CallbackQuery,  callback_data:dict):
    await call.answer(cache_time=18)

    product_id = callback_data.get('id')
    user = call.message.chat.id
    cartController.add_cart(user,product_id)
    await  call.message.answer('Товар добавлен в  корзину.',reply_markup=nazad_korzina())

@dp.callback_query_handler(cb.filter(id='96'))
async def menu_tanlash(call:CallbackQuery,  callback_data:dict):
    await call.answer(cache_time=18)

    product_id = callback_data.get('id')
    user = call.message.chat.id
    cartController.add_cart(user,product_id)
    await  call.message.answer('Товар добавлен в  корзину.',reply_markup=nazad_korzina())

@dp.callback_query_handler(cb.filter(id='97'))
async def menu_tanlash(call:CallbackQuery,  callback_data:dict):
    await call.answer(cache_time=18)

    product_id = callback_data.get('id')
    user = call.message.chat.id
    cartController.add_cart(user,product_id)
    await  call.message.answer('Товар добавлен в  корзину.',reply_markup=nazad_korzina())

@dp.callback_query_handler(cb.filter(id='98'))
async def menu_tanlash(call:CallbackQuery,  callback_data:dict):
    await call.answer(cache_time=18)

    product_id = callback_data.get('id')
    user = call.message.chat.id
    cartController.add_cart(user,product_id)
    await  call.message.answer('Товар добавлен в  корзину.',reply_markup=nazad_korzina())

@dp.callback_query_handler(cb.filter(id='99'))
async def menu_tanlash(call:CallbackQuery,  callback_data:dict):
    await call.answer(cache_time=18)

    product_id = callback_data.get('id')
    user = call.message.chat.id
    cartController.add_cart(user,product_id)
    await  call.message.answer('Товар добавлен в  корзину.',reply_markup=nazad_korzina())

@dp.callback_query_handler(cb.filter(id='100'))
async def menu_tanlash(call:CallbackQuery,  callback_data:dict):
    await call.answer(cache_time=18)

    product_id = callback_data.get('id')
    user = call.message.chat.id
    cartController.add_cart(user,product_id)
    await  call.message.answer('Товар добавлен в  корзину.',reply_markup=nazad_korzina())

@dp.callback_query_handler(cb.filter(id='101'))
async def menu_tanlash(call:CallbackQuery,  callback_data:dict):
    await call.answer(cache_time=18)

    product_id = callback_data.get('id')
    user = call.message.chat.id
    cartController.add_cart(user,product_id)
    await  call.message.answer('Товар добавлен в  корзину.',reply_markup=nazad_korzina())

@dp.callback_query_handler(cb.filter(id='102'))
async def menu_tanlash(call:CallbackQuery,  callback_data:dict):
    await call.answer(cache_time=18)

    product_id = callback_data.get('id')
    user = call.message.chat.id
    cartController.add_cart(user,product_id)
    await  call.message.answer('Товар добавлен в  корзину.',reply_markup=nazad_korzina())

@dp.callback_query_handler(cb.filter(id='103'))
async def menu_tanlash(call:CallbackQuery,  callback_data:dict):
    await call.answer(cache_time=18)

    product_id = callback_data.get('id')
    user = call.message.chat.id
    cartController.add_cart(user,product_id)
    await  call.message.answer('Товар добавлен в  корзину.',reply_markup=nazad_korzina())

@dp.callback_query_handler(cb.filter(id='104'))
async def menu_tanlash(call:CallbackQuery,  callback_data:dict):
    await call.answer(cache_time=18)

    product_id = callback_data.get('id')
    user = call.message.chat.id
    cartController.add_cart(user,product_id)
    await  call.message.answer('Товар добавлен в  корзину.',reply_markup=nazad_korzina())

@dp.callback_query_handler(cb.filter(id='105'))
async def menu_tanlash(call:CallbackQuery,  callback_data:dict):
    await call.answer(cache_time=18)

    product_id = callback_data.get('id')
    user = call.message.chat.id
    cartController.add_cart(user,product_id)
    await  call.message.answer('Товар добавлен в  корзину.',reply_markup=nazad_korzina())

@dp.callback_query_handler(cb.filter(id='106'))
async def menu_tanlash(call:CallbackQuery,  callback_data:dict):
    await call.answer(cache_time=18)

    product_id = callback_data.get('id')
    user = call.message.chat.id
    cartController.add_cart(user,product_id)
    await  call.message.answer('Товар добавлен в  корзину.',reply_markup=nazad_korzina())

@dp.callback_query_handler(cb.filter(id='107'))
async def menu_tanlash(call:CallbackQuery,  callback_data:dict):
    await call.answer(cache_time=18)

    product_id = callback_data.get('id')
    user = call.message.chat.id
    cartController.add_cart(user,product_id)
    await  call.message.answer('Товар добавлен в  корзину.',reply_markup=nazad_korzina())

@dp.callback_query_handler(cb.filter(id='108'))
async def menu_tanlash(call:CallbackQuery,  callback_data:dict):
    await call.answer(cache_time=18)

    product_id = callback_data.get('id')
    user = call.message.chat.id
    cartController.add_cart(user,product_id)
    await  call.message.answer('Товар добавлен в  корзину.',reply_markup=nazad_korzina())

@dp.callback_query_handler(cb.filter(id='109'))
async def menu_tanlash(call:CallbackQuery,  callback_data:dict):
    await call.answer(cache_time=18)

    product_id = callback_data.get('id')
    user = call.message.chat.id
    cartController.add_cart(user,product_id)
    await  call.message.answer('Товар добавлен в  корзину.',reply_markup=nazad_korzina())

@dp.callback_query_handler(cb.filter(id='110'))
async def menu_tanlash(call:CallbackQuery,  callback_data:dict):
    await call.answer(cache_time=18)

    product_id = callback_data.get('id')
    user = call.message.chat.id
    cartController.add_cart(user,product_id)
    await  call.message.answer('Товар добавлен в  корзину.',reply_markup=nazad_korzina())

@dp.callback_query_handler(cb.filter(id='111'))
async def menu_tanlash(call:CallbackQuery,  callback_data:dict):
    await call.answer(cache_time=18)

    product_id = callback_data.get('id')
    user = call.message.chat.id
    cartController.add_cart(user,product_id)
    await  call.message.answer('Товар добавлен в  корзину.',reply_markup=nazad_korzina())

@dp.callback_query_handler(cb.filter(id='112'))
async def menu_tanlash(call:CallbackQuery,  callback_data:dict):
    await call.answer(cache_time=18)

    product_id = callback_data.get('id')
    user = call.message.chat.id
    cartController.add_cart(user,product_id)
    await  call.message.answer('Товар добавлен в  корзину.',reply_markup=nazad_korzina())

@dp.callback_query_handler(cb.filter(id='113'))
async def menu_tanlash(call:CallbackQuery,  callback_data:dict):
    await call.answer(cache_time=18)

    product_id = callback_data.get('id')
    user = call.message.chat.id
    cartController.add_cart(user,product_id)
    await  call.message.answer('Товар добавлен в  корзину.',reply_markup=nazad_korzina())

@dp.callback_query_handler(cb.filter(id='114'))
async def menu_tanlash(call:CallbackQuery,  callback_data:dict):
    await call.answer(cache_time=18)

    product_id = callback_data.get('id')
    user = call.message.chat.id
    cartController.add_cart(user,product_id)
    await  call.message.answer('Товар добавлен в  корзину.',reply_markup=nazad_korzina())

@dp.callback_query_handler(cb.filter(id='115'))
async def menu_tanlash(call:CallbackQuery,  callback_data:dict):
    await call.answer(cache_time=18)

    product_id = callback_data.get('id')
    user = call.message.chat.id
    cartController.add_cart(user,product_id)
    await  call.message.answer('Товар добавлен в  корзину.',reply_markup=nazad_korzina())

@dp.callback_query_handler(cb.filter(id='116'))
async def menu_tanlash(call:CallbackQuery,  callback_data:dict):
    await call.answer(cache_time=18)

    product_id = callback_data.get('id')
    user = call.message.chat.id
    cartController.add_cart(user,product_id)
    await  call.message.answer('Товар добавлен в  корзину.',reply_markup=nazad_korzina())

@dp.callback_query_handler(cb.filter(id='117'))
async def menu_tanlash(call:CallbackQuery,  callback_data:dict):
    await call.answer(cache_time=18)

    product_id = callback_data.get('id')
    user = call.message.chat.id
    cartController.add_cart(user,product_id)
    await  call.message.answer('Товар добавлен в  корзину.',reply_markup=nazad_korzina())

@dp.callback_query_handler(cb.filter(id='118'))
async def menu_tanlash(call:CallbackQuery,  callback_data:dict):
    await call.answer(cache_time=18)

    product_id = callback_data.get('id')
    user = call.message.chat.id
    cartController.add_cart(user,product_id)
    await  call.message.answer('Товар добавлен в  корзину.',reply_markup=nazad_korzina())

@dp.callback_query_handler(cb.filter(id='119'))
async def menu_tanlash(call:CallbackQuery,  callback_data:dict):
    await call.answer(cache_time=18)

    product_id = callback_data.get('id')
    user = call.message.chat.id
    cartController.add_cart(user,product_id)
    await  call.message.answer('Товар добавлен в  корзину.',reply_markup=nazad_korzina())

@dp.callback_query_handler(cb.filter(id='120'))
async def menu_tanlash(call:CallbackQuery,  callback_data:dict):
    await call.answer(cache_time=18)

    product_id = callback_data.get('id')
    user = call.message.chat.id
    cartController.add_cart(user,product_id)
    await  call.message.answer('Товар добавлен в  корзину.',reply_markup=nazad_korzina())

@dp.callback_query_handler(cb.filter(id='121'))
async def menu_tanlash(call:CallbackQuery,  callback_data:dict):
    await call.answer(cache_time=18)

    product_id = callback_data.get('id')
    user = call.message.chat.id
    cartController.add_cart(user,product_id)
    await  call.message.answer('Товар добавлен в  корзину.',reply_markup=nazad_korzina())

@dp.callback_query_handler(cb.filter(id='122'))
async def menu_tanlash(call:CallbackQuery,  callback_data:dict):
    await call.answer(cache_time=18)

    product_id = callback_data.get('id')
    user = call.message.chat.id
    cartController.add_cart(user,product_id)
    await  call.message.answer('Товар добавлен в  корзину.',reply_markup=nazad_korzina())

@dp.callback_query_handler(cb.filter(id='123'))
async def menu_tanlash(call:CallbackQuery,  callback_data:dict):
    await call.answer(cache_time=18)

    product_id = callback_data.get('id')
    user = call.message.chat.id
    cartController.add_cart(user,product_id)
    await  call.message.answer('Товар добавлен в  корзину.',reply_markup=nazad_korzina())

@dp.callback_query_handler(cb.filter(id='124'))
async def menu_tanlash(call:CallbackQuery,  callback_data:dict):
    await call.answer(cache_time=18)

    product_id = callback_data.get('id')
    user = call.message.chat.id
    cartController.add_cart(user,product_id)
    await  call.message.answer('Товар добавлен в  корзину.',reply_markup=nazad_korzina())

@dp.callback_query_handler(cb.filter(id='125'))
async def menu_tanlash(call:CallbackQuery,  callback_data:dict):
    await call.answer(cache_time=18)

    product_id = callback_data.get('id')
    user = call.message.chat.id
    cartController.add_cart(user,product_id)
    await  call.message.answer('Товар добавлен в  корзину.',reply_markup=nazad_korzina())

@dp.callback_query_handler(cb.filter(id='126'))
async def menu_tanlash(call:CallbackQuery,  callback_data:dict):
    await call.answer(cache_time=18)

    product_id = callback_data.get('id')
    user = call.message.chat.id
    cartController.add_cart(user,product_id)
    await  call.message.answer('Товар добавлен в  корзину.',reply_markup=nazad_korzina())

@dp.callback_query_handler(cb.filter(id='127'))
async def menu_tanlash(call:CallbackQuery,  callback_data:dict):
    await call.answer(cache_time=18)

    product_id = callback_data.get('id')
    user = call.message.chat.id
    cartController.add_cart(user,product_id)
    await  call.message.answer('Товар добавлен в  корзину.',reply_markup=nazad_korzina())

@dp.callback_query_handler(cb.filter(id='128'))
async def menu_tanlash(call:CallbackQuery,  callback_data:dict):
    await call.answer(cache_time=18)

    product_id = callback_data.get('id')
    user = call.message.chat.id
    cartController.add_cart(user,product_id)
    await  call.message.answer('Товар добавлен в  корзину.',reply_markup=nazad_korzina())

@dp.callback_query_handler(cb.filter(id='129'))
async def menu_tanlash(call:CallbackQuery,  callback_data:dict):
    await call.answer(cache_time=18)

    product_id = callback_data.get('id')
    user = call.message.chat.id
    cartController.add_cart(user,product_id)
    await  call.message.answer('Товар добавлен в  корзину.',reply_markup=nazad_korzina())

@dp.callback_query_handler(cb.filter(id='130'))
async def menu_tanlash(call:CallbackQuery,  callback_data:dict):
    await call.answer(cache_time=18)

    product_id = callback_data.get('id')
    user = call.message.chat.id
    cartController.add_cart(user,product_id)
    await  call.message.answer('Товар добавлен в  корзину.',reply_markup=nazad_korzina())

@dp.callback_query_handler(cb.filter(id='131'))
async def menu_tanlash(call:CallbackQuery,  callback_data:dict):
    await call.answer(cache_time=18)

    product_id = callback_data.get('id')
    user = call.message.chat.id
    cartController.add_cart(user,product_id)
    await  call.message.answer('Товар добавлен в  корзину.',reply_markup=nazad_korzina())

@dp.callback_query_handler(cb.filter(id='132'))
async def menu_tanlash(call:CallbackQuery,  callback_data:dict):
    await call.answer(cache_time=18)

    product_id = callback_data.get('id')
    user = call.message.chat.id
    cartController.add_cart(user,product_id)
    await  call.message.answer('Товар добавлен в  корзину.',reply_markup=nazad_korzina())

@dp.callback_query_handler(cb.filter(id='133'))
async def menu_tanlash(call:CallbackQuery,  callback_data:dict):
    await call.answer(cache_time=18)

    product_id = callback_data.get('id')
    user = call.message.chat.id
    cartController.add_cart(user,product_id)
    await  call.message.answer('Товар добавлен в  корзину.',reply_markup=nazad_korzina())

@dp.callback_query_handler(cb.filter(id='134'))
async def menu_tanlash(call:CallbackQuery,  callback_data:dict):
    await call.answer(cache_time=18)

    product_id = callback_data.get('id')
    user = call.message.chat.id
    cartController.add_cart(user,product_id)
    await  call.message.answer('Товар добавлен в  корзину.',reply_markup=nazad_korzina())

@dp.callback_query_handler(cb.filter(id='135'))
async def menu_tanlash(call:CallbackQuery,  callback_data:dict):
    await call.answer(cache_time=18)

    product_id = callback_data.get('id')
    user = call.message.chat.id
    cartController.add_cart(user,product_id)
    await  call.message.answer('Товар добавлен в  корзину.',reply_markup=nazad_korzina())

@dp.callback_query_handler(cb.filter(id='136'))
async def menu_tanlash(call:CallbackQuery,  callback_data:dict):
    await call.answer(cache_time=18)

    product_id = callback_data.get('id')
    user = call.message.chat.id
    cartController.add_cart(user,product_id)
    await  call.message.answer('Товар добавлен в  корзину.',reply_markup=nazad_korzina())

@dp.callback_query_handler(cb.filter(id='137'))
async def menu_tanlash(call:CallbackQuery,  callback_data:dict):
    await call.answer(cache_time=18)

    product_id = callback_data.get('id')
    user = call.message.chat.id
    cartController.add_cart(user,product_id)
    await  call.message.answer('Товар добавлен в  корзину.',reply_markup=nazad_korzina())

@dp.callback_query_handler(cb.filter(id='138'))
async def menu_tanlash(call:CallbackQuery,  callback_data:dict):
    await call.answer(cache_time=18)

    product_id = callback_data.get('id')
    user = call.message.chat.id
    cartController.add_cart(user,product_id)
    await  call.message.answer('Товар добавлен в  корзину.',reply_markup=nazad_korzina())

@dp.callback_query_handler(cb.filter(id='139'))
async def menu_tanlash(call:CallbackQuery,  callback_data:dict):
    await call.answer(cache_time=18)

    product_id = callback_data.get('id')
    user = call.message.chat.id
    cartController.add_cart(user,product_id)
    await  call.message.answer('Товар добавлен в  корзину.',reply_markup=nazad_korzina())

@dp.callback_query_handler(cb.filter(id='140'))
async def menu_tanlash(call:CallbackQuery,  callback_data:dict):
    await call.answer(cache_time=18)

    product_id = callback_data.get('id')
    user = call.message.chat.id
    cartController.add_cart(user,product_id)
    await  call.message.answer('Товар добавлен в  корзину.',reply_markup=nazad_korzina())

@dp.callback_query_handler(cb.filter(id='141'))
async def menu_tanlash(call:CallbackQuery,  callback_data:dict):
    await call.answer(cache_time=18)

    product_id = callback_data.get('id')
    user = call.message.chat.id
    cartController.add_cart(user,product_id)
    await  call.message.answer('Товар добавлен в  корзину.',reply_markup=nazad_korzina())

@dp.callback_query_handler(cb.filter(id='142'))
async def menu_tanlash(call:CallbackQuery,  callback_data:dict):
    await call.answer(cache_time=18)

    product_id = callback_data.get('id')
    user = call.message.chat.id
    cartController.add_cart(user,product_id)
    await  call.message.answer('Товар добавлен в  корзину.',reply_markup=nazad_korzina())

@dp.callback_query_handler(cb.filter(id='143'))
async def menu_tanlash(call:CallbackQuery,  callback_data:dict):
    await call.answer(cache_time=18)

    product_id = callback_data.get('id')
    user = call.message.chat.id
    cartController.add_cart(user,product_id)
    await  call.message.answer('Товар добавлен в  корзину.',reply_markup=nazad_korzina())

@dp.callback_query_handler(cb.filter(id='144'))
async def menu_tanlash(call:CallbackQuery,  callback_data:dict):
    await call.answer(cache_time=18)

    product_id = callback_data.get('id')
    user = call.message.chat.id
    cartController.add_cart(user,product_id)
    await  call.message.answer('Товар добавлен в  корзину.',reply_markup=nazad_korzina())

@dp.callback_query_handler(cb.filter(id='145'))
async def menu_tanlash(call:CallbackQuery,  callback_data:dict):
    await call.answer(cache_time=18)

    product_id = callback_data.get('id')
    user = call.message.chat.id
    cartController.add_cart(user,product_id)
    await  call.message.answer('Товар добавлен в  корзину.',reply_markup=nazad_korzina())

@dp.callback_query_handler(cb.filter(id='146'))
async def menu_tanlash(call:CallbackQuery,  callback_data:dict):
    await call.answer(cache_time=18)

    product_id = callback_data.get('id')
    user = call.message.chat.id
    cartController.add_cart(user,product_id)
    await  call.message.answer('Товар добавлен в  корзину.',reply_markup=nazad_korzina())

@dp.callback_query_handler(cb.filter(id='147'))
async def menu_tanlash(call:CallbackQuery,  callback_data:dict):
    await call.answer(cache_time=18)

    product_id = callback_data.get('id')
    user = call.message.chat.id
    cartController.add_cart(user,product_id)
    await  call.message.answer('Товар добавлен в  корзину.',reply_markup=nazad_korzina())

@dp.callback_query_handler(cb.filter(id='148'))
async def menu_tanlash(call:CallbackQuery,  callback_data:dict):
    await call.answer(cache_time=18)

    product_id = callback_data.get('id')
    user = call.message.chat.id
    cartController.add_cart(user,product_id)
    await  call.message.answer('Товар добавлен в  корзину.',reply_markup=nazad_korzina())

@dp.callback_query_handler(cb.filter(id='149'))
async def menu_tanlash(call:CallbackQuery,  callback_data:dict):
    await call.answer(cache_time=18)

    product_id = callback_data.get('id')
    user = call.message.chat.id
    cartController.add_cart(user,product_id)
    await  call.message.answer('Товар добавлен в  корзину.',reply_markup=nazad_korzina())

@dp.callback_query_handler(cb.filter(id='150'))
async def menu_tanlash(call:CallbackQuery,  callback_data:dict):
    await call.answer(cache_time=18)

    product_id = callback_data.get('id')
    user = call.message.chat.id
    cartController.add_cart(user,product_id)
    await  call.message.answer('Товар добавлен в  корзину.',reply_markup=nazad_korzina())

@dp.callback_query_handler(cb.filter(id='151'))
async def menu_tanlash(call:CallbackQuery,  callback_data:dict):
    await call.answer(cache_time=18)

    product_id = callback_data.get('id')
    user = call.message.chat.id
    cartController.add_cart(user,product_id)
    await  call.message.answer('Товар добавлен в  корзину.',reply_markup=nazad_korzina())

@dp.callback_query_handler(cb.filter(id='152'))
async def menu_tanlash(call:CallbackQuery,  callback_data:dict):
    await call.answer(cache_time=18)

    product_id = callback_data.get('id')
    user = call.message.chat.id
    cartController.add_cart(user,product_id)
    await  call.message.answer('Товар добавлен в  корзину.',reply_markup=nazad_korzina())

@dp.callback_query_handler(cb.filter(id='153'))
async def menu_tanlash(call:CallbackQuery,  callback_data:dict):
    await call.answer(cache_time=18)

    product_id = callback_data.get('id')
    user = call.message.chat.id
    cartController.add_cart(user,product_id)
    await  call.message.answer('Товар добавлен в  корзину.',reply_markup=nazad_korzina())

@dp.callback_query_handler(cb.filter(id='154'))
async def menu_tanlash(call:CallbackQuery,  callback_data:dict):
    await call.answer(cache_time=18)

    product_id = callback_data.get('id')
    user = call.message.chat.id
    cartController.add_cart(user,product_id)
    await  call.message.answer('Товар добавлен в  корзину.',reply_markup=nazad_korzina())

@dp.callback_query_handler(cb.filter(id='155'))
async def menu_tanlash(call:CallbackQuery,  callback_data:dict):
    await call.answer(cache_time=18)

    product_id = callback_data.get('id')
    user = call.message.chat.id
    cartController.add_cart(user,product_id)
    await  call.message.answer('Товар добавлен в  корзину.',reply_markup=nazad_korzina())

@dp.callback_query_handler(cb.filter(id='156'))
async def menu_tanlash(call:CallbackQuery,  callback_data:dict):
    await call.answer(cache_time=18)

    product_id = callback_data.get('id')
    user = call.message.chat.id
    cartController.add_cart(user,product_id)
    await  call.message.answer('Товар добавлен в  корзину.',reply_markup=nazad_korzina())

@dp.callback_query_handler(cb.filter(id='157'))
async def menu_tanlash(call:CallbackQuery,  callback_data:dict):
    await call.answer(cache_time=18)

    product_id = callback_data.get('id')
    user = call.message.chat.id
    cartController.add_cart(user,product_id)
    await  call.message.answer('Товар добавлен в  корзину.',reply_markup=nazad_korzina())

@dp.callback_query_handler(cb.filter(id='158'))
async def menu_tanlash(call:CallbackQuery,  callback_data:dict):
    await call.answer(cache_time=18)

    product_id = callback_data.get('id')
    user = call.message.chat.id
    cartController.add_cart(user,product_id)
    await  call.message.answer('Товар добавлен в  корзину.',reply_markup=nazad_korzina())

@dp.callback_query_handler(cb.filter(id='159'))
async def menu_tanlash(call:CallbackQuery,  callback_data:dict):
    await call.answer(cache_time=18)

    product_id = callback_data.get('id')
    user = call.message.chat.id
    cartController.add_cart(user,product_id)
    await  call.message.answer('Товар добавлен в  корзину.',reply_markup=nazad_korzina())

@dp.callback_query_handler(cb.filter(id='160'))
async def menu_tanlash(call:CallbackQuery,  callback_data:dict):
    await call.answer(cache_time=18)

    product_id = callback_data.get('id')
    user = call.message.chat.id
    cartController.add_cart(user,product_id)
    await  call.message.answer('Товар добавлен в  корзину.',reply_markup=nazad_korzina())

@dp.callback_query_handler(cb.filter(id='161'))
async def menu_tanlash(call:CallbackQuery,  callback_data:dict):
    await call.answer(cache_time=18)

    product_id = callback_data.get('id')
    user = call.message.chat.id
    cartController.add_cart(user,product_id)
    await  call.message.answer('Товар добавлен в  корзину.',reply_markup=nazad_korzina())

@dp.callback_query_handler(cb.filter(id='162'))
async def menu_tanlash(call:CallbackQuery,  callback_data:dict):
    await call.answer(cache_time=18)

    product_id = callback_data.get('id')
    user = call.message.chat.id
    cartController.add_cart(user,product_id)
    await  call.message.answer('Товар добавлен в  корзину.',reply_markup=nazad_korzina())

@dp.callback_query_handler(cb.filter(id='163'))
async def menu_tanlash(call:CallbackQuery,  callback_data:dict):
    await call.answer(cache_time=18)

    product_id = callback_data.get('id')
    user = call.message.chat.id
    cartController.add_cart(user,product_id)
    await  call.message.answer('Товар добавлен в  корзину.',reply_markup=nazad_korzina())

@dp.callback_query_handler(cb.filter(id='164'))
async def menu_tanlash(call:CallbackQuery,  callback_data:dict):
    await call.answer(cache_time=18)

    product_id = callback_data.get('id')
    user = call.message.chat.id
    cartController.add_cart(user,product_id)
    await  call.message.answer('Товар добавлен в  корзину.',reply_markup=nazad_korzina())

@dp.callback_query_handler(cb.filter(id='165'))
async def menu_tanlash(call:CallbackQuery,  callback_data:dict):
    await call.answer(cache_time=18)

    product_id = callback_data.get('id')
    user = call.message.chat.id
    cartController.add_cart(user,product_id)
    await  call.message.answer('Товар добавлен в  корзину.',reply_markup=nazad_korzina())

@dp.callback_query_handler(cb.filter(id='166'))
async def menu_tanlash(call:CallbackQuery,  callback_data:dict):
    await call.answer(cache_time=18)

    product_id = callback_data.get('id')
    user = call.message.chat.id
    cartController.add_cart(user,product_id)
    await  call.message.answer('Товар добавлен в  корзину.',reply_markup=nazad_korzina())

@dp.callback_query_handler(cb.filter(id='167'))
async def menu_tanlash(call:CallbackQuery,  callback_data:dict):
    await call.answer(cache_time=18)

    product_id = callback_data.get('id')
    user = call.message.chat.id
    cartController.add_cart(user,product_id)
    await  call.message.answer('Товар добавлен в  корзину.',reply_markup=nazad_korzina())

@dp.callback_query_handler(cb.filter(id='168'))
async def menu_tanlash(call:CallbackQuery,  callback_data:dict):
    await call.answer(cache_time=18)

    product_id = callback_data.get('id')
    user = call.message.chat.id
    cartController.add_cart(user,product_id)
    await  call.message.answer('Товар добавлен в  корзину.',reply_markup=nazad_korzina())

@dp.callback_query_handler(cb.filter(id='169'))
async def menu_tanlash(call:CallbackQuery,  callback_data:dict):
    await call.answer(cache_time=18)

    product_id = callback_data.get('id')
    user = call.message.chat.id
    cartController.add_cart(user,product_id)
    await  call.message.answer('Товар добавлен в  корзину.',reply_markup=nazad_korzina())

@dp.callback_query_handler(cb.filter(id='170'))
async def menu_tanlash(call:CallbackQuery,  callback_data:dict):
    await call.answer(cache_time=18)

    product_id = callback_data.get('id')
    user = call.message.chat.id
    cartController.add_cart(user,product_id)
    await  call.message.answer('Товар добавлен в  корзину.',reply_markup=nazad_korzina())

@dp.callback_query_handler(cb.filter(id='171'))
async def menu_tanlash(call:CallbackQuery,  callback_data:dict):
    await call.answer(cache_time=18)

    product_id = callback_data.get('id')
    user = call.message.chat.id
    cartController.add_cart(user,product_id)
    await  call.message.answer('Товар добавлен в  корзину.',reply_markup=nazad_korzina())

@dp.callback_query_handler(cb.filter(id='172'))
async def menu_tanlash(call:CallbackQuery,  callback_data:dict):
    await call.answer(cache_time=18)

    product_id = callback_data.get('id')
    user = call.message.chat.id
    cartController.add_cart(user,product_id)
    await  call.message.answer('Товар добавлен в  корзину.',reply_markup=nazad_korzina())

@dp.callback_query_handler(cb.filter(id='173'))
async def menu_tanlash(call:CallbackQuery,  callback_data:dict):
    await call.answer(cache_time=18)

    product_id = callback_data.get('id')
    user = call.message.chat.id
    cartController.add_cart(user,product_id)
    await  call.message.answer('Товар добавлен в  корзину.',reply_markup=nazad_korzina())

@dp.callback_query_handler(cb.filter(id='174'))
async def menu_tanlash(call:CallbackQuery,  callback_data:dict):
    await call.answer(cache_time=18)

    product_id = callback_data.get('id')
    user = call.message.chat.id
    cartController.add_cart(user,product_id)
    await  call.message.answer('Товар добавлен в  корзину.',reply_markup=nazad_korzina())


@dp.callback_query_handler(text="korz",state=None)
async def echo(call:CallbackQuery):
    await call.message.answer('<b>Для совершения заказа отправьте  свой  номер  телефона:</b>',parse_mode='HTML',reply_markup=phone)
    await Phone.ph.set()

@dp.message_handler(content_types=['contact'],state=Phone.phone_number)
async def load_contact(message: types.Message, state:FSMContext):
    async with state.proxy() as data:
        data['contact']  = message.contact.phone_number
        userController.telephone(message.chat.id,data['contact'])
        dat =  cartController.get_cart(message.chat.id)
        new_data  = []
        for i in dat:
            salom = productController.get_prod(i[1])
            new_data.append(salom)
        new_data = [new_data[i][0] for i in range(len(new_data))]
        print(new_data)
        prices  = [LabeledPrice(label=i[1],amount=i[2]) for i in  new_data]


    await message.answer('Общая цена и список всех выбранных товаров. ',reply_markup=menu_ru)
    await bot.send_invoice(message.chat.id,
                            title='Корзина',
                            description='Все выбранные товары и общая цена.',
                            provider_token=PAYMENTS_TOKEN,
                            currency='uzs',
                            prices=prices,
                            start_parameter='start',
                            payload='some_invoice')
    await state.finish()



@dp.pre_checkout_query_handler(lambda q: True)
async def  checkout_process(pre_checkout_query: PreCheckoutQuery):
    await bot.answer_pre_checkout_query(pre_checkout_query.id,ok=True)

@dp.message_handler(content_types=ContentType.SUCCESSFUL_PAYMENT)
async def pay(message: types.Message):
    cartController.del_final(message.chat.id)
    await bot.send_message(message.chat.id, 'Платеж прошел  успешно, спасибо за ваш выбор!В ближайшем  времени администратор с вами  свяжеться.')


@dp.message_handler(commands=['allusers'],user_id=admin)
async def send_welcome(message: types.Message):
    fo1 = userController.count()
    print(fo1)
    for i in fo1:
        b = i[0]
        await message.reply(f"Привет админ!\nЧисло пользователей использующих боте равно {b}.")


@dp.message_handler(commands=['reklama'],user_id = admin)
async def send_welcome(message: types.Message):
    await Send.text.set()
    await message.reply('<b>Введите  текст для рассылки: </b>',parse_mode='HTML')

@dp.message_handler(state=Send.text)
async def load_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['text'] = message.text
    await Send.next()
    await message.reply('<b>Отправьте фотографию для рассылки:  </b>',parse_mode='HTML')


@dp.message_handler(content_types=['photo'],state=Send.photo)
async def load_photo(message: types.Message, state:FSMContext):
    async with state.proxy() as data:
        data['photo'] = message.photo[0].file_id
    rek1 =   userController.reklama()
    for j in rek1:
        user_id = j[0]
        await bot.send_message(chat_id = user_id,text = f"""<b>{data['text']}</b>""",parse_mode='HTML')
    await message.answer_photo(
        photo = data['photo'],
        caption = """ """,parse_mode='HTML')
    await state.finish()


async def on_startup(_):
    # Create default db's tables
    userController.create_base()
    productController.create_base_prod()
    cartController.create_base_cart()

    # Binds custom filters
    bind_all_custom_filters(dp)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)

    # Connect to db and init controllers
    connection = sqlite3.connect('baza.db')
    db_cursor = connection.cursor()
    userController, productController, cartController = init_controllers(connection, db_cursor)

    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)