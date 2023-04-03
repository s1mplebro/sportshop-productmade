from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup,ReplyKeyboardMarkup,KeyboardButton
from aiogram.utils.callback_data import CallbackData


languag = ReplyKeyboardMarkup(
	keyboard = [
	      [
	      KeyboardButton(text="🇷🇺Русский")
	      ],
	 ],
	 resize_keyboard = True 
)
loc = ReplyKeyboardMarkup(
	keyboard = [
	      [
	      KeyboardButton(text=" 📍  Отправить геолокацию",request_location=True),
	      ],
	 ],
	 resize_keyboard = True
)
phone = ReplyKeyboardMarkup(
	keyboard = [
	      [
	      KeyboardButton(text="📞 Отправить контакт",request_contact=True),
	      ],
	 ],
	 resize_keyboard = True
)
cancel_keyboard = ReplyKeyboardMarkup(
	keyboard = [
	      [
	      KeyboardButton(text="❌ Отмена"),
	      ],
	 ],
	 resize_keyboard = True
)

menu_ru = ReplyKeyboardMarkup(
	keyboard = [
	      [
	      KeyboardButton(text="🛒 Начать новый заказ"),
	      KeyboardButton(text="✍️ Оставить отзыв")
	      ],
	      [
	      KeyboardButton(text="🤔О магазине"),
	      KeyboardButton(text="⬅️Поменять язык")
	      ],
	 ],
	  resize_keyboard = True
)

tovari = InlineKeyboardMarkup(#menu osnovnoy
 	inline_keyboard = [
 	      [
 	      InlineKeyboardButton(text="Протеины🦾",callback_data="protein"),
 	      InlineKeyboardButton(text="Жиросжигатели🔥",callback_data="jir"),
 	      ],
 	      [
 	      InlineKeyboardButton(text="Гейнеры💪",callback_data="geyner"),
 	      InlineKeyboardButton(text="Креатин🥩",callback_data="kreatin"),
 	      ],
 	      [
          InlineKeyboardButton(text="Энергетики🔋",callback_data="energetic"),
 	      InlineKeyboardButton(text="Бустер/Тестостерон🔝",callback_data="buster"),
 	      ],
 	      [
 	      InlineKeyboardButton(text="Аминокислоты🉑",callback_data="aminokislota"),
 	      InlineKeyboardButton(text="BCAA🍚",callback_data="bcaa"),
 	      ],
 	      [
 	      InlineKeyboardButton(text="Витамины🟢",callback_data="vitamin"),
 	      InlineKeyboardButton(text="Изотоник / Электролит🟦",callback_data="izotonik")
 	      ],
 	      [
 	      InlineKeyboardButton(text="L-карнитин🧃",callback_data="lkarnitin"),
 	      InlineKeyboardButton(text="Батончики🍫",callback_data="batonchik")
 	      ],
 	      [
			InlineKeyboardButton(text="Глютамин🌰",callback_data="glutamin") 	      
 	      ],
 	 ],

 )

proteins = InlineKeyboardMarkup(#menu protein
 	inline_keyboard = [
 	      [
 	      InlineKeyboardButton(text="Optimum Nutrition Platinum Hydrowhey🥇",callback_data="optm_nutrition"),
 	      
 	      ],
 	      [
 	      	InlineKeyboardButton(text="PROSTAR 100% WHEY PROTEIN🔥",callback_data="prostar1"),
 	      ],
 	      [
 	      InlineKeyboardButton(text="Whey Gold от Weider💪",callback_data="wheygold"),
 	    
 	      ],
 	      [
 	       InlineKeyboardButton(text="100% WHEY GOLD STANDARD🥩",callback_data="wheygold-1"),
 	      ],
 	      [
          InlineKeyboardButton(text="100% Casein Gold Standard🔋",callback_data="atlant"),
 	      
 	      ],
 	      [
 	      	InlineKeyboardButton(text="АТЛАНТ (креатин+глютамин)🔝",callback_data="bigwhey"),
 	      ],
 	      [
 	      InlineKeyboardButton(text="АТЛАНТ (с креатином)🉑",callback_data="carnivor"),
 	      
 	      ],
 	      [
 	      InlineKeyboardButton(text="BIG WHEY🟦",callback_data="wheyhd"),
 	      ],
 	      [
 	      InlineKeyboardButton(text="CARNIVOR от MuscleMeds🟢",callback_data="kevin"),
 	      
 	      ],
 	      [
 	      	InlineKeyboardButton(text="PURE WHEY 100% BE PERFECT NUTRITION🟣",callback_data="casein")
 	      ],
 	      [
 	      InlineKeyboardButton(text="Whey HD от BPI Sports💥",callback_data="wheyprotein"),
 	      
 	      ],
 	      [
 	      	InlineKeyboardButton(text="Rule 1 Whey Blend Chocolate Fudge 68🫡",callback_data="prostar")
 	      ],
 	      [
 	      InlineKeyboardButton(text="Levro Iso Whey 2 kg🫡",callback_data="prostarkg"),
 	      
 	      ],
 	      [
 	      InlineKeyboardButton(text="R1 Протеин Whey Blend 4,5 kg🍪",callback_data="sensation")
 	      ],
 	      [
 	      InlineKeyboardButton(text="R1 Casein Rule 1🍪",callback_data="sensationkg"),
 	      
 	      ],
 	      [
 	      	InlineKeyboardButton(text="Gat Whey Protein👾",callback_data="monsterlabs")
 	      ],
 	      [
 	      InlineKeyboardButton(text="PROSTAR 100% WHEY PROTEIN 907g🟥",callback_data="sticker"),
 	      
 	      ],

 	      [
 	      InlineKeyboardButton(text="SUPERIOR 14 - WHEY ISOLATE ISO-PRO (2.2KG)🥥",callback_data="superioriso"),
 	      
 	      ],
 	      [
 	      	InlineKeyboardButton(text="SUPERIOR 14 Superior Quattro Protein 3000G🍫",callback_data="superiorqua")
 	      ],
 	      [
 	      InlineKeyboardButton(text="Iso Sensation 93 910g⚡️",callback_data="tesla"),
 	      
 	      ],
 	      [
 	      InlineKeyboardButton(text="Iso Sensation 93 2.27kg🍓",callback_data="teslaiso")
 	      ],
 	      [
 	      InlineKeyboardButton(text="Monster Labs Whey💧",callback_data="labsmon"),
 	      
 	      ],
 	      [
 	      InlineKeyboardButton(text="Syntha-6🍓",callback_data="syntha6")
 	      ],
 	      [
			InlineKeyboardButton(text="Назад◀️",callback_data="back_to_main"),
			InlineKeyboardButton(text="Больше➡️",callback_data="more_proteinlar") 	       	      
 	      ],
 	 ],

 )

mor_proteins = InlineKeyboardMarkup(#menu protein
 	inline_keyboard = [
 	      [
 	      InlineKeyboardButton(text="WHEY Protein Pole Nutrition🥇",callback_data="whey_pole"),
 	      
 	      ],
 	      [
 	      	InlineKeyboardButton(text="Whey Gold Standatd 100 % (со стикером)🔥",callback_data="gold_standard"),
 	      ],
 	      [
 	      InlineKeyboardButton(text="Vegan Protein Tesla Nutrition💪",callback_data="vegan"),
 	    
 	      ],
 	      [
 	       InlineKeyboardButton(text="Superior 14 Whey Core Protein🥩",callback_data="whey_core"),
 	      ],
 	      [
          InlineKeyboardButton(text="Tesla Whey Charger 100🔋",callback_data="tesla_whey_charger"),
 	      
 	      ],
 	      [
 	      	InlineKeyboardButton(text="Tesla Nutrition Iso Zero 100🔝",callback_data="tesla_nutrition"),
 	      ],
 	      [
 	      InlineKeyboardButton(text="Superior 14 Hydro Whey Zero🉑",callback_data="hydro_whey"),
 	      
 	      ],
 	      [
 	      InlineKeyboardButton(text="Iso Zero 100 Tesla Nutrition🟦",callback_data="iso_tesla"),
 	      ],
 	      [
 	      InlineKeyboardButton(text="Rule1 Plant Protein🟢",callback_data="rule_plant"),
 	      
 	      ],
 	      [
 	      	InlineKeyboardButton(text="Rule1 Protein Isolate🟣",callback_data="protein_rule1")
 	      ],
 	      [
 	      InlineKeyboardButton(text="Xtend Pro Whey Isolate 826g💥",callback_data="xtendpro"),
 	      
 	      ],
 	      [
 	      	InlineKeyboardButton(text="DYMATIYZE ISO 100🫡",callback_data="dymanize")
 	      ],
 	      [
 	      InlineKeyboardButton(text="Xtend Pro Whey Isolate🫡",callback_data="xtendwhey"),
 	      
 	      ],
 	      [
 	      InlineKeyboardButton(text="Nitro Tech Whey Gold🍪",callback_data="nitro_tech")
 	      ],
 	      [
 	      InlineKeyboardButton(text="Combat 100% Whey🍪",callback_data="combat_whey"),
 	      
 	      ],
 	      [
 	      	InlineKeyboardButton(text="Elite Whey Protein👾",callback_data="elite")
 	      ],
 	      [
 	      InlineKeyboardButton(text="ULTRA WHEY PRO🟥",callback_data="ultra"),
 	      
 	      ],
 	      [
 	      	InlineKeyboardButton(text="MUTANT WHEY PROTEIN✴️",callback_data="mutant")
 	      ],
 	      [
 	      InlineKeyboardButton(text="Elite Casein от Dymatize🥥",callback_data="elite_casein"),
 	      
 	      ],
 	      [
 	      	InlineKeyboardButton(text="Combat Protein Powder🍫",callback_data="combat_powder")
 	      ],
 	      [
 	      InlineKeyboardButton(text="NITRO TECH CASEIN GOLD⚡️",callback_data="nitro_gold"),
 	      
 	      ],
 	      [
 	      InlineKeyboardButton(text="Протеин Bombbar Whey Protein (30 г)🍓",callback_data="bombbar")
 	      ],
 	      [
 	      InlineKeyboardButton(text="BADASS Nutrition, Whey Protein, 2270 г💧",callback_data="badass"),
 	      
 	      ],
 	      [
 	      InlineKeyboardButton(text="Kevin Levrone, Gold Whey, 2000 гр",callback_data="levrone"),
 	      
 	      ],
 	      [
 	      InlineKeyboardButton(text="Slow-Release Casein",callback_data="slow-rel"),
 	      
 	      ],
 	      [
 	      InlineKeyboardButton(text="Viking Empire Whey",callback_data="viking"),
 	      
 	      ],
 	      [
 	      InlineKeyboardButton(text="Fitness Authority Core Pro",callback_data="fitness"),
 	      
 	      ],
 	      [
 	      InlineKeyboardButton(text="KEVIN LEVRONE ANABOLIC ISO",callback_data="kevin_anabolic"),
 	      
 	      ],
 	      [
 	      InlineKeyboardButton(text="Impact Whey Protein",callback_data="impact"),
 	      
 	      ],
 	      [
 	      InlineKeyboardButton(text="Tesla Hydro Whey Zero",callback_data="hydra_tesla"),
 	      
 	      ],
 	      [
			InlineKeyboardButton(text="Назад🔙",callback_data="back_to_prot") 	       	      
 	      ],
 	 ],

 )


simple_queries_templates = {
	"⬅️Поменять язык": (f"<b><em>$USERNAME</em>, Выберите язык🇷🇺:  \
                        \n<em>$USERNAME</em>, Tilni tanlang🇺🇿:</b>", languag),
	
	"🇷🇺Русский": (f"<em>Сюда можно  какой то текст по типу добро  пожаловать вас приветствует бот еще  что то \
					\n \n Выберите одно из следующих: </em>", menu_ru),
	
	"❌ Отмена": (f"<b><em>Вы отменили действие</em></b>", menu_ru),

	"🤔О магазине": ('''<b>В интернет-магазине спортивного питания  Sportshop в Ташкенте🇺🇿 можно найти всё,\
	что нужно для нутритивной поддержки и профессионалам, и любителям, и начинающим\
	спортсменам, а также всем, кто следит за своим здоровьем! Не забывайте о том, что\
	спортивное питание - это здоровое питание, и у нас Вы можете купить спортивное питание\
	по доступным ценам по всему Узбекистану. У нас представлены наиболее популярные мировые\
	бренды спортивного питания, и максимально низкие цены на них! С интернет магазином\
	спортивного питания Sportshop в Узбекистане, Вы можете купить спортивное питание через\
	интернет дешево и быстро в любой точке Узбекистана.\n\nЛюбому, кто занимается \
	бодибилдингом, фитнесом, пауэрлифтингом, кроссфитом или воркаутом, профессионально\
	или только начинает – просто необходимы добавки к основному питанию, включающие в себя\
	целый витаминно-минеральный комплекс, незаменимые аминокислоты, качественные белки и\
	другие специальные добавки, которые вы можете найти в Узбекистане, а именно в нашем\
	онлайн магазине спортивного питания в Ташкенте.\n\nИ всё это Вы найдёте в нашем интернет\
	магазине Sportshop , спортивное питание для улучшения Ваших результатов в спорте – для\
	набора мышечной массы, для сгонки жира, для увеличения силы, для быстрого восстановления\
	сил, для увеличения выносливости, для борьбы со стрессом организма, для общего улучшения\
	здоровья.\n\nКупить спортивное питание, протеины и многое другое в Ташкенте Вы можете у\
	нас в интернет магазине спортивного питания Sportshop.\n\n  Спортивное питание в\
	Узбекистане, у нас есть все виды строго качественного американского спортивного питания.\
	Всё для набора массы похудения и рельефа. У нас вы можете найти абсолютно всё.\
	Вся информация по номеру +998933921192 и +998998915151 Звоните пишите\
	( + все виды меседжеров) Измениться не вопрос когда рядом ваш спортшоп.\
	@sportshopintashkent</b> \n \n НАШ ИНТЕРНЕТ МАГАЗИН  ЗДЕСЬ:\
	<a  href="https://sportshopin.uz/">КЛИКНИ</a>''', menu_ru)
}

