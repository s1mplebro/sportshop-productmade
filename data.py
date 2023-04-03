import sqlite3 

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