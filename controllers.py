class  UserController:

	def __init__(self, connection, db_cursor):
		self.connection = connection
		self.cursor = db_cursor

	def create_base(self):
		self.cursor.execute("""CREATE TABLE IF NOT EXISTS users(
			id integer,
			username varchar(60),
			tel int NULL,
			kor1 bigint NULL,
			kor2 bigint NULL
			)""")

	def add_user(self, user_id, username):
		self.cursor.execute("INSERT INTO users VALUES ({},'{}',NULL,NULL,NULL)".format(user_id, username))
		return self.connection.commit()

	def id_user(self, user_id):
		self.cursor.execute(f"SELECT EXISTS(SELECT id FROM users WHERE id = {user_id})")
		data = self.cursor.fetchone()
		return data

	def location_update(self, user_id, kor1, kor2):
		self.cursor.execute(f"UPDATE users SET kor1 = {kor1}, kor2 = {kor2} WHERE id = {user_id}")
		return self.connection.commit()

	def telephone(self, user_id, tel1):
		self.cursor.execute(f"UPDATE users SET tel = {tel1} WHERE id = {user_id}")
		return self.connection.commit()

	def sendto_admin(self, user_id):
		self.cursor.execute(f"SELECT * FROM  users WHERE id = {user_id}")
		da = self.cursor.fetchone()
		return  da

	def count(self):
		self.cursor.execute("SELECT COUNT(id) FROM users")
		fo = self.cursor.fetchall()
		return fo

	def reklama(self):
		self.cursor.execute("SELECT * FROM users")
		rek = self.cursor.fetchall()
		return rek

class  CartController:
	def __init__(self, connection, db_cursor):
		self.connection = connection
		self.cursor = db_cursor

	def create_base_cart(self):
		self.cursor.execute("""CREATE TABLE IF NOT EXISTS cart(
			user_id integer,
			product_id integer
			)""")

	def add_cart(self,user_id,product_id):
		self.cursor.execute("""INSERT INTO cart (user_id, product_id) VALUES(?,?)""",[user_id,product_id])
		return self.connection.commit()

	def get_cart(self,idi):
		self.cursor.execute(f"SELECT * FROM cart WHERE user_id = {idi}")
		data =  self.cursor.fetchall()
		return data

	def del_final(self,idi):
		self.cursor.execute(f"DELETE FROM cart WHERE user_id={idi}")
		return  self.connection.commit()
		