cb = CallbackData('buy','id')
def protein_korzina():
	protein = InlineKeyboardMarkup(
		inline_keyboard = [
		[
		InlineKeyboardButton(text='Добавить в корзину🛒',callback_data='buy:1')
		],
		[
		InlineKeyboardButton(text='Назад◀️',callback_data='back_from_protein')
		],
		],
								)
	return protein
	
def protein_korzina2():
	protein2 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
		InlineKeyboardButton(text='Добавить в корзину🛒',callback_data='buy:2')
		],
		[
		InlineKeyboardButton(text='Назад◀️',callback_data='back_from_protein')
		],
		],
								)
	return protein2

def protein_korzina3():
	protein3 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
		InlineKeyboardButton(text='Добавить в корзину🛒',callback_data='buy:3')
		],
		[
		InlineKeyboardButton(text='Назад◀️',callback_data='back_from_protein')
		],
		],
								)
	return protein3

def protein_korzina4():
	protein4 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
		InlineKeyboardButton(text='Добавить в корзину🛒',callback_data='buy:4')
		],
		[
		InlineKeyboardButton(text='Назад◀️',callback_data='back_from_protein')
		],
		],
								)
	return protein4

def protein_korzina5():
	protein5 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
		InlineKeyboardButton(text='Добавить в корзину🛒',callback_data='buy:5')
		],
		[
		InlineKeyboardButton(text='Назад◀️',callback_data='back_from_protein')
		],
		],
								)
	return protein5


def protein_korzina6():
	protein6 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
		InlineKeyboardButton(text='Добавить в корзину🛒',callback_data='buy:6')
		],
		[
		InlineKeyboardButton(text='Назад◀️',callback_data='back_from_protein')
		],
		],
								)
	return protein6

def protein_korzina7():
	protein7 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
		InlineKeyboardButton(text='Добавить в корзину🛒',callback_data='buy:7')
		],
		[
		InlineKeyboardButton(text='Назад◀️',callback_data='back_from_protein')
		],
		],
								)
	return protein7


def protein_korzina8():
	protein8 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
		InlineKeyboardButton(text='Добавить в корзину🛒',callback_data='buy:8')
		],
		[
		InlineKeyboardButton(text='Назад◀️',callback_data='back_from_protein')
		],
		],
								)
	return protein8


def protein_korzina9():
	protein9 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
		InlineKeyboardButton(text='Добавить в корзину🛒',callback_data='buy:9')
		],
		[
		InlineKeyboardButton(text='Назад◀️',callback_data='back_from_protein')
		],
		],
								)
	return protein9

def protein_korzina10():
	protein10 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
		InlineKeyboardButton(text='Добавить в корзину🛒',callback_data='buy:10')
		],
		[
		InlineKeyboardButton(text='Назад◀️',callback_data='back_from_protein')
		],
		],
								)
	return protein10

def protein_korzina11():
	protein11 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
		InlineKeyboardButton(text='Добавить в корзину🛒',callback_data='buy:11')
		],
		[
		InlineKeyboardButton(text='Назад◀️',callback_data='back_from_protein')
		],
		],
								)
	return protein11 

def protein_korzina12():
	protein12 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
		InlineKeyboardButton(text='Добавить в корзину🛒',callback_data='buy:12')
		],
		[
		InlineKeyboardButton(text='Назад◀️',callback_data='back_from_protein')
		],
		],
								)
	return protein12


def protein_korzina13():
	protein13 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
		InlineKeyboardButton(text='Добавить в корзину🛒',callback_data='buy:13')
		],
		[
		InlineKeyboardButton(text='Назад◀️',callback_data='back_from_protein')
		],
		],
								)
	return protein13

def protein_korzina14():
	protein14 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
		InlineKeyboardButton(text='Добавить в корзину🛒',callback_data='buy:14')
		],
		[
		InlineKeyboardButton(text='Назад◀️',callback_data='back_from_protein')
		],
		],
								)
	return protein14

def protein_korzina15():
	protein15 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
		InlineKeyboardButton(text='Добавить в корзину🛒',callback_data='buy:15')
		],
		[
		InlineKeyboardButton(text='Назад◀️',callback_data='back_from_protein')
		],
		],
								)
	return protein15

def protein_korzina16():
	protein16 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
		InlineKeyboardButton(text='Добавить в корзину🛒',callback_data='buy:16')
		],
		[
		InlineKeyboardButton(text='Назад◀️',callback_data='back_from_protein')
		],
		],
								)
	return protein16


def protein_korzina17():
	protein17 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
		InlineKeyboardButton(text='Добавить в корзину🛒',callback_data='buy:17')
		],
		[
		InlineKeyboardButton(text='Назад◀️',callback_data='back_from_protein')
		],
		],
								)
	return protein17

def protein_korzina18():
	protein18 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
		InlineKeyboardButton(text='Добавить в корзину🛒',callback_data='buy:18')
		],
		[
		InlineKeyboardButton(text='Назад◀️',callback_data='back_from_protein')
		],
		],
								)
	return protein18

def protein_korzina19():
	protein19 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
		InlineKeyboardButton(text='Добавить в корзину🛒',callback_data='buy:19')
		],
		[
		InlineKeyboardButton(text='Назад◀️',callback_data='back_from_protein')
		],
		],
								)
	return protein19 


def protein_korzina20():
	protein20 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
		InlineKeyboardButton(text='Добавить в корзину🛒',callback_data='buy:20')
		],
		[
		InlineKeyboardButton(text='Назад◀️',callback_data='back_from_protein')
		],
		],
								)
	return protein20

def protein_korzina21():
	protein21 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
		InlineKeyboardButton(text='Добавить в корзину🛒',callback_data='buy:21')
		],
		[
		InlineKeyboardButton(text='Назад◀️',callback_data='back_from_protein')
		],
		],
								)
	return protein21 


def protein_korzina22():
	protein22 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
		InlineKeyboardButton(text='Добавить в корзину🛒',callback_data='buy:22')
		],
		[
		InlineKeyboardButton(text='Назад◀️',callback_data='back_from_protein')
		],
		],
								)
	return protein22 

def protein_korzina23():
	protein23 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
		InlineKeyboardButton(text='Добавить в корзину🛒',callback_data='buy:23')
		],
		[
		InlineKeyboardButton(text='Назад◀️',callback_data='back_from_protein')
		],
		],
								)
	return protein23  

def protein_korzina24():
	protein24 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
		InlineKeyboardButton(text='Добавить в корзину🛒',callback_data='buy:24')
		],
		[
		InlineKeyboardButton(text='Назад◀️',callback_data='back_from_protein')
		],
		],
								)
	return protein24 


def protein_korzina25():
	protein25 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
		InlineKeyboardButton(text='Добавить в корзину🛒',callback_data='buy:25')
		],
		[
		InlineKeyboardButton(text='Назад◀️',callback_data='back_from_protein')
		],
		],
								)
	return protein25 

def protein_korzina26():
	protein26 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
		InlineKeyboardButton(text='Добавить в корзину🛒',callback_data='buy:26')
		],
		[
		InlineKeyboardButton(text='Назад◀️',callback_data='back_from_protein')
		],
		],
								)
	return protein26 

def protein_korzina27():
	protein27 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
		InlineKeyboardButton(text='Добавить в корзину🛒',callback_data='buy:27')
		],
		[
		InlineKeyboardButton(text='Назад◀️',callback_data='back_from_protein')
		],
		],
								)
	return protein27 

def protein_korzina28():
	protein28 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
		InlineKeyboardButton(text='Добавить в корзину🛒',callback_data='buy:28')
		],
		[
		InlineKeyboardButton(text='Назад◀️',callback_data='back_from_protein')
		],
		],
								)
	return protein28 

def protein_korzina29():
	protein29 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
		InlineKeyboardButton(text='Добавить в корзину🛒',callback_data='buy:29')
		],
		[
		InlineKeyboardButton(text='Назад◀️',callback_data='back_from_protein')
		],
		],
								)
	return protein29 

def protein_korzina30():
	protein30 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
		InlineKeyboardButton(text='Добавить в корзину🛒',callback_data='buy:30')
		],
		[
		InlineKeyboardButton(text='Назад◀️',callback_data='back_from_protein')
		],
		],
								)
	return protein30 

def protein_korzina31():
	protein31 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
		InlineKeyboardButton(text='Добавить в корзину🛒',callback_data='buy:31')
		],
		[
		InlineKeyboardButton(text='Назад◀️',callback_data='back_from_protein')
		],
		],
								)
	return protein31

def protein_korzina32():
	protein32 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
		InlineKeyboardButton(text='Добавить в корзину🛒',callback_data='buy:32')
		],
		[
		InlineKeyboardButton(text='Назад◀️',callback_data='back_from_protein')
		],
		],
								)
	return protein32 

def protein_korzina33():
	protein33 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
		InlineKeyboardButton(text='Добавить в корзину🛒',callback_data='buy:33')
		],
		[
		InlineKeyboardButton(text='Назад◀️',callback_data='back_from_protein')
		],
		],
								)
	return protein33  

def protein_korzina34():
	protein34 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
		InlineKeyboardButton(text='Добавить в корзину🛒',callback_data='buy:34')
		],
		[
		InlineKeyboardButton(text='Назад◀️',callback_data='back_from_protein')
		],
		],
								)
	return protein34  

def protein_korzina35():
	protein35 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
		InlineKeyboardButton(text='Добавить в корзину🛒',callback_data='buy:35')
		],
		[
		InlineKeyboardButton(text='Назад◀️',callback_data='back_from_protein')
		],
		],
								)
	return protein35  

def protein_korzina36():
	protein36 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
		InlineKeyboardButton(text='Добавить в корзину🛒',callback_data='buy:36')
		],
		[
		InlineKeyboardButton(text='Назад◀️',callback_data='back_from_protein')
		],
		],
								)
	return protein36  

def protein_korzina37():
	protein37 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
		InlineKeyboardButton(text='Добавить в корзину🛒',callback_data='buy:37')
		],
		[
		InlineKeyboardButton(text='Назад◀️',callback_data='back_from_protein')
		],
		],
								)
	return protein37

def protein_korzina38():
	protein38 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
		InlineKeyboardButton(text='Добавить в корзину🛒',callback_data='buy:38')
		],
		[
		InlineKeyboardButton(text='Назад◀️',callback_data='back_from_protein')
		],
		],
								)
	return protein38  

def protein_korzina39():
	protein39 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
		InlineKeyboardButton(text='Добавить в корзину🛒',callback_data='buy:39')
		],
		[
		InlineKeyboardButton(text='Назад◀️',callback_data='back_from_protein')
		],
		],
								)
	return protein39   

def protein_korzina40():
	protein40 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
		InlineKeyboardButton(text='Добавить в корзину🛒',callback_data='buy:40')
		],
		[
		InlineKeyboardButton(text='Назад◀️',callback_data='back_from_protein')
		],
		],
								)
	return protein40 

def protein_korzina41():
	protein41 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
		InlineKeyboardButton(text='Добавить в корзину🛒',callback_data='buy:41')
		],
		[
		InlineKeyboardButton(text='Назад◀️',callback_data='back_from_protein')
		],
		],
								)
	return protein41

def protein_korzina42():
	protein42 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
		InlineKeyboardButton(text='Добавить в корзину🛒',callback_data='buy:42')
		],
		[
		InlineKeyboardButton(text='Назад◀️',callback_data='back_from_protein')
		],
		],
								)
	return protein42  

def protein_korzina43():
	protein43 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
		InlineKeyboardButton(text='Добавить в корзину🛒',callback_data='buy:43')
		],
		[
		InlineKeyboardButton(text='Назад◀️',callback_data='back_from_protein')
		],
		],
								)
	return protein43 

def protein_korzina44():
	protein44 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
		InlineKeyboardButton(text='Добавить в корзину🛒',callback_data='buy:44')
		],
		[
		InlineKeyboardButton(text='Назад◀️',callback_data='back_from_protein')
		],
		],
								)
	return protein44 

def protein_korzina45():
	protein45 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
		InlineKeyboardButton(text='Добавить в корзину🛒',callback_data='buy:45')
		],
		[
		InlineKeyboardButton(text='Назад◀️',callback_data='back_from_protein')
		],
		],
								)
	return protein45   

def protein_korzina46():
	protein46 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
		InlineKeyboardButton(text='Добавить в корзину🛒',callback_data='buy:46')
		],
		[
		InlineKeyboardButton(text='Назад◀️',callback_data='back_from_protein')
		],
		],
								)
	return protein46 

def protein_korzina47():
	protein47 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
		InlineKeyboardButton(text='Добавить в корзину🛒',callback_data='buy:47')
		],
		[
		InlineKeyboardButton(text='Назад◀️',callback_data='back_from_protein')
		],
		],
								)
	return protein47  

def protein_korzina48():
	protein48 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
		InlineKeyboardButton(text='Добавить в корзину🛒',callback_data='buy:48')
		],
		[
		InlineKeyboardButton(text='Назад◀️',callback_data='back_from_protein')
		],
		],
								)
	return protein48  

def protein_korzina49():
	protein49 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
		InlineKeyboardButton(text='Добавить в корзину🛒',callback_data='buy:49')
		],
		[
		InlineKeyboardButton(text='Назад◀️',callback_data='back_from_protein')
		],
		],
								)
	return protein49  

def protein_korzina50():
	protein50 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
		InlineKeyboardButton(text='Добавить в корзину🛒',callback_data='buy:50')
		],
		[
		InlineKeyboardButton(text='Назад◀️',callback_data='back_from_protein')
		],
		],
								)
	return protein50 

def protein_korzina51():
	protein51 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
		InlineKeyboardButton(text='Добавить в корзину🛒',callback_data='buy:51')
		],
		[
		InlineKeyboardButton(text='Назад◀️',callback_data='back_from_protein')
		],
		],
								)
	return protein51 

def protein_korzina52():
	protein52 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
		InlineKeyboardButton(text='Добавить в корзину🛒',callback_data='buy:52')
		],
		[
		InlineKeyboardButton(text='Назад◀️',callback_data='back_from_protein')
		],
		],
								)
	return protein52 

def protein_korzina53():
	protein53 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
		InlineKeyboardButton(text='Добавить в корзину🛒',callback_data='buy:53')
		],
		[
		InlineKeyboardButton(text='Назад◀️',callback_data='back_from_protein')
		],
		],
								)
	return protein53 


########
def jirfire1():
	jir2 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
		InlineKeyboardButton(text='Добавить в корзину🛒',callback_data='buy:55')
		],
		[
		InlineKeyboardButton(text='Назад◀️',callback_data='back_to_jir')
		],
		],
								)
	return jir2

def jirfire2():
	jir2 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
		InlineKeyboardButton(text='Добавить в корзину🛒',callback_data='buy:56')
		],
		[
		InlineKeyboardButton(text='Назад◀️',callback_data='back_to_jir')
		],
		],
								)
	return jir2

def jirfire3():
	jir3 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
		InlineKeyboardButton(text='Добавить в корзину🛒',callback_data='buy:57')
		],
		[
		InlineKeyboardButton(text='Назад◀️',callback_data='back_to_jir')
		],
		],
								)
	return jir3

def jirfire4():
	jir4 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
		InlineKeyboardButton(text='Добавить в корзину🛒',callback_data='buy:58')
		],
		[
		InlineKeyboardButton(text='Назад◀️',callback_data='back_to_jir')
		],
		],
								)
	return jir4
def jirfire5():
	jir5 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
		InlineKeyboardButton(text='Добавить в корзину🛒',callback_data='buy:59')
		],
		[
		InlineKeyboardButton(text='Назад◀️',callback_data='back_to_jir')
		],
		],
								)
	return jir5
def jirfire6():
	jir6 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
		InlineKeyboardButton(text='Добавить в корзину🛒',callback_data='buy:60')
		],
		[
		InlineKeyboardButton(text='Назад◀️',callback_data='back_to_jir')
		],
		],
								)
	return jir6
def jirfire7():
	jir7 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
		InlineKeyboardButton(text='Добавить в корзину🛒',callback_data='buy:61')
		],
		[
		InlineKeyboardButton(text='Назад◀️',callback_data='back_to_jir')
		],
		],
								)
	return jir7
def jirfire8():
	jir8 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
		InlineKeyboardButton(text='Добавить в корзину🛒',callback_data='buy:62')
		],
		[
		InlineKeyboardButton(text='Назад◀️',callback_data='back_to_jir')
		],
		],
								)
	return jir8
def jirfire9():
	jir9 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
		InlineKeyboardButton(text='Добавить в корзину🛒',callback_data='buy:63')
		],
		[
		InlineKeyboardButton(text='Назад◀️',callback_data='back_to_jir')
		],
		],
								)
	return jir9

def jirfire10():
	jir10 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
		InlineKeyboardButton(text='Добавить в корзину🛒',callback_data='buy:64')
		],
		[
		InlineKeyboardButton(text='Назад◀️',callback_data='back_to_jir')
		],
		],
								)
	return jir10

def jirfire11():
	jir11 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
		InlineKeyboardButton(text='Добавить в корзину🛒',callback_data='buy:65')
		],
		[
		InlineKeyboardButton(text='Назад◀️',callback_data='back_to_jir')
		],
		],
								)
	return jir11

def jirfire12():
	jir12 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
		InlineKeyboardButton(text='Добавить в корзину🛒',callback_data='buy:66')
		],
		[
		InlineKeyboardButton(text='Назад◀️',callback_data='back_to_jir')
		],
		],
								)
	return jir12

def jirfire13():
	jir13 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
		InlineKeyboardButton(text='Добавить в корзину🛒',callback_data='buy:67')
		],
		[
		InlineKeyboardButton(text='Назад◀️',callback_data='back_to_jir')
		],
		],
								)
	return jir13

def jirfire14():
	jir14 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
		InlineKeyboardButton(text='Добавить в корзину🛒',callback_data='buy:68')
		],
		[
		InlineKeyboardButton(text='Назад◀️',callback_data='back_to_jir')
		],
		],
								)
	return jir14

def jirfire15():
	jir15 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
		InlineKeyboardButton(text='Добавить в корзину🛒',callback_data='buy:69')
		],
		[
		InlineKeyboardButton(text='Назад◀️',callback_data='back_to_jir')
		],
		],
								)
	return jir15

def jirfire16():
	jir16 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
		InlineKeyboardButton(text='Добавить в корзину🛒',callback_data='buy:70')
		],
		[
		InlineKeyboardButton(text='Назад◀️',callback_data='back_to_jir')
		],
		],
								)
	return jir16

def jirfire17():
	jir17 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
		InlineKeyboardButton(text='Добавить в корзину🛒',callback_data='buy:71')
		],
		[
		InlineKeyboardButton(text='Назад◀️',callback_data='back_to_jir')
		],
		],
								)
	return jir17

def jirfire18():
	jir18 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
		InlineKeyboardButton(text='Добавить в корзину🛒',callback_data='buy:72')
		],
		[
		InlineKeyboardButton(text='Назад◀️',callback_data='back_to_jir')
		],
		],
								)
	return jir18

def jirfire19():
	jir19 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
		InlineKeyboardButton(text='Добавить в корзину🛒',callback_data='buy:73')
		],
		[
		InlineKeyboardButton(text='Назад◀️',callback_data='back_to_jir')
		],
		],
								)
	return jir19

def jirfire20():
	jir20 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
		InlineKeyboardButton(text='Добавить в корзину🛒',callback_data='buy:74')
		],
		[
		InlineKeyboardButton(text='Назад◀️',callback_data='back_to_jir')
		],
		],
								)
	return jir20

def jirfire21():
	jir21 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
		InlineKeyboardButton(text='Добавить в корзину🛒',callback_data='buy:75')
		],
		[
		InlineKeyboardButton(text='Назад◀️',callback_data='back_to_jir')
		],
		],
								)
	return jir21

def jirfire22():
	jir22 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
		InlineKeyboardButton(text='Добавить в корзину🛒',callback_data='buy:76')
		],
		[
		InlineKeyboardButton(text='Назад◀️',callback_data='back_to_jir')
		],
		],
								)
	return jir22

def jirfire23():
	jir23 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
		InlineKeyboardButton(text='Добавить в корзину🛒',callback_data='buy:77')
		],
		[
		InlineKeyboardButton(text='Назад◀️',callback_data='back_to_jir')
		],
		],
								)
	return jir23

def jirfire24():
	jir24 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
		InlineKeyboardButton(text='Добавить в корзину🛒',callback_data='buy:78')
		],
		[
		InlineKeyboardButton(text='Назад◀️',callback_data='back_to_jir')
		],
		],
								)
	return jir24

def jirfire25():
	jir25 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
		InlineKeyboardButton(text='Добавить в корзину🛒',callback_data='buy:79')
		],
		[
		InlineKeyboardButton(text='Назад◀️',callback_data='back_to_jir')
		],
		],
								)
	return jir25

def jirfire26():
	jir26 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
		InlineKeyboardButton(text='Добавить в корзину🛒',callback_data='buy:80')
		],
		[
		InlineKeyboardButton(text='Назад◀️',callback_data='back_to_jir')
		],
		],
								)
	return jir26

def jirfire27():
	jir27 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
		InlineKeyboardButton(text='Добавить в корзину🛒',callback_data='buy:81')
		],
		[
		InlineKeyboardButton(text='Назад◀️',callback_data='back_to_jir')
		],
		],
								)
	return jir27

def jirfire28():
	jir28 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
		InlineKeyboardButton(text='Добавить в корзину🛒',callback_data='buy:82')
		],
		[
		InlineKeyboardButton(text='Назад◀️',callback_data='back_to_jir')
		],
		],
								)
	return jir28  

def jirfire29():
	jir29 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
		InlineKeyboardButton(text='Добавить в корзину🛒',callback_data='buy:83')
		],
		[
		InlineKeyboardButton(text='Назад◀️',callback_data='back_to_jir')
		],
		],
								)
	return jir29

def jirfire30():
	jir30 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
		InlineKeyboardButton(text='Добавить в корзину🛒',callback_data='buy:84')
		],
		[
		InlineKeyboardButton(text='Назад◀️',callback_data='back_to_jir')
		],
		],
								)
	return jir30

def jirfire31():
	jir31 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
		InlineKeyboardButton(text='Добавить в корзину🛒',callback_data='buy:85')
		],
		[
		InlineKeyboardButton(text='Назад◀️',callback_data='back_to_jir')
		],
		],
								)
	return jir31

def jirfire32():
	jir32 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
		InlineKeyboardButton(text='Добавить в корзину🛒',callback_data='buy:86')
		],
		[
		InlineKeyboardButton(text='Назад◀️',callback_data='back_to_jir')
		],
		],
								)
	return jir32

def jirfire33():
	jir33 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
		InlineKeyboardButton(text='Добавить в корзину🛒',callback_data='buy:87')
		],
		[
		InlineKeyboardButton(text='Назад◀️',callback_data='back_to_jir')
		],
		],
								)
	return jir33

def jirfire34():
	jir34 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
		InlineKeyboardButton(text='Добавить в корзину🛒',callback_data='buy:88')
		],
		[
		InlineKeyboardButton(text='Назад◀️',callback_data='back_to_jir')
		],
		],
								)
	return jir34

def jirfire35():
	jir35 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
		InlineKeyboardButton(text='Добавить в корзину🛒',callback_data='buy:89')
		],
		[
		InlineKeyboardButton(text='Назад◀️',callback_data='back_to_jir')
		],
		],
								)
	return jir35

def jirfire36():
	jir36 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
		InlineKeyboardButton(text='Добавить в корзину🛒',callback_data='buy:90')
		],
		[
		InlineKeyboardButton(text='Назад◀️',callback_data='back_to_jir')
		],
		],
								)
	return jir36

def jirfire37():
	jir37 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
		InlineKeyboardButton(text='Добавить в корзину🛒',callback_data='buy:91')
		],
		[
		InlineKeyboardButton(text='Назад◀️',callback_data='back_to_jir')
		],
		],
								)
	return jir37