class  ProductController:
	def __init__(self, connection, db_cursor):
		self.connection = connection
		self.cursor = db_cursor

	def create_base_prod(self):
		self.cursor.execute("""CREATE TABLE IF NOT EXISTS products(
			id integer,
			name varchar(190),
            price integer
			)""")
		producti = [
        (1,'Optimum Nutrition Platinum Hydrowhey',153900000),
		(2,'PROSTAR 100% WHEY PROTEIN',101004000),
		(3,'Whey Gold от Weider',79230000),
		(4,'100% WHEY GOLD STANDARD',114000000),#
		(5,'100% Casein Gold Standard',14181600),
		(6,'АТЛАНТ (креатин+глютамин)',17000000),
		(7,'АТЛАНТ (с креатином)',17000000),
		(8,'BIG WHEY',41154000),
		(9,'CARNIVOR от MuscleMeds',99750000),
		(10,'PURE WHEY 100% BE PERFECT NUTRITION',27000000),
		(11,'Whey HD от BPI Sports',98724000),
		(12,'Rule 1 Whey Blend Chocolate Fudge 68',94164000),
		(13,'Levro Iso Whey 2 kg',123211200),
		(14,'R1 Протеин Whey Blend 4,5 kg',155610000),
		(15,'R1 Casein Rule 1',103284000),
		(16,'Gat Whey Protein',101460000),
		(17,'PROSTAR 100% WHEY PROTEIN 907g',68286000),
		(18,'SUPERIOR 14 - WHEY ISOLATE ISO-PRO (2.2KG)',119700000),
		(19,'SUPERIOR 14 Superior Quattro Protein 3000G',108300000),
		(20,'Iso Sensation 93 910g',85842000),
		(21,'Iso Sensation 93 2.27kg',132012000),
		(22,'Monster Labs Whey',99636000),
		(23,'Syntha-6',101460000),
		(24,'WHEY Protein Pole Nutrition',95646000),
		(25,'Whey Gold Standatd 100 % (со стикером)',141800000),
		(27,'Vegan Protein Tesla Nutrition',54720000),
		(28,'Superior 14 Whey Core Protein',94620000),
		(29,'Tesla Whey Charger',95760000),
		(30,'Tesla Nutrition Iso Zero 100',66120000),
		(31,'Superior 14 Hydro Whey Zero',67260000),
		(32,'Iso Zero 100 Tesla Nutrition',112860000),
		(33,'Rule1 Plant Protein',66348000),
		(34,'Rule1 Protein Isolate',146262000),
		(35,'Xtend Pro Whey Isolate 826g',78660000),
		(36,'DYMATIYZE ISO 100',119700000),
		(37,'Xtend Pro Whey Isolate',107160000),
		(38,'Nitro Tech Whey Gold',102600000),
		(39,'Combat 100% Whey',91200000),
		(40,'Elite Whey Protein',102600000),
		(41,'ULTRA WHEY PRO',88920000),
		(42,'MUTANT WHEY PROTEIN',88464000),
		(43,'Elite Casein от Dymatize',102600000),
		(44,'Combat Protein Powder',107160000),
		(45,'NITRO TECH CASEIN GOLD',125400000),
		(46,'Протеин Bombbar Whey Protein (30 г)',1800000),
		(47,'BADASS Nutrition, Whey Protein, 2270 г',93480000),
		(48,'Kevin Levrone, Gold Whey, 2000 гр',96900000),
		(49,'"Slow-Release Casein',117648000),
		(50,'Viking Empire Whey',101460000),
		(51,'Fitness Authority Core Pro',96900000),
		(52,'KEVIN LEVRONE ANABOLIC ISO',132012000),
		(53,'Impact Whey Protein',99066000),
		(54,'Tesla Hydro Whey Zero',136800000),###protein end
		(55,'Ape Shit Cutz',65607000),
		(56,'Asia Black 25 Cloma Pharma',68491200),
		(57,'Black spider 25 Cloma Pharma',79800000),
		(58,'Black Widow 25',78489000),
		(59,'Burn on Keto',60499800),
		(60,'Cellucor Super HD',68491200),
		(61,'China White',68491200),
		(62,'CLA 1250',66108600),
		(63,'CLA от RSP Nutrition',64866000),
		(64,'Guggul Ultimate Nutrition',45030000),
		(65,'LEAN MODE',78397800),
		(66,'LeanlFire',58299600),
		(67,'Nutrex Lipo 6 Black Maximum Potency',59508000),
		(68,'Lipo-6 Black Hers',54834000),
		(69,'Methyldrene 25 от Cloma Pharma',70395000),
		(70,'Platinum Pure CLA',64866000),
		(71,'Roxylean 60 caps',66576000),
		(72,'Animal Cuts',84018000),
		(73,'Black Mamba',86640000),
		(74,'CLA Pure 1000',72960000),
		(75,'Fat Burner Daily',68400000),
		(76,'HELL FIRE',93480000),
		(77,'Hydroxycut',80940000),
		(78,'Hydroxycut Hardcore Elite',86640000),
		(79,'Hydroxycut Hardcore Next Gen',83220000),
		(80,'Hydroxycut MAX For Women',94620000),
		(81,'Hydroxycut Platinum',95760000),
		(82,'JetFuel Superburn',72504000),
		(83,'KETO ELITE',85500000),
		(84,'keto-karma burn fat red',76380000),
		(85,'Lipo 6 Natural',51300000),
		(86,'NUTREX LIPO-6 RX 60 CAP',54720000),
		(87,'Fat Burner Plus Super Citrimax',62700000),
		(88,'Metabolism Weight Control, 70',96900000),
		(89,'NOBI NUTRITION,PREMIUM WOMENS',54720000),
		(90,'RAPIDCUTS SHREDDED ALLMAX NUTRITION',79800000),
		(91,'Ripped Fast',64980000),
		(92,'Terra Origin HEALTHY',45486000),
		(93,'The Omen!',61617000),
		(94,'14 Superior HYPER MASS PROFESSIONAL',117935000),
		(95,'14 Superior SUPERIOR MASS PROFESSIONAL',120225000),
		(96,'Applied Critical Mass Original',122858500),
		(97,'Big Mass от Big Man Nutrition',85875000),
		(98,'Carbs Pro Matrix от Superior14',75570000),
		(99,'Kevin Levrone Anabolic Mass',82898000),
		(100,'Mega Mass 4000 от Weider',76371500),
		(101,'Monster Lab Real Mass Gainer',66982500),
		(102,'PLATINUM MASS 14 Superior',114500000),
		(103,'R1 GAINER LBS 2,75 kg',78089000),
		(104,'Rule 1 R1 5,4кг',108374300),
		(105,'SERIOUS MASS OPTIMUM NUTRITION',89310000),
		(106,'Serious Mass 1250',139575500),
		(107,'Super Mass Gainer от Dymatize',128240000),
		(108,'Superior 14 Platinum Mass',73280000),
		(109,'True-Mass 1200',129385000),
		(110,'Up Your Mass 1200',132018500),
		(111,'Mass Tech Extreme 2000',116103000),
		(112,'Hyper Gain',118164000),
		(113,'MUTANT MASS 6.8 kg',134079500),
		(114,'Myprotein Impact Weight Gainer',97210500),
		(115,'Anabolic Mass',113355000),
		(116,'ATLET HARD MASS',17000000),
		(117,'Bulk Muscle от BPI Sports 6.8 kg',120225000),
		(118,'Carnivor Mass от MuscleMeds',101905000),
		(119,'Gain Fast от Universal Nutrition',125950000),
		(120,'Hardcore Mass Phase',57250000),
		(121,'HealthXP Essential Series Weight',68700000),
		(122,'HyperBolic Mass',120225000),
		(123,'Kevin Levrone, Anabolic Mass, 7 кг',131675000),
		(124,'Levro Legendary MASS от KEVIN LEVRONE',80722500),
		(125,'Kevin Levrone, Legendary Mass, 6800 гр',125950000),
		(126,'Mass Gainer Geneticlab Nutrition',79005000),
		(127,'Muscletech Mass Gainer',91600000),
		(128,'MASS INFUSION',103050000),
		(129,'Muscle Juice Revolution 2600',90455000),
		(130,'Combat XL Mass Gainer',95035000),
		(131,'Mutant Mass 2,27кг',76371500),
		(132,'Special Mass Gainer',93890000),
		(133,'100% Creatine Monohydrate',40075000),
		(134,'Charged Creatine Rule 1',50838000),
		(135,'Creatine 120 serv Optimum Nutrition',67097000),
		(136,'Creatine 60 serv Optimum Nutrition',52555500),
		(137,'Creatine Micronized от Dymatize',36559900),
		(138,'Creatine Monohydrate powder 300g',35495000),
		(139,'CREATINE,CREA BAD ASS, 300g',62975000),
		(140,'MUSCLE TECH Креатин CELL TECH 2,72кг',103050000),
		(141,'Pole Nutrition Creatine Monohydrate, 300 Grams',32060000),
		(142,'ProMera Sports, Con-Cret, 64 serv',44998500),
		(143,'Sunline Alaska',26323600),
		(144,'Fitness Authority Ice Creatine',42387900),
		(145,'Kevin Levrone Gold Creatine',40178100),
		(146,'Anabolic Creatine от Kevin Levrone',39846000),
		(147,'CreaGen',53700500),
		(148,'CREAKONG',33205000),
		(149,'Creatine 3000 All Max',62975000),
		(150,'Creatine DNA',46945000),
		(151,'Creatine Drive Nutrex',32060000),
		(152,'Creatine Monohydrate',45800000),
		(153,'Creatine Monohydrate MyProtein',29770000),
		(154,'Creatine Powder 300g',49212100),
		(155,'Creatine-XS',68700000),
		(156,'Dexer Jackson, Micronized 300mg',32060000),
		(157,'GAT Creatine Powder',62975000),
		(158,'Kevin Levrone MICRONIZED MONOHYDRATE 300g',36640000),
		(159,'ProMera Sports Con-Cret Pre Workout',65265000),
		(160,'Skull Labs Angel Creatine',33147800),
		(161,'Inner Armour',51525000),
		(162,'Apeshit Untamed 40 Servicios',61486500),
		(163,'Apshit Pumps',64578000),
		(164,'CITRULLINE PURE от Extrifit',53242500),
		(165,'HEMO-RAGE UNLEASHED от Nutrex',66982500),
		(166,'N.O.- XPLODE',73165500),
		(167,'Pole Nutrition Teazer Pre',53528800),
		(168,'Pre-Sweat Advanced Pre-Workout',52212000),
		(169,'The Curse от Cobra Nutrition',67784000),
		(170,'C4 энергетик pre	 work out original',68356500),
		(171,'Cellucor C4 Extreme Energy™(270g)',62975000),
		(172,'Moons Truck от Zoomad Labs',59540000),
		(173,'GUARANA',45800000),
		(174,'Энергетический напиток - Апельсин (500 мл)',3300000),
		(175,'Tribulus от BPI Sports 180 капсул',63204000),
		(176,'Primeval Labs APESH*T Alpha',61486500),
		(177,'Primeval Labs Apesh*t Test',65952000),
		(178,'Ultimate Nutrition Testostron Grow HP 126 Tablets',60799500),
		(179,'Tribulus terrestris от VPLab',60765200),
		(180,'Force Factor Tribulus',54960000),
		(181,'Kevin Levrone LevroTribulus 1500',51525000),
		(182,'Testrol Elite  Gat',73165500),
		(183,'MRM TRIBUPLEX 750',51525000),
		(184,'Nugenix Natural Testosterone Booster - 42',91600000),
		(185,'Test HD Thermo, Muscletech, 90',84386500),
		(186,'TribX90',60799500),
		(187,'Tribulus 1000 mg',62975000),
		(188,'Animal Pak Animal M-Stak Non-Hormonal Anabolic Stack',73165500),
		(189,'Nutrex Tribulus Black 1300',65150500),
		(190,'Tesla Turbo-X.',57250000),
		(191,'Kevin Levrone Anabolic Test 90',89310000),
		(192,'EVL Tribulus - 650 mg',48090000),
		(193,'Tribulus XS 120 caps',51525000),
		(194,'Animal Test от Universal Nutrition',113355000),
		(195,'Men"s Multi + test',54845500),
		(196,'GAT Sport Testrol65',64120000),
		(197,'Bodybuilding Signature Testosterone Booster',68700000),
		(198,'Tribulus Elite',43510000),
		(199,'RIBULUS, SOURCE NATURALS, 750',50380000),
		(200,'Universal Pro',62975000),
		(201,'Tribuvar 1000',51525000),
		(202,'Tribulus 625 ON',48090000),
		(203,'Tribulus 1100 1125 mg',56105000),
		(204,'Testosterone Booster Six Star',73165500),
		(205,'Test HD',91600000),
		(206,'P6 pm Testosterone Booster',57250000),
		(207,'Now Tribulus 500mg',50380000),
		(208,'N1-T Universal',57250000),
		(209,'EVL Test EVLUTION NUTRITION',51525000),
		(210,'Alpha Test',74425000),
		(211,'Black Tiger',85875000),
		# (212,'',),

		

        
]
		self.cursor.executemany("INSERT INTO products VALUES (?,?,?)",producti) 
		return self.connection.commit()
		
	def add_prod(self,idi,name,price):
		self.cursor.execute("INSERT INTO products VALUES ({},'{}',{})".format(idi,name,price))
		return self.connection.commit()

	def get_prod(self,idi):
		self.cursor.execute(f"SELECT * FROM  products WHERE id = {idi}")
		data = self.cursor.fetchall()
		return data