def jirfire38():
	jir38 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
		InlineKeyboardButton(text='Добавить в корзину🛒',callback_data='buy:92')
		],
		[
		InlineKeyboardButton(text='Назад◀️',callback_data='back_to_jir')
		],
		],
								)
	return jir38

def jirfire39():
	jir39 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
		InlineKeyboardButton(text='Добавить в корзину🛒',callback_data='buy:93')
		],
		[
		InlineKeyboardButton(text='Назад◀️',callback_data='back_to_jir')
		],
		],
								)
	return jir39

def geynerr1():
	iysgeynerrr1 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
		InlineKeyboardButton(text='Добавить в корзину🛒',callback_data='buy:94')
		],
		[
		InlineKeyboardButton(text='Назад◀️',callback_data='back_to_jir')
		],
		],
								)
	return iysgeynerrr1

def geynerr2():
	iysgeynerrr2 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
		InlineKeyboardButton(text='Добавить в корзину🛒',callback_data='buy:95')
		],
		[
		InlineKeyboardButton(text='Назад◀️',callback_data='back_to_jir')
		],
		],
								)
	return iysgeynerrr2

def geynerr3():
	iysgeynerrr3 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
		InlineKeyboardButton(text='Добавить в корзину🛒',callback_data='buy:96')
		],
		[
		InlineKeyboardButton(text='Назад◀️',callback_data='back_to_jir')
		],
		],
								)
	return iysgeynerrr3

def geynerr4():
	iysgeynerrr4 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
		InlineKeyboardButton(text='Добавить в корзину🛒',callback_data='buy:97')
		],
		[
		InlineKeyboardButton(text='Назад◀️',callback_data='back_to_jir')
		],
		],
								)
	return iysgeynerrr4

def geynerr5():
	iysgeynerrr5 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
		InlineKeyboardButton(text='Добавить в корзину🛒',callback_data='buy:98')
		],
		[
		InlineKeyboardButton(text='Назад◀️',callback_data='back_to_jir')
		],
		],
								)
	return iysgeynerrr5

def geynerr6():
	iysgeynerrr6 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
		InlineKeyboardButton(text='Добавить в корзину🛒',callback_data='buy:99')
		],
		[
		InlineKeyboardButton(text='Назад◀️',callback_data='back_to_jir')
		],
		],
								)
	return iysgeynerrr6

def geynerr7():
	iysgeynerrr7 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
		InlineKeyboardButton(text='Добавить в корзину🛒',callback_data='buy:100')
		],
		[
		InlineKeyboardButton(text='Назад◀️',callback_data='back_to_jir')
		],
		],
								)
	return iysgeynerrr7

def geynerr8():
	iysgeynerrr8 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
		InlineKeyboardButton(text='Добавить в корзину🛒',callback_data='buy:101')
		],
		[
		InlineKeyboardButton(text='Назад◀️',callback_data='back_to_jir')
		],
		],
								)
	return iysgeynerrr8

def geynerr9():
	iysgeynerrr9 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
		InlineKeyboardButton(text='Добавить в корзину🛒',callback_data='buy:102')
		],
		[
		InlineKeyboardButton(text='Назад◀️',callback_data='back_to_jir')
		],
		],
								)
	return iysgeynerrr9

def geynerr10():
	iysgeynerrr10 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
		InlineKeyboardButton(text='Добавить в корзину🛒',callback_data='buy:103')
		],
		[
		InlineKeyboardButton(text='Назад◀️',callback_data='back_to_jir')
		],
		],
								)
	return iysgeynerrr10

def geynerr11():
	iysgeynerrr11 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
		InlineKeyboardButton(text='Добавить в корзину🛒',callback_data='buy:104')
		],
		[
		InlineKeyboardButton(text='Назад◀️',callback_data='back_to_jir')
		],
		],
								)
	return iysgeynerrr11

def geynerr12():
	iysgeynerrr12 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
		InlineKeyboardButton(text='Добавить в корзину🛒',callback_data='buy:105')
		],
		[
		InlineKeyboardButton(text='Назад◀️',callback_data='back_to_jir')
		],
		],
								)
	return iysgeynerrr12

def geynerr13():
	iysgeynerrr13 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
		InlineKeyboardButton(text='Добавить в корзину🛒',callback_data='buy:106')
		],
		[
		InlineKeyboardButton(text='Назад◀️',callback_data='back_to_jir')
		],
		],
								)
	return iysgeynerrr13

def geynerr14():
	iysgeynerrr14 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
		InlineKeyboardButton(text='Добавить в корзину🛒',callback_data='buy:107')
		],
		[
		InlineKeyboardButton(text='Назад◀️',callback_data='back_to_jir')
		],
		],
								)
	return iysgeynerrr14

def geynerr15():
	iysgeynerrr15 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
		InlineKeyboardButton(text='Добавить в корзину🛒',callback_data='buy:108')
		],
		[
		InlineKeyboardButton(text='Назад◀️',callback_data='back_to_jir')
		],
		],
								)
	return iysgeynerrr15

def geynerr16():
	iysgeynerrr16 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
		InlineKeyboardButton(text='Добавить в корзину🛒',callback_data='buy:109')
		],
		[
		InlineKeyboardButton(text='Назад◀️',callback_data='back_to_jir')
		],
		],
								)
	return iysgeynerrr16

def geynerr17():
	iysgeynerrr17 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
		InlineKeyboardButton(text='Добавить в корзину🛒',callback_data='buy:110')
		],
		[
		InlineKeyboardButton(text='Назад◀️',callback_data='back_to_jir')
		],
		],
								)
	return iysgeynerrr17

def geynerr18():
	iysgeynerrr18 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
		InlineKeyboardButton(text='Добавить в корзину🛒',callback_data='buy:111')
		],
		[
		InlineKeyboardButton(text='Назад◀️',callback_data='back_to_jir')
		],
		],
								)
	return iysgeynerrr18

def geynerr19():
	iysgeynerrr19 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
		InlineKeyboardButton(text='Добавить в корзину🛒',callback_data='buy:112')
		],
		[
		InlineKeyboardButton(text='Назад◀️',callback_data='back_to_jir')
		],
		],
								)
	return iysgeynerrr19

def geynerr20():
	iysgeynerrr20 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
		InlineKeyboardButton(text='Добавить в корзину🛒',callback_data='buy:113')
		],
		[
		InlineKeyboardButton(text='Назад◀️',callback_data='back_to_jir')
		],
		],
								)
	return iysgeynerrr20

def geynerr21():
	iysgeynerrr21 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
		InlineKeyboardButton(text='Добавить в корзину🛒',callback_data='buy:114')
		],
		[
		InlineKeyboardButton(text='Назад◀️',callback_data='back_to_jir')
		],
		],
								)
	return iysgeynerrr21

def geynerr22():
	iysgeynerrr22 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
		InlineKeyboardButton(text='Добавить в корзину🛒',callback_data='buy:115')
		],
		[
		InlineKeyboardButton(text='Назад◀️',callback_data='back_to_jir')
		],
		],
								)
	return iysgeynerrr22

def geynerr23():
	iysgeynerrr23 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
		InlineKeyboardButton(text='Добавить в корзину🛒',callback_data='buy:116')
		],
		[
		InlineKeyboardButton(text='Назад◀️',callback_data='back_to_jir')
		],
		],
								)
	return iysgeynerrr23

def geynerr24():
	iysgeynerrr24 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
		InlineKeyboardButton(text='Добавить в корзину🛒',callback_data='buy:117')
		],
		[
		InlineKeyboardButton(text='Назад◀️',callback_data='back_to_jir')
		],
		],
								)
	return iysgeynerrr24

def geynerr25():
	iysgeynerrr25 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
		InlineKeyboardButton(text='Добавить в корзину🛒',callback_data='buy:118')
		],
		[
		InlineKeyboardButton(text='Назад◀️',callback_data='back_to_jir')
		],
		],
								)
	return iysgeynerrr25

def geynerr26():
	iysgeynerrr26 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
		InlineKeyboardButton(text='Добавить в корзину🛒',callback_data='buy:119')
		],
		[
		InlineKeyboardButton(text='Назад◀️',callback_data='back_to_jir')
		],
		],
								)
	return iysgeynerrr26

def geynerr27():
	iysgeynerrr27 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
		InlineKeyboardButton(text='Добавить в корзину🛒',callback_data='buy:120')
		],
		[
		InlineKeyboardButton(text='Назад◀️',callback_data='back_to_jir')
		],
		],
								)
	return iysgeynerrr27

def geynerr28():
	iysgeynerrr28 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
		InlineKeyboardButton(text='Добавить в корзину🛒',callback_data='buy:121')
		],
		[
		InlineKeyboardButton(text='Назад◀️',callback_data='back_to_jir')
		],
		],
								)
	return iysgeynerrr28

def geynerr29():
	iysgeynerrr29 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
		InlineKeyboardButton(text='Добавить в корзину🛒',callback_data='buy:122')
		],
		[
		InlineKeyboardButton(text='Назад◀️',callback_data='back_to_jir')
		],
		],
								)
	return iysgeynerrr29

def geynerr30():
	iysgeynerrr30 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
		InlineKeyboardButton(text='Добавить в корзину🛒',callback_data='buy:123')
		],
		[
		InlineKeyboardButton(text='Назад◀️',callback_data='back_to_jir')
		],
		],
								)
	return iysgeynerrr30

def geynerr31():
	iysgeynerrr31 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
		InlineKeyboardButton(text='Добавить в корзину🛒',callback_data='buy:124')
		],
		[
		InlineKeyboardButton(text='Назад◀️',callback_data='back_to_jir')
		],
		],
								)
	return iysgeynerrr31

def geynerr32():
	iysgeynerrr32 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
		InlineKeyboardButton(text='Добавить в корзину🛒',callback_data='buy:125')
		],
		[
		InlineKeyboardButton(text='Назад◀️',callback_data='back_to_jir')
		],
		],
								)
	return iysgeynerrr32

def geynerr33():
	iysgeynerrr33 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
		InlineKeyboardButton(text='Добавить в корзину🛒',callback_data='buy:126')
		],
		[
		InlineKeyboardButton(text='Назад◀️',callback_data='back_to_jir')
		],
		],
								)
	return iysgeynerrr33

def geynerr34():
	iysgeynerrr34 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
		InlineKeyboardButton(text='Добавить в корзину🛒',callback_data='buy:127')
		],
		[
		InlineKeyboardButton(text='Назад◀️',callback_data='back_to_jir')
		],
		],
								)
	return iysgeynerrr34

def geynerr35():
	iysgeynerrr35 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
		InlineKeyboardButton(text='Добавить в корзину🛒',callback_data='buy:128')
		],
		[
		InlineKeyboardButton(text='Назад◀️',callback_data='back_to_jir')
		],
		],
								)
	return iysgeynerrr35

def geynerr36():
	iysgeynerrr31 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
		InlineKeyboardButton(text='Добавить в корзину🛒',callback_data='buy:129')
		],
		[
		InlineKeyboardButton(text='Назад◀️',callback_data='back_to_jir')
		],
		],
								)
	return iysgeynerrr31

def geynerr37():
	iysgeynerrr37 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
		InlineKeyboardButton(text='Добавить в корзину🛒',callback_data='buy:130')
		],
		[
		InlineKeyboardButton(text='Назад◀️',callback_data='back_to_jir')
		],
		],
								)
	return iysgeynerrr37

def geynerr38():
	iysgeynerrr38 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
		InlineKeyboardButton(text='Добавить в корзину🛒',callback_data='buy:131')
		],
		[
		InlineKeyboardButton(text='Назад◀️',callback_data='back_to_jir')
		],
		],
								)
	return iysgeynerrr38

def geynerr39():
	iysgeynerrr39 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
		InlineKeyboardButton(text='Добавить в корзину🛒',callback_data='buy:132')
		],
		[
		InlineKeyboardButton(text='Назад◀️',callback_data='back_to_jir')
		],
		],
								)
	return iysgeynerrr39

def creat1():
	kreatin1 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
		InlineKeyboardButton(text='Добавить в корзину🛒',callback_data='buy:133')
		],
		[
		InlineKeyboardButton(text='Назад◀️',callback_data='back_to_jir')
		],
		],
								)
	return kreatin1

def creat2():
	kreatin2 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
		InlineKeyboardButton(text='Добавить в корзину🛒',callback_data='buy:134')
		],
		[
		InlineKeyboardButton(text='Назад◀️',callback_data='back_to_jir')
		],
		],
								)
	return kreatin2

def creat3():
	kreatin3 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
		InlineKeyboardButton(text='Добавить в корзину🛒',callback_data='buy:135')
		],
		[
		InlineKeyboardButton(text='Назад◀️',callback_data='back_to_jir')
		],
		],
								)
	return kreatin3

def creat4():
	kreatin4 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
		InlineKeyboardButton(text='Добавить в корзину🛒',callback_data='buy:136')
		],
		[
		InlineKeyboardButton(text='Назад◀️',callback_data='back_to_jir')
		],
		],
								)
	return kreatin4

def creat5():
	kreatin5 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
		InlineKeyboardButton(text='Добавить в корзину🛒',callback_data='buy:137')
		],
		[
		InlineKeyboardButton(text='Назад◀️',callback_data='back_to_jir')
		],
		],
								)
	return kreatin5

def creat6():
	kreatin6 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
		InlineKeyboardButton(text='Добавить в корзину🛒',callback_data='buy:138')
		],
		[
		InlineKeyboardButton(text='Назад◀️',callback_data='back_to_jir')
		],
		],
								)
	return kreatin6

def creat7():
	kreatin7 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
		InlineKeyboardButton(text='Добавить в корзину🛒',callback_data='buy:139')
		],
		[
		InlineKeyboardButton(text='Назад◀️',callback_data='back_to_jir')
		],
		],
								)
	return kreatin7

def creat8():
	kreatin8 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
		InlineKeyboardButton(text='Добавить в корзину🛒',callback_data='buy:140')
		],
		[
		InlineKeyboardButton(text='Назад◀️',callback_data='back_to_jir')
		],
		],
								)
	return kreatin8

def creat9():
	kreatin9 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
		InlineKeyboardButton(text='Добавить в корзину🛒',callback_data='buy:141')
		],
		[
		InlineKeyboardButton(text='Назад◀️',callback_data='back_to_jir')
		],
		],
								)
	return kreatin9

def creat10():
	kreatin10 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
		InlineKeyboardButton(text='Добавить в корзину🛒',callback_data='buy:142')
		],
		[
		InlineKeyboardButton(text='Назад◀️',callback_data='back_to_jir')
		],
		],
								)
	return kreatin10

def creat11():
	kreatin11 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
		InlineKeyboardButton(text='Добавить в корзину🛒',callback_data='buy:143')
		],
		[
		InlineKeyboardButton(text='Назад◀️',callback_data='back_to_jir')
		],
		],
								)
	return kreatin11

def creat12():
	kreatin12 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
		InlineKeyboardButton(text='Добавить в корзину🛒',callback_data='buy:144')
		],
		[
		InlineKeyboardButton(text='Назад◀️',callback_data='back_to_jir')
		],
		],
								)
	return kreatin12

def creat13():
	kreatin13 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
		InlineKeyboardButton(text='Добавить в корзину🛒',callback_data='buy:145')
		],
		[
		InlineKeyboardButton(text='Назад◀️',callback_data='back_to_jir')
		],
		],
								)
	return kreatin13

def creat14():
	kreatin14 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
		InlineKeyboardButton(text='Добавить в корзину🛒',callback_data='buy:146')
		],
		[
		InlineKeyboardButton(text='Назад◀️',callback_data='back_to_jir')
		],
		],
								)
	return kreatin14

def creat15():
	kreatin15 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
		InlineKeyboardButton(text='Добавить в корзину🛒',callback_data='buy:147')
		],
		[
		InlineKeyboardButton(text='Назад◀️',callback_data='back_to_jir')
		],
		],
								)
	return kreatin15

def creat16():
	kreatin16 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
		InlineKeyboardButton(text='Добавить в корзину🛒',callback_data='buy:148')
		],
		[
		InlineKeyboardButton(text='Назад◀️',callback_data='back_to_jir')
		],
		],
								)
	return kreatin16

def creat17():
	kreatin17 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
		InlineKeyboardButton(text='Добавить в корзину🛒',callback_data='buy:149')
		],
		[
		InlineKeyboardButton(text='Назад◀️',callback_data='back_to_jir')
		],
		],
								)
	return kreatin17

def creat18():
	kreatin18 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
		InlineKeyboardButton(text='Добавить в корзину🛒',callback_data='buy:150')
		],
		[
		InlineKeyboardButton(text='Назад◀️',callback_data='back_to_jir')
		],
		],
								)
	return kreatin18

def creat19():
	kreatin19 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
		InlineKeyboardButton(text='Добавить в корзину🛒',callback_data='buy:151')
		],
		[
		InlineKeyboardButton(text='Назад◀️',callback_data='back_to_jir')
		],
		],
								)
	return kreatin19

def creat20():
	kreatin20 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
		InlineKeyboardButton(text='Добавить в корзину🛒',callback_data='buy:152')
		],
		[
		InlineKeyboardButton(text='Назад◀️',callback_data='back_to_jir')
		],
		],
								)
	return kreatin20

def creat21():
	kreatin21 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
		InlineKeyboardButton(text='Добавить в корзину🛒',callback_data='buy:153')
		],
		[
		InlineKeyboardButton(text='Назад◀️',callback_data='back_to_jir')
		],
		],
								)
	return kreatin21

def creat22():
	kreatin22 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
		InlineKeyboardButton(text='Добавить в корзину🛒',callback_data='buy:154')
		],
		[
		InlineKeyboardButton(text='Назад◀️',callback_data='back_to_jir')
		],
		],
								)
	return kreatin22

def creat23():
	kreatin22 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
		InlineKeyboardButton(text='Добавить в корзину🛒',callback_data='buy:155')
		],
		[
		InlineKeyboardButton(text='Назад◀️',callback_data='back_to_jir')
		],
		],
								)
	return kreatin22

def creat24():
	kreatin22 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
		InlineKeyboardButton(text='Добавить в корзину🛒',callback_data='buy:156')
		],
		[
		InlineKeyboardButton(text='Назад◀️',callback_data='back_to_jir')
		],
		],
								)
	return kreatin22

def creat25():
	kreatin22 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
		InlineKeyboardButton(text='Добавить в корзину🛒',callback_data='buy:157')
		],
		[
		InlineKeyboardButton(text='Назад◀️',callback_data='back_to_jir')
		],
		],
								)
	return kreatin22

def creat26():
	kreatin22 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
		InlineKeyboardButton(text='Добавить в корзину🛒',callback_data='buy:158')
		],
		[
		InlineKeyboardButton(text='Назад◀️',callback_data='back_to_jir')
		],
		],
								)
	return kreatin22

def creat27():
	kreatin22 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
		InlineKeyboardButton(text='Добавить в корзину🛒',callback_data='buy:159')
		],
		[
		InlineKeyboardButton(text='Назад◀️',callback_data='back_to_jir')
		],
		],
								)
	return kreatin22

def creat28():
	kreatin22 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
		InlineKeyboardButton(text='Добавить в корзину🛒',callback_data='buy:160')
		],
		[
		InlineKeyboardButton(text='Назад◀️',callback_data='back_to_jir')
		],
		],
								)
	return kreatin22

def creat29():
	kreatin22 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
		InlineKeyboardButton(text='Добавить в корзину🛒',callback_data='buy:161')
		],
		[
		InlineKeyboardButton(text='Назад◀️',callback_data='back_to_jir')
		],
		],
								)
	return kreatin22

def enr1():
	energa = InlineKeyboardMarkup(
		inline_keyboard = [
		[
		InlineKeyboardButton(text='Добавить в корзину🛒',callback_data='buy:162')
		],
		[
		InlineKeyboardButton(text='Назад◀️',callback_data='back_to_jir')
		],
		],
								)
	return energa

def enr2():
	energa = InlineKeyboardMarkup(
		inline_keyboard = [
		[
		InlineKeyboardButton(text='Добавить в корзину🛒',callback_data='buy:163')
		],
		[
		InlineKeyboardButton(text='Назад◀️',callback_data='back_to_jir')
		],
		],
								)
	return energa

def enr3():
	energa = InlineKeyboardMarkup(
		inline_keyboard = [
		[
		InlineKeyboardButton(text='Добавить в корзину🛒',callback_data='buy:164')
		],
		[
		InlineKeyboardButton(text='Назад◀️',callback_data='back_to_jir')
		],
		],
								)
	return energa

def enr4():
	energa = InlineKeyboardMarkup(
		inline_keyboard = [
		[
		InlineKeyboardButton(text='Добавить в корзину🛒',callback_data='buy:165')
		],
		[
		InlineKeyboardButton(text='Назад◀️',callback_data='back_to_jir')
		],
		],
								)
	return energa

def enr5():
	energa = InlineKeyboardMarkup(
		inline_keyboard = [
		[
		InlineKeyboardButton(text='Добавить в корзину🛒',callback_data='buy:166')
		],
		[
		InlineKeyboardButton(text='Назад◀️',callback_data='back_to_jir')
		],
		],
								)
	return energa

def enr6():
	energa = InlineKeyboardMarkup(
		inline_keyboard = [
		[
		InlineKeyboardButton(text='Добавить в корзину🛒',callback_data='buy:167')
		],
		[
		InlineKeyboardButton(text='Назад◀️',callback_data='back_to_jir')
		],
		],
								)
	return energa

def enr7():
	energa = InlineKeyboardMarkup(
		inline_keyboard = [
		[
		InlineKeyboardButton(text='Добавить в корзину🛒',callback_data='buy:168')
		],
		[
		InlineKeyboardButton(text='Назад◀️',callback_data='back_to_jir')
		],
		],
								)
	return energa

def enr8():
	energa = InlineKeyboardMarkup(
		inline_keyboard = [
		[
		InlineKeyboardButton(text='Добавить в корзину🛒',callback_data='buy:169')
		],
		[
		InlineKeyboardButton(text='Назад◀️',callback_data='back_to_jir')
		],
		],
								)
	return energa

def enr9():
	energa = InlineKeyboardMarkup(
		inline_keyboard = [
		[
		InlineKeyboardButton(text='Добавить в корзину🛒',callback_data='buy:170')
		],
		[
		InlineKeyboardButton(text='Назад◀️',callback_data='back_to_jir')
		],
		],
								)
	return energa

def enr10():
	energa = InlineKeyboardMarkup(
		inline_keyboard = [
		[
		InlineKeyboardButton(text='Добавить в корзину🛒',callback_data='buy:171')
		],
		[
		InlineKeyboardButton(text='Назад◀️',callback_data='back_to_jir')
		],
		],
								)
	return energa

def enr11():
	energa = InlineKeyboardMarkup(
		inline_keyboard = [
		[
		InlineKeyboardButton(text='Добавить в корзину🛒',callback_data='buy:172')
		],
		[
		InlineKeyboardButton(text='Назад◀️',callback_data='back_to_jir')
		],
		],
								)
	return energa

def enr12():
	energa = InlineKeyboardMarkup(
		inline_keyboard = [
		[
		InlineKeyboardButton(text='Добавить в корзину🛒',callback_data='buy:173')
		],
		[
		InlineKeyboardButton(text='Назад◀️',callback_data='back_to_jir')
		],
		],
								)
	return energa

def enr13():
	energa = InlineKeyboardMarkup(
		inline_keyboard = [
		[
		InlineKeyboardButton(text='Добавить в корзину🛒',callback_data='buy:174')
		],
		[
		InlineKeyboardButton(text='Назад◀️',callback_data='back_to_jir')
		],
		],															
					)
	return energa

def bbst1():
	bbst1 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
		InlineKeyboardButton(text='Добавить в корзину🛒',callback_data='buy:175')
		],
		[
		InlineKeyboardButton(text='Назад◀️',callback_data='back_to_jir')
		],
		],
								)
	return bbst1

def bbst2():
	bbst1 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
		InlineKeyboardButton(text='Добавить в корзину🛒',callback_data='buy:176')
		],
		[
		InlineKeyboardButton(text='Назад◀️',callback_data='back_to_jir')
		],
		],
								)
	return bbst1

def bbst3():
	bbst1 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
		InlineKeyboardButton(text='Добавить в корзину🛒',callback_data='buy:177')
		],
		[
		InlineKeyboardButton(text='Назад◀️',callback_data='back_to_jir')
		],
		],
								)
	return bbst1

def bbst4():
	bbst1 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
		InlineKeyboardButton(text='Добавить в корзину🛒',callback_data='buy:178')
		],
		[
		InlineKeyboardButton(text='Назад◀️',callback_data='back_to_jir')
		],
		],
								)
	return bbst1

def bbst5():
	bbst1 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
		InlineKeyboardButton(text='Добавить в корзину🛒',callback_data='buy:179')
		],
		[
		InlineKeyboardButton(text='Назад◀️',callback_data='back_to_jir')
		],
		],
								)
	return bbst1

def bbst6():
	bbst1 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
		InlineKeyboardButton(text='Добавить в корзину🛒',callback_data='buy:180')
		],
		[
		InlineKeyboardButton(text='Назад◀️',callback_data='back_to_jir')
		],
		],
								)
	return bbst1

def bbst7():
	bbst1 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
		InlineKeyboardButton(text='Добавить в корзину🛒',callback_data='buy:181')
		],
		[
		InlineKeyboardButton(text='Назад◀️',callback_data='back_to_jir')
		],
		],
								)
	return bbst1

def bbst8():
	bbst1 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
		InlineKeyboardButton(text='Добавить в корзину🛒',callback_data='buy:182')
		],
		[
		InlineKeyboardButton(text='Назад◀️',callback_data='back_to_jir')
		],
		],
								)
	return bbst1

def bbst9():
	bbst1 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
		InlineKeyboardButton(text='Добавить в корзину🛒',callback_data='buy:183')
		],
		[
		InlineKeyboardButton(text='Назад◀️',callback_data='back_to_jir')
		],
		],
								)
	return bbst1

def bbst10():
	bbst1 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
		InlineKeyboardButton(text='Добавить в корзину🛒',callback_data='buy:184')
		],
		[
		InlineKeyboardButton(text='Назад◀️',callback_data='back_to_jir')
		],
		],
								)
	return bbst1
 
def bbst11():
	bbst1 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
		InlineKeyboardButton(text='Добавить в корзину🛒',callback_data='buy:185')
		],
		[
		InlineKeyboardButton(text='Назад◀️',callback_data='back_to_jir')
		],
		],
								)
	return bbst1

def bbst12():
	bbst1 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
		InlineKeyboardButton(text='Добавить в корзину🛒',callback_data='buy:186')
		],
		[
		InlineKeyboardButton(text='Назад◀️',callback_data='back_to_jir')
		],
		],
								)
	return bbst1

def bbst13():
	bbst1 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
		InlineKeyboardButton(text='Добавить в корзину🛒',callback_data='buy:187')
		],
		[
		InlineKeyboardButton(text='Назад◀️',callback_data='back_to_jir')
		],
		],
								)
	return bbst1

def bbst14():
	bbst1 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
		InlineKeyboardButton(text='Добавить в корзину🛒',callback_data='buy:188')
		],
		[
		InlineKeyboardButton(text='Назад◀️',callback_data='back_to_jir')
		],
		],
								)
	return bbst1

def bbst15():
	bbst1 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
		InlineKeyboardButton(text='Добавить в корзину🛒',callback_data='buy:189')
		],
		[
		InlineKeyboardButton(text='Назад◀️',callback_data='back_to_jir')
		],
		],
								)
	return bbst1

def bbst16():
	bbst1 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
		InlineKeyboardButton(text='Добавить в корзину🛒',callback_data='buy:190')
		],
		[
		InlineKeyboardButton(text='Назад◀️',callback_data='back_to_jir')
		],
		],
								)
	return bbst1

def bbst17():
	bbst1 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
		InlineKeyboardButton(text='Добавить в корзину🛒',callback_data='buy:191')
		],
		[
		InlineKeyboardButton(text='Назад◀️',callback_data='back_to_jir')
		],
		],
								)
	return bbst1

def bbst18():
	bbst1 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
		InlineKeyboardButton(text='Добавить в корзину🛒',callback_data='buy:192')
		],
		[
		InlineKeyboardButton(text='Назад◀️',callback_data='back_to_jir')
		],
		],
								)
	return bbst1

def bbst19():
	bbst1 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
		InlineKeyboardButton(text='Добавить в корзину🛒',callback_data='buy:193')
		],
		[
		InlineKeyboardButton(text='Назад◀️',callback_data='back_to_jir')
		],
		],
								)
	return bbst1

def bbst20():
	bbst1 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
		InlineKeyboardButton(text='Добавить в корзину🛒',callback_data='buy:194')
		],
		[
		InlineKeyboardButton(text='Назад◀️',callback_data='back_to_jir')
		],
		],
								)
	return bbst1

def bbst21():
	bbst1 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
		InlineKeyboardButton(text='Добавить в корзину🛒',callback_data='buy:195')
		],
		[
		InlineKeyboardButton(text='Назад◀️',callback_data='back_to_jir')
		],
		],
								)
	return bbst1

def bbst22():
	bbst1 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
		InlineKeyboardButton(text='Добавить в корзину🛒',callback_data='buy:196')
		],
		[
		InlineKeyboardButton(text='Назад◀️',callback_data='back_to_jir')
		],
		],
								)
	return bbst1

def bbst23():
	bbst1 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
		InlineKeyboardButton(text='Добавить в корзину🛒',callback_data='buy:197')
		],
		[
		InlineKeyboardButton(text='Назад◀️',callback_data='back_to_jir')
		],
		],
								)
	return bbst1

def bbst24():
	bbst1 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
		InlineKeyboardButton(text='Добавить в корзину🛒',callback_data='buy:198')
		],
		[
		InlineKeyboardButton(text='Назад◀️',callback_data='back_to_jir')
		],
		],
								)
	return bbst1

def bbst25():
	bbst1 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
		InlineKeyboardButton(text='Добавить в корзину🛒',callback_data='buy:199')
		],
		[
		InlineKeyboardButton(text='Назад◀️',callback_data='back_to_jir')
		],
		],
								)
	return bbst1

def bbst26():
	bbst1 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
		InlineKeyboardButton(text='Добавить в корзину🛒',callback_data='buy:200')
		],
		[
		InlineKeyboardButton(text='Назад◀️',callback_data='back_to_jir')
		],
		],
								)
	return bbst1

def bbst27():
	bbst1 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
		InlineKeyboardButton(text='Добавить в корзину🛒',callback_data='buy:201')
		],
		[
		InlineKeyboardButton(text='Назад◀️',callback_data='back_to_jir')
		],
		],
								)
	return bbst1

def bbst28():
	bbst1 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
		InlineKeyboardButton(text='Добавить в корзину🛒',callback_data='buy:202')
		],
		[
		InlineKeyboardButton(text='Назад◀️',callback_data='back_to_jir')
		],
		],
								)
	return bbst1

def bbst29():
	bbst1 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
		InlineKeyboardButton(text='Добавить в корзину🛒',callback_data='buy:203')
		],
		[
		InlineKeyboardButton(text='Назад◀️',callback_data='back_to_jir')
		],
		],
								)
	return bbst1

def bbst30():
	bbst1 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
		InlineKeyboardButton(text='Добавить в корзину🛒',callback_data='buy:204')
		],
		[
		InlineKeyboardButton(text='Назад◀️',callback_data='back_to_jir')
		],
		],
								)
	return bbst1

def bbst31():
	bbst1 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
		InlineKeyboardButton(text='Добавить в корзину🛒',callback_data='buy:205')
		],
		[
		InlineKeyboardButton(text='Назад◀️',callback_data='back_to_jir')
		],
		],
								)
	return bbst1

def bbst32():
	bbst1 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
		InlineKeyboardButton(text='Добавить в корзину🛒',callback_data='buy:206')
		],
		[
		InlineKeyboardButton(text='Назад◀️',callback_data='back_to_jir')
		],
		],
								)
	return bbst1

def bbst33():
	bbst1 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
		InlineKeyboardButton(text='Добавить в корзину🛒',callback_data='buy:207')
		],
		[
		InlineKeyboardButton(text='Назад◀️',callback_data='back_to_jir')
		],
		],
								)
	return bbst1

def bbst34():
	bbst1 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
		InlineKeyboardButton(text='Добавить в корзину🛒',callback_data='buy:208')
		],
		[
		InlineKeyboardButton(text='Назад◀️',callback_data='back_to_jir')
		],
		],
								)
	return bbst1

def bbst35():
	bbst1 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
		InlineKeyboardButton(text='Добавить в корзину🛒',callback_data='buy:209')
		],
		[
		InlineKeyboardButton(text='Назад◀️',callback_data='back_to_jir')
		],
		],
								)
	return bbst1

def bbst36():
	bbst1 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
		InlineKeyboardButton(text='Добавить в корзину🛒',callback_data='buy:210')
		],
		[
		InlineKeyboardButton(text='Назад◀️',callback_data='back_to_jir')
		],
		],
								)
	return bbst1

def bbst37():
	bbst1 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
		InlineKeyboardButton(text='Добавить в корзину🛒',callback_data='buy:211')
		],
		[
		InlineKeyboardButton(text='Назад◀️',callback_data='back_to_jir')
		],
		],
								)
	return bbst1

def nazad_korzina():
	nk = InlineKeyboardMarkup(
		inline_keyboard = [
		[
		InlineKeyboardButton(text='Kорзина🛒',callback_data='korz')
		],
		[
		InlineKeyboardButton(text='Очистить корзину❌',callback_data='clean')
		],
		[
		InlineKeyboardButton(text='Назад◀️',callback_data='back_from_protein')
		],
		],
								)
	return nk

def general():
	nmn = InlineKeyboardMarkup(
		inline_keyboard = [
		[
		InlineKeyboardButton(text='Очистить корзину❌',callback_data='clean')
		],
		[
		InlineKeyboardButton(text='Назад◀️',callback_data='back_from_protein')
		],
		],
								)
	return nmn

its_jir = InlineKeyboardMarkup(#menu jir
 	inline_keyboard = [
 	      [
			InlineKeyboardButton(text='Ape Shit Cutz🍎',callback_data='appe')
		],
		 [
			InlineKeyboardButton(text='Asia Black 25🌏',callback_data='asi')
		],
		[
			InlineKeyboardButton(text='Black spider 25 Cloma Pharma🕷',callback_data='pauk')
		],
		[
			InlineKeyboardButton(text='Black Widow 25📉',callback_data='widow')
		],
		[
			InlineKeyboardButton(text='Burn on Keto🔥',callback_data='keto')
		],
		[
			InlineKeyboardButton(text='Cellucor Super HD🟩',callback_data='cell')
		],
		[
			InlineKeyboardButton(text='China White🌏',callback_data='china')
		],
		[
			InlineKeyboardButton(text='CLA 1250🚒',callback_data='cla1250')
		],
		[
			InlineKeyboardButton(text='CLA от RSP Nutrition💭',callback_data='cla_rsp')
		],
		[
			InlineKeyboardButton(text='Guggul Ultimate Nutrition🦮',callback_data='guggul')
		],
		[
			InlineKeyboardButton(text='LEAN MODE🔵',callback_data='leanmode')
		],
		[
			InlineKeyboardButton(text='LeanlFire🍀',callback_data='leanfire')
		],
		[
			InlineKeyboardButton(text='Nutrex Lipo 6 Black Maximum Potency🔥',callback_data='nutrex')
		],
		[
			InlineKeyboardButton(text='Lipo-6 Black Hers🧘',callback_data='black_hers')
		],
		[
			InlineKeyboardButton(text='Methyldrene 25 от Cloma Pharma🟨',callback_data='methyldrene')
		],
		[
			InlineKeyboardButton(text='Platinum Pure CLA👨‍🦳',callback_data='pure_cla')
		],
		[
			InlineKeyboardButton(text='Roxylean 60 caps🤟',callback_data='roxylean')
		],
		[
			InlineKeyboardButton(text='Animal Cuts🦁',callback_data='animals_curs')
		],
		[
			InlineKeyboardButton(text='Black Mamba⬛️',callback_data='black_mamba')
		],
		[
			InlineKeyboardButton(text='CLA Pure 1000',callback_data='cla_pure_1000')
		],
		[
			InlineKeyboardButton(text='Fat Burner Daily🔥',callback_data='fat_burner')
		],
		[
			InlineKeyboardButton(text='HELL FIRE🔥',callback_data='hell_fire')
		],
		[
			InlineKeyboardButton(text='Hydroxycut💭',callback_data='hydroxycut')
		],
		[
			InlineKeyboardButton(text='Hydroxycut Hardcore Elite',callback_data='hardcor_elite')
		],
		[
			InlineKeyboardButton(text='Назад◀️',callback_data='back_to_main'),
			InlineKeyboardButton(text='Больше➡️',callback_data='mor_jir'),
		],
	],
)
jirrr = InlineKeyboardMarkup(#menu more_jir
 	inline_keyboard = [
 	      [
 	      InlineKeyboardButton(text="Hydroxycut Hardcore Next Gen🥇",callback_data="next_gen"),
 	      
 	      ],
 	      [
 	      	InlineKeyboardButton(text="Hydroxycut MAX For Women🔥",callback_data="max_forwomen"),
 	      ],
 	      [
 	      InlineKeyboardButton(text="Hydroxycut Platinum💪",callback_data="hydro_platinum"),
 	    
 	      ],
 	      [
 	       InlineKeyboardButton(text="JetFuel Superburn🥩",callback_data="jetful_super"),
 	      ],
 	      [
          InlineKeyboardButton(text="KETO ELITE🔋",callback_data="ketto_elite"),
 	      
 	      ],
 	      [
 	      	InlineKeyboardButton(text="keto-karma burn fat red🔝",callback_data="keto_karma"),
 	      ],
 	      [
 	      	InlineKeyboardButton(text="Lipo 6 Natural👾",callback_data="lipo_natural")
 	      ],
 	      [
 	      InlineKeyboardButton(text="NUTREX LIPO-6 RX 60 CAP🟥",callback_data="nutrex_lipo6"),
 	      
 	      ],
 	      [
 	      	InlineKeyboardButton(text="Fat Burner Plus Super Citrimax✴️",callback_data="fat_burner_plus")
 	      ],
 	      [
 	      InlineKeyboardButton(text="Metabolism Weight Control, 70 🥥",callback_data="weight_control"),
 	      
 	      ],
 	      [
 	      	InlineKeyboardButton(text="NOBI NUTRITION,PREMIUM WOMEN'S🍫",callback_data="nobii")
 	      ],
 	      [
 	      InlineKeyboardButton(text="RAPIDCUTS SHREDDED ALLMAX NUTRITION⚡️",callback_data="rapiducuts"),
 	      
 	      ],
 	      [
 	      InlineKeyboardButton(text="Ripped Fast🍓",callback_data="ripped_fast")
 	      ],
 	      [
 	      InlineKeyboardButton(text="Terra Origin HEALTHY💧",callback_data="terra_origgin"),
 	      
 	      ],
 	      [
 	      InlineKeyboardButton(text="The Omen!🍓",callback_data="the_omen")
 	      ],
 	      [
			InlineKeyboardButton(text="Назад🔙",callback_data="back_to_jir") 	       	      
 	      ],
 	 ],

 )

its_geyner = InlineKeyboardMarkup(#menu geyner
 	inline_keyboard = [
 	      [
			InlineKeyboardButton(text='14 Superior HYPER MASS PROFESSIONAL🍎',callback_data='hyper_mass_prof')
		],
		 [
			InlineKeyboardButton(text='14 Superior SUPERIOR MASS PROFESSIONAL🌏',callback_data='superoir_mass_prof')
		],
		[
			InlineKeyboardButton(text='Applied Critical Mass Original🕷',callback_data='Applied_Critical')
		],
		[
			InlineKeyboardButton(text='Big Mass от Big Man Nutrition📉',callback_data='big_mass_big_man')
		],
		[
			InlineKeyboardButton(text='Carbs Pro Matrix от Superior14🔥',callback_data='Carbs_Pro_Matrix')
		],
		[
			InlineKeyboardButton(text='Kevin Levrone Anabolic Mass🟩',callback_data='Kevin_Levrone_Anabolic_Mass')
		],
		[
			InlineKeyboardButton(text='Mega Mass 4000 от Weider🌏',callback_data='megamass400weider')
		],
		[
			InlineKeyboardButton(text='Monster Lab Real Mass Gainer🚒',callback_data='Monster_Lab_Real_Mass_Gainer')
		],
		[
			InlineKeyboardButton(text='PLATINUM MASS 14 Superior💭',callback_data='PLATINUM_MASS_14_Superior')
		],
		[
			InlineKeyboardButton(text='R1 GAINER LBS 2,75 kg🦮',callback_data='r1_gainer_lbs')
		],
		[
			InlineKeyboardButton(text='Rule 1 R1 5,4кг🔵',callback_data='rule1_r1_54')
		],
		[
			InlineKeyboardButton(text='SERIOUS MASS OPTIMUM NUTRITION🍀',callback_data='serious_mass_optimuim')
		],
		[
			InlineKeyboardButton(text='Serious Mass 1250🔥',callback_data='serious_mass_1250')
		],
		[
			InlineKeyboardButton(text='Super Mass Gainer от Dymatize🧘',callback_data='Super_Mass_Gainer')
		],
		[
			InlineKeyboardButton(text='Superior 14 Platinum Mass🟨',callback_data='Superior_14_Platinum_Mass')
		],
		[
			InlineKeyboardButton(text='True-Mass 1200👨‍🦳',callback_data='True_Mass_1200')
		],
		[
			InlineKeyboardButton(text='Up Your Mass 1200🤟',callback_data='Up_Your_Mass_1200')
		],
		[
			InlineKeyboardButton(text='Mass Tech Extreme 2000🦁',callback_data='MassTechExtreme2000')
		],
		[
			InlineKeyboardButton(text='Hyper Gain⬛️',callback_data='hyper_gain')
		],
		[
			InlineKeyboardButton(text='MUTANT MASS 6.8 kg',callback_data='mutant_mass_68kg')
		],
		[
			InlineKeyboardButton(text='Myprotein Impact Weight Gainer🔥',callback_data='Myprotein_Impact_Weight_Gainer')
		],
		[
			InlineKeyboardButton(text='Anabolic Mass🔥',callback_data='Anabolic_Mass')
		],
		[
			InlineKeyboardButton(text='ATLET HARD MASS💭',callback_data='ATLETHARDMASS')
		],
		[
			InlineKeyboardButton(text='Bulk Muscle от BPI Sports 6.8 kg',callback_data='bulk_muscle_bpisports')
		],
		[
			InlineKeyboardButton(text='Назад◀️',callback_data='back_to_main'),
			InlineKeyboardButton(text='Больше➡️',callback_data='mor_geyner'),
		],
	],
)


geynerrr = InlineKeyboardMarkup(#menu more_geyner
 	inline_keyboard = [
 	      [
 	      InlineKeyboardButton(text="Carnivor Mass от MuscleMeds🥇",callback_data="Carnivor_Mass_MuscleMeds"),
 	      
 	      ],
 	      [
 	      	InlineKeyboardButton(text="Gain Fast от Universal Nutrition🔥",callback_data="Gain_Fast_Universal_Nutrition"),
 	      ],
 	      [
 	      InlineKeyboardButton(text="Hardcore Mass Phase💪",callback_data="HardcoreMassPhase"),
 	    
 	      ],
 	      [
 	       InlineKeyboardButton(text="HealthXP Essential Series Weight🥩",callback_data="pzds_slojniy_cbl"),
 	      ],
 	      [
          InlineKeyboardButton(text="HyperBolic Mass🔋",callback_data="HyperBolicMass"),
 	      
 	      ],
 	      [
 	      	InlineKeyboardButton(text="Kevin Levrone, Anabolic Mass, 7 кг🔝",callback_data="kevin_radnoy_geyner_7kg"),
 	      ],
 	      [
 	      	InlineKeyboardButton(text="Levro Legendary MASS от KEVIN LEVRONE👾",callback_data="yMASSKEVINLEVRONE")
 	      ],
 	      [
 	      InlineKeyboardButton(text=" Kevin Levrone, Legendary Mass, 6800 гр🟥",callback_data="kevin_levrone_legen_mass68"),
 	      
 	      ],
 	      [
 	      	InlineKeyboardButton(text="Mass Gainer Geneticlab Nutrition✴️",callback_data="MassGainerGeneticlab")
 	      ],
 	      [
 	      InlineKeyboardButton(text="Muscletech Mass Gainer🥥",callback_data="muscle_mathchgeinre"),
 	      
 	      ],
 	      [
 	      	InlineKeyboardButton(text="MASS INFUSION🍫",callback_data="MASSINFUSION")
 	      ],
 	      [
 	      InlineKeyboardButton(text="Muscle Juice Revolution 2600⚡️",callback_data="muscle_juice_revolution"),
 	      
 	      ],
 	      [
 	      InlineKeyboardButton(text="Combat XL Mass Gainer🍓",callback_data="combat_xlmass_gainer")
 	      ],
 	      [
 	      InlineKeyboardButton(text="Mutant Mass 2,27кг💧",callback_data="mutant_mass_227"),
 	      
 	      ],
 	      [
 	      InlineKeyboardButton(text="Special Mass Gainer🍓",callback_data="special_mass_geiner")
 	      ],
 	      [
			InlineKeyboardButton(text="Назад🔙",callback_data="geyner") 	       	      
 	      ],
 	 ],

 )

kre = InlineKeyboardMarkup(#menu _jir
 	inline_keyboard = [
 	      [
 	      InlineKeyboardButton(text="100% Creatine Monohydrate🥇",callback_data="Creatine_Monohydrate"),
 	      
 	      ],
 	      [
 	      	InlineKeyboardButton(text="Charged Creatine Rule 1🔥",callback_data="Chargedcreatinerule1"),
 	      ],
 	      [
 	      InlineKeyboardButton(text="Creatine 120 serv Optimum Nutrition💪",callback_data="Creatine120serv"),
 	    
 	      ],
 	      [
 	       InlineKeyboardButton(text="Creatine 60 serv Optimum Nutrition🥩",callback_data="Creatine60servOptimum"),
 	      ],
 	      [
          InlineKeyboardButton(text="Creatine Micronized от Dymatize🔋",callback_data="CreatineMicronizedDymatize"),
 	      
 	      ],
 	      [
 	      	InlineKeyboardButton(text="Creatine Monohydrate powder 300g🔝",callback_data="CreatineMonohydratepowder"),
 	      ],
 	      [
 	      	InlineKeyboardButton(text="CREATINE,CREA BAD ASS, 300g👾",callback_data="creatine_crea_badass")
 	      ],
 	      [
 	      InlineKeyboardButton(text="MUSCLE TECH Креатин CELL TECH 2,72кг🟥",callback_data="Muscle_techcell272"),
 	      
 	      ],
 	      [
 	      	InlineKeyboardButton(text="Pole Nutrition Creatine Monohydrate, 300 Grams✴️",callback_data="pole_nutrition_creas_mono")
 	      ],
 	      [
 	      InlineKeyboardButton(text="ProMera Sports, Con-Cret, 64 serv🥥",callback_data="prometa_sports_concret"),
 	      
 	      ],
 	      [
 	      	InlineKeyboardButton(text="Sunline Alaska🍫",callback_data="sunline_alaska")
 	      ],
 	      [
 	      InlineKeyboardButton(text="Fitness Authority Ice Creatine⚡️",callback_data="fitness_authority_ice_creatine"),
 	      
 	      ],
 	      [
 	      InlineKeyboardButton(text="Kevin Levrone Gold Creatine🍓",callback_data="kevin_levrone_gold_creatine")
 	      ],
 	      [
 	      InlineKeyboardButton(text="Anabolic Creatine от Kevin Levrone💧",callback_data="anabolic_creatine_kevin_levorne"),
 	      
 	      ],
 	      [
 	      InlineKeyboardButton(text="CreaGen🍓",callback_data="creagen")
 	      ],
		  [
 	      InlineKeyboardButton(text="CREAKONG🍓",callback_data="crea_kong")
 	      ],
 	      [
 	      InlineKeyboardButton(text="Creatine 3000 All Max💧",callback_data="creatine_3000_allmax"),
 	      
 	      ],
		  [
			InlineKeyboardButton(text='Назад◀️',callback_data='back_to_main'),
			InlineKeyboardButton(text='Больше➡️',callback_data='mor_creatin'),
		],
 	 ],

 )

mor_creatine = InlineKeyboardMarkup(#menu more_geyner
 	inline_keyboard = [
 	      [
 	      InlineKeyboardButton(text="Creatine DNA🥇",callback_data="creatine_dna"),
 	      
 	      ],
 	      [
 	      	InlineKeyboardButton(text="Creatine Drive Nutrex🔥",callback_data="creatine_drive_nutrex"),
 	      ],
 	      [
 	      InlineKeyboardButton(text="Creatine Monohydrate💪",callback_data="creatine_monohydrate"),
 	    
 	      ],
 	      [
 	       InlineKeyboardButton(text="Creatine Monohydrate MyProtein🥩",callback_data="CreatinemyMonohydrate"),
 	      ],
 	      [
          InlineKeyboardButton(text="Creatine Powder 300g🔋",callback_data="creatine_pwoder300g"),
 	      
 	      ],
 	      [
 	      	InlineKeyboardButton(text="Creatine-XS🔝",callback_data="creatine_xsmaxip"),
 	      ],
 	      [
 	      	InlineKeyboardButton(text="Dexer Jackson, Micronized 300mg👾",callback_data="dexer_molody_jackson")
 	      ],
 	      [
 	      InlineKeyboardButton(text="GAT Creatine Powder🟥",callback_data="gat_creatin_powder"),
 	      
 	      ],
 	      [
 	      	InlineKeyboardButton(text="Kevin Levrone MICRONIZED MONOHYDRATE 300g✴️",callback_data="MICRONIZED_MONOHYDRATe")
 	      ],
 	      [
 	      InlineKeyboardButton(text="ProMera Sports Con-Cret Pre Workout🥥",callback_data="workout_pilesosramhav"),
 	      
 	      ],
 	      [
 	      	InlineKeyboardButton(text="Skull Labs Angel Creatine🍫",callback_data="Skulls_labs_angels")
 	      ],
 	      [
 	      InlineKeyboardButton(text="Inner Armour⚡️",callback_data="inner_armour"),
 	      
 	      ],
 	      [
			InlineKeyboardButton(text="Назад🔙",callback_data="kreatin") 	       	      
 	      ],
 	 ],

 )



energeticss = InlineKeyboardMarkup(#menu _energetic
 	inline_keyboard = [
 	      [
 	      InlineKeyboardButton(text="Apeshit Untamed 40 Servicios🥇",callback_data="apeshit_untamed_40servicious"),
 	      
 	      ],
 	      [
 	      	InlineKeyboardButton(text="Apshit Pumps🔥",callback_data="Apshit_pumps_energetic"),
 	      ],
 	      [
 	      InlineKeyboardButton(text="CITRULLINE PURE от Extrifit💪",callback_data="citurulline_pure_ener"),
 	    
 	      ],
 	
 	      [
          InlineKeyboardButton(text="HEMO-RAGE UNLEASHED от Nutrex🔋",callback_data="HEMORAGEUNLEASHED"),
 	      
 	      ],
 	      
 	    
 	      [
 	      	InlineKeyboardButton(text="N.O.- XPLODE✴️",callback_data="noxplode_ener")
 	      ],
 	      [
 	      InlineKeyboardButton(text="Pole Nutrition Teazer Pre🥥",callback_data="pole_nutrtut_teazere_prom"),
 	      
 	      ],
 	  
 	      [
 	      InlineKeyboardButton(text="Pre-Sweat Advanced Pre-Workout⚡️",callback_data="PreSweat_AdvancedPreWorkout"),
 	      
 	      ],
 	      [
 	      InlineKeyboardButton(text="The Curse от Cobra Nutrition🍓",callback_data="curse_cobra_nutrtitionener")
 	      ],
 	    
		
 	    
		[
			InlineKeyboardButton(text='C4 энергетик pre	 work out original🍎',callback_data='xzchtortopomogibly')
		],
		
		[
			InlineKeyboardButton(text='Cellucor C4 Extreme Energy™(270g)',callback_data='cellucor_extreme_energ')
		],
		[
			InlineKeyboardButton(text='Moons Truck от Zoomad Labs🔥',callback_data='moons_truck_zoomad_ener')
		],
		[
			InlineKeyboardButton(text='GUARANA🚒',callback_data='guarana_energe')
		],
		[
			InlineKeyboardButton(text='Энергетический напиток - Апельсин (500 мл)🍊',callback_data='orange_napitka')
		],
		
	
		  [
			InlineKeyboardButton(text='Назад◀️',callback_data='back_to_main'),
		],
 	 ],

 )

its_geyner = InlineKeyboardMarkup(#menu geyner
 	inline_keyboard = [
 	      [
			InlineKeyboardButton(text='14 Superior HYPER MASS PROFESSIONAL🍎',callback_data='hyper_mass_prof')
		],
		 [
			InlineKeyboardButton(text='14 Superior SUPERIOR MASS PROFESSIONAL🌏',callback_data='superoir_mass_prof')
		],
		[
			InlineKeyboardButton(text='Applied Critical Mass Original🕷',callback_data='Applied_Critical')
		],
		[
			InlineKeyboardButton(text='Big Mass от Big Man Nutrition📉',callback_data='big_mass_big_man')
		],
		[
			InlineKeyboardButton(text='Carbs Pro Matrix от Superior14🔥',callback_data='Carbs_Pro_Matrix')
		],
		[
			InlineKeyboardButton(text='Kevin Levrone Anabolic Mass🟩',callback_data='Kevin_Levrone_Anabolic_Mass')
		],
		[
			InlineKeyboardButton(text='Mega Mass 4000 от Weider🌏',callback_data='megamass400weider')
		],
		[
			InlineKeyboardButton(text='Monster Lab Real Mass Gainer🚒',callback_data='Monster_Lab_Real_Mass_Gainer')
		],
		[
			InlineKeyboardButton(text='PLATINUM MASS 14 Superior💭',callback_data='PLATINUM_MASS_14_Superior')
		],
		[
			InlineKeyboardButton(text='R1 GAINER LBS 2,75 kg🦮',callback_data='r1_gainer_lbs')
		],
		[
			InlineKeyboardButton(text='Rule 1 R1 5,4кг🔵',callback_data='rule1_r1_54')
		],
		[
			InlineKeyboardButton(text='SERIOUS MASS OPTIMUM NUTRITION🍀',callback_data='serious_mass_optimuim')
		],
		[
			InlineKeyboardButton(text='Serious Mass 1250🔥',callback_data='serious_mass_1250')
		],
		[
			InlineKeyboardButton(text='Super Mass Gainer от Dymatize🧘',callback_data='Super_Mass_Gainer')
		],
		[
			InlineKeyboardButton(text='Superior 14 Platinum Mass🟨',callback_data='Superior_14_Platinum_Mass')
		],
		[
			InlineKeyboardButton(text='True-Mass 1200👨‍🦳',callback_data='True_Mass_1200')
		],
		[
			InlineKeyboardButton(text='Up Your Mass 1200🤟',callback_data='Up_Your_Mass_1200')
		],
		[
			InlineKeyboardButton(text='Mass Tech Extreme 2000🦁',callback_data='MassTechExtreme2000')
		],
		[
			InlineKeyboardButton(text='Hyper Gain⬛️',callback_data='hyper_gain')
		],
		[
			InlineKeyboardButton(text='MUTANT MASS 6.8 kg',callback_data='mutant_mass_68kg')
		],
		[
			InlineKeyboardButton(text='Myprotein Impact Weight Gainer🔥',callback_data='Myprotein_Impact_Weight_Gainer')
		],
		[
			InlineKeyboardButton(text='Anabolic Mass🔥',callback_data='Anabolic_Mass')
		],
		[
			InlineKeyboardButton(text='ATLET HARD MASS💭',callback_data='ATLETHARDMASS')
		],
		[
			InlineKeyboardButton(text='Bulk Muscle от BPI Sports 6.8 kg',callback_data='bulk_muscle_bpisports')
		],
		[
			InlineKeyboardButton(text='Назад◀️',callback_data='back_to_main'),
			InlineKeyboardButton(text='Больше➡️',callback_data='mor_geyner'),
		],
	],
)


buster_testt = InlineKeyboardMarkup(#menu more_geyner
 	inline_keyboard = [
 	      [
 	      InlineKeyboardButton(text="Tribulus от BPI Sports 180 капсул🥇",callback_data="tribilus_testoron_damn"),
 	      
 	      ],
 	      [
 	      	InlineKeyboardButton(text="Primeval Labs APESH*T Alpha🔥",callback_data="primeval_labs_alphha"),
 	      ],
 	      [
 	      InlineKeyboardButton(text="Primeval Labs Apesh*t Test 💪",callback_data="primeval_labs_apesh_test"),
 	    
 	      ],
 	      [
 	       InlineKeyboardButton(text="Ultimate Nutrition Testostron Grow HP 126 Tablets🥩",callback_data="ultimate_nutrition_testoron_grow"),
 	      ],
 	      [
          InlineKeyboardButton(text="Tribulus terrestris от VPLab🔋",callback_data="tribulus_testoronn"),
 	      
 	      ],
 	      [
 	      	InlineKeyboardButton(text="Force Factor Tribulus🔝",callback_data="force_factor_testoron"),
 	      ],
 	      [
 	      	InlineKeyboardButton(text="Kevin Levrone LevroTribulus 1500👾",callback_data="levrone_tribulusss")
 	      ],
 	      [
 	      InlineKeyboardButton(text=" Testrol Elite  Gat🟥",callback_data="testoroline_elite_gatt"),
 	      
 	      ],
 	      [
 	      	InlineKeyboardButton(text="MRM TRIBUPLEX 750✴️",callback_data="Mrm_tribuplex_testoronn")
 	      ],
 	      [
 	      InlineKeyboardButton(text="Nugenix Natural Testosterone Booster - 42🥥",callback_data="nugenix_natural_testerone"),
 	      
 	      ],
 	      [
 	      	InlineKeyboardButton(text="Test HD Thermo, Muscletech, 90🍫",callback_data="test_thermo_muscletech")
 	      ],
 	      [
 	      InlineKeyboardButton(text="TribX90⚡️",callback_data="tribx90_salomm"),
 	      
 	      ],
 	      [
 	      InlineKeyboardButton(text="Tribulus 1000 mg.🍓",callback_data="tribulus_100mg_ener")
 	      ],
 	      [
 	      InlineKeyboardButton(text="Animal Pak Animal M-Stak Non-Hormonal Anabolic Stack💧",callback_data="anabolic_pak_animal_mmm"),
 	      
 	      ],
 	      [
 	      InlineKeyboardButton(text="Nutrex Tribulus Black 1300🍓",callback_data="nutrex_tribulus_black1399")
 	      ],
		  [
 	      InlineKeyboardButton(text="Tesla Turbo-X.⚡️",callback_data="tesla_turbo_testor"),
 	      
 	      ],
		   [
 	      InlineKeyboardButton(text="Kevin Levrone Anabolic Test 90⚡️",callback_data="kevin_levrone_anabloc90testor"),
 	      
 	      ],
 	      [
			InlineKeyboardButton(text="Назад🔙",callback_data="back_to_main"),
			InlineKeyboardButton(text='Больше➡️',callback_data='mor_testeoron'),	       	      
 	      ],
 	 ],

 )


mor_testoon = InlineKeyboardMarkup(#menu more_testoron
 	inline_keyboard = [
 	      [
 	      InlineKeyboardButton(text="EVL Tribulus - 650 mg🥇",callback_data="evl_tribulus_testoron"),
 	      
 	      ],
 	      [
 	      	InlineKeyboardButton(text="Tribulus XS 120 caps🔥",callback_data="tribulus_xs_120capss"),
 	      ],
 	      [
 	      InlineKeyboardButton(text="Animal Test от Universal Nutrition💪",callback_data="animal_test_universal_tets"),
 	    
 	      ],
 	      [
 	       InlineKeyboardButton(text="Men’s Multi + test🥩",callback_data="mensmulti_testoron"),
 	      ],
 	      [
          InlineKeyboardButton(text="GAT Sport Testrol65🔋",callback_data="gat_sport_testorol655"),
 	      
 	      ],
 	      [
 	      	InlineKeyboardButton(text="Bodybuilding Signature Testosterone Booster🔝",callback_data="bodybuilding_signaturee"),
 	      ],
 	      [
 	      	InlineKeyboardButton(text="Tribulus Elite👾",callback_data="tribulus_elite_testoron")
 	      ],
 	      [
 	      InlineKeyboardButton(text="RIBULUS, SOURCE NATURALS, 750🟥",callback_data="ribulus_source_naturals_testor"),
 	      
 	      ],
 	      [
 	      	InlineKeyboardButton(text="Universal Pro✴️",callback_data="universal_pro_testoron")
 	      ],
 	      [
 	      InlineKeyboardButton(text="Tribuvar 1000🥥",callback_data="tribuvar_1000_testoron"),
 	      
 	      ],
 	      [
 	      	InlineKeyboardButton(text="Tribulus 625 ON🍫",callback_data="tribulus_625_on_testoron")
 	      ],
 	      [
 	      InlineKeyboardButton(text="Tribulus 1100 1125 mg⚡️",callback_data="tribulus_1100_1125mg"),
 	      
 	      ],
		  [
 	      InlineKeyboardButton(text="Testosterone Booster Six Star⚡️",callback_data="testorone_booster_sixstar"),
 	      
 	      ],
		  [
 	      InlineKeyboardButton(text="Test HD⚡️",callback_data="test_hd_testorone"),
 	      
 	      ],
		  [
 	      InlineKeyboardButton(text="P6 pm Testosterone Booster⚡️",callback_data="p6_pm_testorone"),
 	      
 	      ],
		  [
 	      InlineKeyboardButton(text="Now Tribulus 500mg⚡️",callback_data="now_tribulus_testoron500mgg"),
 	      
 	      ],
		  [
 	      InlineKeyboardButton(text="N1-T Universal⚡️",callback_data="n1_t_universtjkwehew"),
 	      
 	      ],
		  [
 	      InlineKeyboardButton(text="EVL Test EVLUTION NUTRITION⚡️",callback_data="evltest_evolution_nutrurthj"),
 	      
 	      ],
		   [
 	      InlineKeyboardButton(text="Alpha Test⚡️",callback_data="alpha-Testststsor"),
 	      
 	      ],
		   [
 	      InlineKeyboardButton(text="Black Tiger⚡️",callback_data="black_tigwer_tesatorom"),
 	      
 	      ],
 	      [
			InlineKeyboardButton(text="Назад🔙",callback_data="buster") 	       	      
 	      ],
 	 ],

 )





